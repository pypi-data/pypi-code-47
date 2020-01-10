import tempfile
import napari
import numpy as np
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from pathlib import Path
from vispy.color import Colormap
from brainio import brainio
from amap.utils.paths import Paths

temp_dir = tempfile.TemporaryDirectory()
temp_dir_path = temp_dir.name


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

    return parser


label_red = Colormap([[0.0, 0.0, 0.0, 0.0], [1.0, 1.0, 1.0, 1.0]])


def load_prepare_image(path):
    image = brainio.load_any(path)
    image = np.swapaxes(image, 2, 0)
    return image


def main():
    print("Starting amap viewer")
    args = parser().parse_args()

    paths = Paths(args.amap_directory)
    if (
        Path(paths.downsampled_brain_path).exists()
        and Path(paths.registered_atlas_path).exists()
        and Path(paths.boundaries_file_path).exists()
    ):
        with napari.gui_qt():
            v = napari.Viewer(title="amap viewer")
            v.add_image(
                load_prepare_image(paths.downsampled_brain_path),
                name="Downsampled raw data",
            )
            v.add_labels(
                load_prepare_image(paths.registered_atlas_path),
                name="Annotations",
                opacity=0.2,
            )
            v.add_image(
                load_prepare_image(paths.boundaries_file_path),
                name="Outlines",
                contrast_limits=[0, 1],
                colormap=("label_red", label_red),
            )
    else:
        raise FileNotFoundError(
            f"The directory: '{args.amap_directory} does not "
            f"appear to be complete. Please ensure this is the correct "
            f"directory and that amap has completed."
        )


if __name__ == "__main__":
    main()
