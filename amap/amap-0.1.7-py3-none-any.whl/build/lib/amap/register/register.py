import os
import logging
import numpy as np
from amap.register.brain_processor import BrainProcessor
from amap.register.brain_registration import BrainRegistration
from amap.tools import general, system
from amap.register.volume import calculate_volumes
from amap.config.atlas import Atlas

from amap.register.registration_params import RegistrationParams

flips = {
    "horizontal": (True, True, False),
    "coronal": (True, True, False),
    "sagittal": (False, True, False),
}


def save_downsampled_image(
    image,
    name,
    output_folder,
    atlas,
    x_pixel_um=0.02,
    y_pixel_um=0.02,
    z_pixel_um=0.05,
    orientation="coronal",
    n_free_cpus=2,
    sort_input_file=False,
    load_parallel=True,
):
    """

    :param image: Image to be downsampled.
    :param str name: Name of the image (for the filename and logging)
    :param output_folder: Where the image is to be saved
    :param atlas: atlas config
    :param x_pixel_um: pixel spacing in the first dimension
    :param y_pixel_um: pixel spacing in the second dimension
    :param z_pixel_um: pixel spacing in the second dimension
    :param orientation: anatomical orientation of the image
    :param n_free_cpus: how many cpus to leave free when loading data
    :param sort_input_file: Should the data be naturally sorted
    (e.g. file paths)
    :param load_parallel: If possible, load the data in parallel
    """

    logging.info(f"Downsampling image: {name}")
    logging.info("Loading data")
    brain = BrainProcessor(
        atlas,
        image,
        output_folder,
        x_pixel_um,
        y_pixel_um,
        z_pixel_um,
        original_orientation=orientation,
        load_parallel=load_parallel,
        sort_input_file=sort_input_file,
        load_atlas=False,
        n_free_cpus=n_free_cpus,
    )

    downsampled_brain_path = os.path.join(
        output_folder, f"downsampled_{name}.nii"
    )

    brain.target_brain = brain.target_brain.astype(np.uint16, copy=False)
    logging.info("Saving downsampled image")
    brain.save(downsampled_brain_path)
    del brain


class Paths:
    """
    A single class to hold all file paths that amap may need. Any paths
    prefixed with "tmp__" refer to internal intermediate steps, and will be
    deleted if "--debug" is not used.
    """

    def __init__(self, registration_output_folder):
        self.registration_output_folder = registration_output_folder
        self.make_reg_paths()

    def make_reg_paths(self):

        self.downsampled_brain_path = self.make_reg_path("downsampled.nii")
        self.tmp__downsampled_filtered = self.make_reg_path(
            "downsampled_filtered.nii"
        )
        self.registered_atlas_path = self.make_reg_path("registered_atlas.nii")
        self.hemispheres_atlas_path = self.make_reg_path(
            "registered_hemispheres.nii"
        )
        self.volume_csv_path = self.make_reg_path("volumes.csv")

        self.tmp__affine_registered_atlas_brain_path = self.make_reg_path(
            "affine_registered_atlas_brain.nii"
        )
        self.tmp__freeform_registered_atlas_brain_path = self.make_reg_path(
            "freeform_registered_atlas_brain.nii"
        )
        self.tmp__inverse_freeform_registered_atlas_brain_path = self.make_reg_path(
            "inverse_freeform_registered_brain.nii"
        )

        self.registered_atlas_img_path = self.make_reg_path(
            "registered_atlas.nii"
        )
        self.registered_hemispheres_img_path = self.make_reg_path(
            "registered_hemispheres.nii"
        )

        self.affine_matrix_path = self.make_reg_path("affine_matrix.txt")
        self.invert_affine_matrix_path = self.make_reg_path(
            "invert_affine_matrix.txt"
        )

        self.control_point_file_path = self.make_reg_path(
            "control_point_file.nii"
        )
        self.inverse_control_point_file_path = self.make_reg_path(
            "inverse_control_point_file.nii"
        )

        (
            self.tmp__affine_log_file_path,
            self.tmp__affine_error_path,
        ) = self.compute_reg_log_file_paths("affine")
        (
            self.tmp__freeform_log_file_path,
            self.tmp__freeform_error_file_path,
        ) = self.compute_reg_log_file_paths("freeform")
        (
            self.tmp__inverse_freeform_log_file_path,
            self.tmp__inverse_freeform_error_file_path,
        ) = self.compute_reg_log_file_paths("inverse_freeform")
        (
            self.tmp__segmentation_log_file,
            self.tmp__segmentation_error_file,
        ) = self.compute_reg_log_file_paths("segment")
        (
            self.tmp__invert_affine_log_file,
            self.tmp__invert_affine_error_file,
        ) = self.compute_reg_log_file_paths("invert_affine")

    def make_reg_path(self, basename):
        """
        Compute the absolute path of the destination file to
        self.registration_output_folder.

        :param str basename:
        :return: The path
        :rtype: str
        """
        return os.path.join(self.registration_output_folder, basename)

    def compute_reg_log_file_paths(self, basename):
        """
        Compute the path of the log and err file for the step corresponding
        to basename

        :param str basename:
        :return: log_file_path, error_file_path
        """

        log_file_template = os.path.join(
            self.registration_output_folder, "{}.log"
        )
        error_file_template = os.path.join(
            self.registration_output_folder, "{}.err"
        )
        log_file_path = log_file_template.format(basename)
        error_file_path = error_file_template.format(basename)
        return log_file_path, error_file_path


