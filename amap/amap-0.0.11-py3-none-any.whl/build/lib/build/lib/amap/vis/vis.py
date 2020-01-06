import napari
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from natsort import natsorted
from napari.util.io import magic_imread

from pathlib import Path
from vispy.color import Colormap
from brainio import brainio
from amap.utils.paths import Paths
from amap.tools.general import get_text_lines
from amap.tools.system import get_sorted_file_paths
from amap.config.config import get_config_ob

label_red = Colormap([[0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0]])


def parser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser = cli_parse(parser)
    return parser


def cli_parse(parser):
    cli_parser = parser.add_argument_group("Visualisation options")

    cli_parser.add_argument(
        dest="amap_directory",
        type=str,
        help="Path to the amap output directory..",
    )

    cli_parser.add_argument(
        "-r" "--raw",
        dest="raw",
        action="store_true",
        help="Display the raw image (as a virtual stack) "
        "rather than the downsampled",
    )
    cli_parser.add_argument(
        "-c",
        "--raw-channels",
        dest="raw_channels",
        type=str,
        nargs="+",
        help="Paths to N additional raw channels to view. Will only work if "
             "using the raw image viewer.",
    )

    return parser


def get_most_recent_log(directory, log_pattern="amap*.log"):
    """
    Returns the most recent amap log file (for parsing of arguments)
    :param directory:
    :param log_pattern: String pattern that defines the log
    :return: Path to the most recent log file
    """
    directory = Path(directory)
    return natsorted(directory.glob(log_pattern))[-1]


def read_log_file(
    log_file,
    log_entries_to_get=[
        "x_pixel_um",
        "y_pixel_um",
        "z_pixel_um",
        "image_paths",
        "registration_config",
    ],
    separator=": ",
):
    """
    Reads an amap log file, and returns a dict of entries corresponding to
    "log_entries_to_get"
    :param log_file: Path to the log file
    :param log_entries_to_get: List of strings corresponding to entries
    in the log file
    :param separator: Separator between the log item label and the entry.
    Default: ": "
    :return: A dict of the entries and labels
    """
    lines = get_text_lines(log_file)
    entries = {}
    for line in lines:
        for entry in log_entries_to_get:
            if line.startswith(entry):
                entries[entry] = line.strip(entry + separator)

    return entries


def prepare_load_nii(nii_path):
    """
    Transforms a nii file into the same coordinate space as the raw data
    :param nii_path: Path to the nii file
    :return: Numpy array in the correct coordinate space
    """
    nii_path = str(nii_path)
    image = brainio.load_any(nii_path)
    image = np.swapaxes(image, 2, 0)
    return image


def load_additional_downsampled_images(
    viewer,
    amap_directory,
    paths,
    search_string="downsampled_",
    extension=".nii",
):
    """
    Loads additional downsampled (i.e. from nii) images into napari viewer
    :param viewer: Napari viewer object
    :param amap_directory: Directory containing images
    :param paths: amap paths object
    :param search_string: String that defines the images.
    Default: "downampled_"
    :param extension: File extension of the downsampled images. Default: ".nii"
    """

    amap_directory = Path(amap_directory)

    for file in amap_directory.iterdir():
        if (
            (file.suffix == ".nii")
            and file.name.startswith(search_string)
            and file != Path(paths.downsampled_brain_path)
            and file != Path(paths.tmp__downsampled_filtered)
        ):
            print(
                f"Found additional downsampled image: {file.name}, "
                f"adding to viewer"
            )
            name = file.name.strip(search_string).strip(extension)
            viewer.add_image(
                prepare_load_nii(file), name=name,
            )


def add_raw_image(viewer, image_path, name):
    """
    Add a raw image (as a virtual stack) to the napari viewer
    :param viewer: Napari viewer object
    :param image_path: Path to the raw data
    :param str name: Name to give the data
    """
    paths = get_sorted_file_paths(image_path, file_extension=".tif")
    images = magic_imread(paths, use_dask=True, stack=True)
    viewer.add_image(images, name=name, opacity=0.6, blending="additive")


def get_image_scales(log_entries):
    """
    Returns the scaling from downsampled data to raw data
    :param log_entries:
    :return: Tuple of scaling factors
    """
    config_obj = get_config_ob(log_entries["registration_config"])
    atlas_conf = config_obj["atlas"]
    pixel_sizes = atlas_conf["pixel_size"]
    x_scale = float(pixel_sizes["x"]) / float(log_entries["x_pixel_um"])
    y_scale = float(pixel_sizes["y"]) / float(log_entries["y_pixel_um"])
    z_scale = float(pixel_sizes["z"]) / float(log_entries["z_pixel_um"])
    return z_scale, y_scale, x_scale


def display_raw(viewer, args):
    """
    Display raw data
    :param viewer:
    :param args:
    :return:
    """
    print(
        "Starting raw image viewer. Streaming full-resolution data."
        " This may be slow."
    )
    log_entries = read_log_file(get_most_recent_log(args.amap_directory))

    image_scales = get_image_scales(log_entries)
    add_raw_image(viewer, log_entries["image_paths"], name="Raw data")

    if args.raw_channels:
        for raw_image in args.raw_channels:
            name = Path(raw_image).name
            print(f"Found additional raw image to add to viewer: " f"{name}")
            add_raw_image(viewer, raw_image, name=name)

    return image_scales


def display_downsampled(viewer, args, paths):
    """
    Display downsampled data
    :param viewer:
    :param args:
    :param paths:
    :return:
    """
    image_scales = (1, 1, 1)
    load_additional_downsampled_images(viewer, args.amap_directory, paths)

    viewer.add_image(
        prepare_load_nii(paths.downsampled_brain_path),
        name="Downsampled raw data",
    )

    return image_scales


def display_registration(viewer, atlas, boundaries, image_scales):
    """
    Display results of the registration
    :param viewer: napari viewer object
    :param atlas: Annotations in sample space
    :param boundaries: Annotation boundaries in sample space
    :param tuple image_scales: Scaling of images from annotations -> data
    """
    viewer.add_labels(
        prepare_load_nii(atlas),
        name="Annotations",
        opacity=0.2,
        scale=image_scales,
    )
    viewer.add_image(
        prepare_load_nii(boundaries),
        name="Outlines",
        contrast_limits=[0, 1],
        colormap=("label_red", label_red),
        scale=image_scales,
    )


def main():
    print("Starting amap viewer")
    args = parser().parse_args()

    paths = Paths(args.amap_directory)
    with napari.gui_qt():
        v = napari.Viewer(title="amap viewer")
        if (
            Path(paths.registered_atlas_path).exists()
            and Path(paths.boundaries_file_path).exists()
        ):

            if args.raw:
                image_scales = display_raw(v, args)

            else:
                if Path(paths.downsampled_brain_path).exists():
                    image_scales = display_downsampled(v, args, paths)

                else:
                    raise FileNotFoundError(
                        f"The downsampled image: "
                        f"{paths.downsampled_brain_path} could not be found. "
                        f"Please ensure this is the correct "
                        f"directory and that amap has completed. "
                    )

            display_registration(
                v,
                paths.registered_atlas_path,
                paths.boundaries_file_path,
                image_scales,
            )

        else:
            raise FileNotFoundError(
                f"The directory: '{args.amap_directory} does not "
                f"appear to be complete. Please ensure this is the correct "
                f"directory and that amap has completed."
            )


if __name__ == "__main__":
    main()
