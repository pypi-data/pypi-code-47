import logging
import os

import face_recognition

from pathlib import Path

ACCEPTED_IMG_EXTENSIONS = ("png", "jpeg", "jpg")

logger = logging.getLogger(__name__)


def get_face_params(im_path: str) -> list:
    """
    From an image path, return the list of faces in the image
    :param im_path: str image path
    :return: return list of list=[f_upper, f_right, f_lower, f_left] for each face found
    """
    im = face_recognition.load_image_file(im_path)
    l_faces = face_recognition.face_locations(im)
    logger.debug(f"Found {len(l_faces)} faces in image {im_path}")
    return l_faces


def get_folder_img_params(folder_path: str, is_background: bool, old_json: list) -> list:
    """
    Read each image in 'folder_images_path' with extension 'ACCEPTED_IMG_EXTENSIONS' and creates a json with the face(s)
    parameters (list=[f_upper, f_right, f_lower, f_left]) and it's path
    :param folder_path: path to folder with the images to get the faces
    :param is_background: bool. If is_background is True, the algorithm will store ALL faces found in the image. Else
        it will save one face (because for face images only one face must appear on the image)
    :param old_json: {list of dicts} old json if any. Will try only to update the parameters for the new and deleted
        images, not the ones already present
    :return: list with dictionaries {path, face_params} for each image on the folder 'face_images_path'
    """

    l_params = []
    old_paths = {face["path"]: face["t_face"] for face in old_json}

    # remove images with incorrect extensions
    img_folder_paths = [Path(f"{folder_path}/{filename}") for filename in os.listdir(folder_path)]
    for img_path in img_folder_paths:
        if not str(img_path).endswith(ACCEPTED_IMG_EXTENSIONS):
            img_path: Path  # cast typing because it is stuck with str instead of Path

            # erase from folder paths
            img_folder_paths.remove(img_path)
            s_log = (
                f"Extensions' face image file {img_path.name} not accepted. Accepted formats: {ACCEPTED_IMG_EXTENSIONS}"
            )
            logger.warning(s_log)
        elif str(img_path) in old_paths.keys():
            d_params = {str(img_path): old_paths[img_path]}
            l_params.append(d_params)

            # and remove the image because we don't want it to process it again
            img_folder_paths.remove(img_path)
        else:  # new image and accepted format
            continue

    for im_path in img_folder_paths:
        l_faces = get_face_params(im_path)
        if not is_background:  # only 1 face in each images
            if len(l_faces) == 1:
                t_face = l_faces[0]  # only one face
                l_params.append({"path": str(im_path), "t_face": t_face})
            elif len(l_faces) > 1:
                logger.warning(f"Found more than one face in '{im_path.name}'. Skipping face image")
            else:
                logger.warning(f"No face found in '{im_path.name}'. Try to make the frame a little bigger")
        else:  # background
            if l_faces:  # if there is at least one face
                l_params.append({"path": str(im_path), "l_faces": l_faces})
            else:
                logger.warning(f"No faces found in '{im_path.name}' background")

    return l_params