def main(
    registration_config,
    target_brain_path,
    registration_output_folder,
    x_pixel_um=0.02,
    y_pixel_um=0.02,
    z_pixel_um=0.05,
    orientation="coronal",
    flip_x=False,
    flip_y=False,
    flip_z=False,
    affine_n_steps=6,
    affine_use_n_steps=5,
    freeform_n_steps=6,
    freeform_use_n_steps=4,
    bending_energy_weight=0.95,
    grid_spacing_x=-10,
    smoothing_sigma_reference=-1.0,
    smoothing_sigma_floating=-1.0,
    histogram_n_bins_floating=128,
    histogram_n_bins_reference=128,
    n_free_cpus=2,
    sort_input_file=False,
    save_downsampled=True,
    additional_images_downsample=None,
    debug=False,
):
    """
        The main function that will perform the library calls and
    register the atlas to the brain given on the CLI

    :param registration_config:
    :param target_brain_path:
    :param registration_output_folder:
    :param filtered_brain_path:
    :param x_pixel_um:
    :param y_pixel_um:
    :param z_pixel_um:
    :param orientation:
    :param flip_x:
    :param flip_y:
    :param flip_z:
    :param n_free_cpus:
    :param sort_input_file:
    :param save_downsampled:
    :param additional_images_downsample: dict of
    {image_name: image_to_be_downsampled}
    :return:
    """
    paths = Paths(registration_output_folder)
    logging.info("Preprocessing data for registration")
    n_processes = system.get_num_processes(min_free_cpu_cores=n_free_cpus)
    load_parallel = n_processes > 1

    logging.info("Loading data")

    atlas = Atlas(registration_config, dest_folder=registration_output_folder)

    brain = BrainProcessor(
        atlas,
        target_brain_path,
        registration_output_folder,
        x_pixel_um,
        y_pixel_um,
        z_pixel_um,
        original_orientation=orientation,
        load_parallel=load_parallel,
        sort_input_file=sort_input_file,
        n_free_cpus=n_free_cpus,
    )

    # reorients the atlas to the orientation of the sample
    brain.swap_atlas_orientation_to_self()

    # reorients atlas to the nifti (origin is the most ventral, posterior,
    # left voxel) coordinate framework

    flip = flips[orientation]
    brain.flip_atlas(flip)

    # flips if the input data doesnt match the nifti standard
    brain.flip_atlas((flip_x, flip_y, flip_z))

    brain.atlas.save_all()
    if save_downsampled:
        brain.target_brain = brain.target_brain.astype(np.uint16, copy=False)
        logging.info("Saving downsampled image")
        brain.save(paths.downsampled_brain_path)

    brain.filter()
    logging.info("Saving filtered image")
    brain.save(paths.tmp__downsampled_filtered)

    del brain
    if additional_images_downsample:
        for name, image in additional_images_downsample.items():
            save_downsampled_image(
                image,
                name,
                registration_output_folder,
                atlas,
                x_pixel_um=x_pixel_um,
                y_pixel_um=y_pixel_um,
                z_pixel_um=z_pixel_um,
                orientation=orientation,
                n_free_cpus=n_free_cpus,
                sort_input_file=sort_input_file,
                load_parallel=load_parallel,
            )

    registration_params = RegistrationParams(
        registration_config,
        output_folder=registration_output_folder,
        affine_n_steps=affine_n_steps,
        affine_use_n_steps=affine_use_n_steps,
        freeform_n_steps=freeform_n_steps,
        freeform_use_n_steps=freeform_use_n_steps,
        bending_energy_weight=bending_energy_weight,
        grid_spacing_x=grid_spacing_x,
        smoothing_sigma_reference=smoothing_sigma_reference,
        smoothing_sigma_floating=smoothing_sigma_floating,
        histogram_n_bins_floating=histogram_n_bins_floating,
        histogram_n_bins_reference=histogram_n_bins_reference,
    )
    brain_reg = BrainRegistration(
        registration_config,
        paths,
        registration_params,
        n_processes=n_processes,
    )

    logging.info("Registering")
    logging.info("Starting affine registration")

    brain_reg.register_affine()
    logging.info("Starting freeform registration")
    brain_reg.register_freeform()

    logging.info("Generating inverse (sample to atlas) transforms")
    brain_reg.generate_inverse_transforms()

    logging.info("Starting segmentation")
    brain_reg.segment()

    logging.info("Segmenting hemispheres")
    brain_reg.register_hemispheres()

    logging.info("Registration complete")

    logging.info("Calculating volumes of each brain area")

    calculate_volumes(
        paths.registered_atlas_path,
        paths.hemispheres_atlas_path,
        atlas.get_structures_path(),
        registration_config,
        paths.volume_csv_path,
        left_hemisphere_value=atlas.get_left_hemisphere_value(),
        right_hemisphere_value=atlas.get_right_hemisphere_value(),
    )

    logging.info(
        f"Segmentation finished.Results can be found here: "
        f"{registration_output_folder}"
    )

    if not debug:
        logging.info("Removing registration temp files")
        general.delete_temp(paths.registration_output_folder, paths)
