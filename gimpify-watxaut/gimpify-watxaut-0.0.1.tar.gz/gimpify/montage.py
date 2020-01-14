import json
import logging
import os
import random
import uuid
from pathlib import Path, PosixPath

from PIL import Image

import gimpify.helpers as helpers

logger = logging.getLogger(__name__)


def get_or_create_params_json(path: str, is_background: bool) -> str:
    """
    If path endswith .json returns the json. If the path is a folder and inside that folder there is already a
    faces.json or backgrounds.json, then returns this path, else creates the json for the path and returns the path
    :param path: str. json path or folder with images path
    :param is_background: bool. If the images are either backgrounds or faces
    :return: str with json path
    """
    path = Path(path)
    if str(path).endswith(".json"):
        return path
    elif os.path.isdir(path):
        l_files = os.listdir(path)
        if is_background:
            json_save_path = Path(f"{path}/backgrounds.json")
            if "backgrounds.json" in l_files:
                pass
            else:
                create_background_json(path, json_save_path, just_update=True)
        else:
            json_save_path = Path(f"{path}/faces.json")
            if "faces.json" in l_files:
                pass
            else:
                create_face_json(path, json_save_path, just_update=True)
        return json_save_path
    else:
        raise Exception(f"Provided path: '{path}' is neither a json or a folder")


def create_face_json(face_images_path, json_save_path, just_update=True) -> None:
    """
    Read each image in 'face_images_path' with extension 'ACCEPTED_IMG_EXTENSIONS' and creates a json with the face
    parameters (list=[f_upper, f_right, f_lower, f_left]) and it's path
    :param face_images_path: {str} path to folder with the faces
    :param json_save_path: {str} save path for the json with the parameters
    :param just_update: {bool, optional} if True, it will only get the new images in the folder and delete the ones that
        do not appear. *The ones present will not be updated for faster processing*
    :return: None
    """

    # if the json file exists (we created it before) and we just want to update
    if os.path.isfile(json_save_path) and just_update:
        with open(json_save_path, "r") as f:
            json_faces = json.load(f)
    else:
        json_faces = []

    face_params: list = helpers.get_folder_img_params(
        folder_path=face_images_path, is_background=False, old_json=json_faces
    )
    json_face_params = json.dumps(face_params)

    with open(json_save_path, "w") as f:
        f.write(json_face_params)


def create_background_json(background_images_path, json_save_path, just_update=True) -> None:
    """
    Read each image in 'background_images_path' with extension 'ACCEPTED_IMG_EXTENSIONS' and creates a json with the
    faces parameters (list=[f_upper, f_right, f_lower, f_left]) and it's path
    :param background_images_path: path to folder with the background images
    :param json_save_path: save path for the json with the parameters
    :param just_update: {bool, optional} if True, it will only get the new images in the folder and delete the ones that
    do not appear. *The ones present will not be updated for faster processing*
    :return: None
    """

    # if the json file exists (we created it before) and we just want to update
    if os.path.isfile(json_save_path) and just_update:
        with open(json_save_path, "r") as f:
            json_faces = json.load(f)
    else:
        json_faces = []

    background_params: list = helpers.get_folder_img_params(
        folder_path=background_images_path, is_background=True, old_json=json_faces
    )
    json_background_params = json.dumps(background_params)

    with open(json_save_path, "w") as f:
        f.write(json_background_params)


def create_montage(im_background: [dict, str], json_faces: dict, only_face: bool) -> Image.Image:
    """
    Creates image with the montage. im_background can be an image path or a json dict. json_faces has to be a json
    loaded of the faces folder. only_face param will crop only the face or leave the hair and chin if False
    :param im_background: str if is an image path or dict if it comes from a json read from a background's folder
    :param json_faces: dict read from a json from the faces folder
    :param only_face: bool. Will leave hair and chin if False, else will crop the image
    :return: Image.Image instance from PIL with the montage
    """
    if type(im_background) is dict:
        im_path = im_background["path"]
        l_background_faces = im_background["l_faces"]
    elif type(im_background) in [str, PosixPath]:
        im_path = str(im_background)
        l_background_faces = helpers.get_face_params(im_background)
    else:
        raise Exception("im_background has to be one of [dict, str]")

    # load base (background) image
    im_base: Image.Image = Image.open(im_path)

    f_factor = 1.1  # multiplies width and creates the width of the new face

    # face with this method gets pasted to high. The greater it is, the lower the face will be pasted
    f_moderate_height = 0.15

    for l_face in l_background_faces:

        # get image props
        upper, right, lower, left = l_face
        width = right - left
        height = lower - upper

        # get a random face from the list of faces
        i = random.randint(0, len(json_faces) - 1)
        d_face = json_faces[i]

        # load face
        im_face = Image.open(d_face["path"])

        # get face props
        f_upper, f_right, f_lower, f_left = d_face["t_face"]
        face_width = f_right - f_left
        face_height = f_lower - f_upper

        if not only_face:  # if the full face is needed (with hair)

            # calculate the aspect ratio of the face to keep it the same when resizing
            k_aspect_ratio_face = im_face.size[0] / im_face.size[1]

            # calculate how big (or small) is the face compared with the one in the image
            k_factor_width = face_width / width
            face_new_width = int(im_face.size[0] / k_factor_width * f_factor)
            face_new_height = int(face_new_width / k_aspect_ratio_face)

            # calculate the point to paste the image
            p1 = [
                int(left - (face_new_width / face_width * f_left)),
                int((upper - (face_new_height / face_height) * f_upper)),
            ]
            p1[1] = p1[1] + int(face_new_height * f_moderate_height)
            p1 = tuple(p1)

            # resize the face and paste it into the background image
            im_face_aux = im_face.resize((face_new_width, face_new_height), Image.ANTIALIAS)
            im_base.paste(im_face_aux, p1, im_face_aux)

        else:  # if only the face needs to get pasted it's easier

            # just crop the new face, resize it to match the background face and paste it
            im_face = im_face.crop((f_left, f_upper, f_right, f_lower))

            im_face_aux = im_face.resize((width, height), Image.ANTIALIAS)
            im_base.paste(im_face_aux, (left, upper), im_face_aux)

    return im_base


def create_random_montage(montage_folder_path: str, b_path: str, f_path: str, only_face: bool) -> str:
    """
    Creates and saves the montage from background and faces folders. If folders are provided, it will create a file
    'backgrounds.json' or 'faces.json' inside the folders for faster loading if used repeatedly. If new images are
    introduced in the folders, delete the json and the next time 'create_random_montage' is called, it will be
    created automatically.
    :param montage_folder_path: folder to save the montage
    :param b_path: folder background path or json with the face params. If folder provided, the 'backgrounds.json' file
        will be created inside the backgrounds' folder
    :param f_path: folder face path or json with the face's params. If folder provided, the 'faces.json' file
        will be created inside the faces' folder
    :param only_face: Whether to crop the hair and chin of the face or not
    :return: str with montage file path
    """

    # if a json is provided, use the json. If a folder is provided, look for a json inside. If no json inside, create it
    json_b_path = get_or_create_params_json(b_path, is_background=True)
    json_f_path = get_or_create_params_json(f_path, is_background=False)

    # read json's from backgrounds and faces
    f_backgrounds = open(json_b_path, "r")
    json_backgrounds: dict = json.load(f_backgrounds)
    f_backgrounds.close()
    f_faces = open(json_f_path, "r")
    json_faces: dict = json.load(f_faces)
    f_faces.close()

    # get random background
    i = random.randint(0, len(json_backgrounds) - 1)
    im_background = json_backgrounds[i]

    im_montage = create_montage(im_background, json_faces, only_face)  # creates the montage
    montage_file_path = Path(f"{montage_folder_path}/montage_{uuid.uuid4().hex[:10]}.png")
    try:
        im_montage.save(montage_file_path)
    except IOError:
        logger.error("Montage created but error while saving montage")
        raise

    logger.info(f"Montage created and saved in '{montage_file_path}'")
    return str(montage_file_path)


def create_montage_for_background(montage_folder_path: str, im_b_path: str, f_path: str, only_face: bool) -> str:
    """
    Creates and saves the montage from a designed background. If a folder is provided for faces, it will create a file
    'faces.json' inside the folder for faster loading if used repeatedly. If new images are
    introduced in the faces' folder, delete the json and the next time 'create_montage_for_background' is called,
    it will be created automatically.
    :param montage_folder_path: folder to save the montage
    :param im_b_path: str with the background image path
    :param f_path: folder face path or json with the face's params. If folder provided, the 'faces.json' file
        will be created inside the faces' folder
    :param only_face: Whether to crop the hair and chin of the face or not
    :return: str with montage path
    """
    json_f_path = get_or_create_params_json(f_path, is_background=False)
    f_faces = open(json_f_path, "r")
    json_faces: dict = json.load(f_faces)
    f_faces.close()

    im_montage = create_montage(im_b_path, json_faces, only_face)  # creates the montage
    montage_file_path = Path(f"{montage_folder_path}/montage_{uuid.uuid4().hex[:10]}.png")
    try:
        im_montage.save(montage_file_path)
    except IOError:
        logger.error("Montage created but error while saving montage")
        raise

    logger.info(f"Montage created and saved in '{montage_file_path}'")
    return str(montage_file_path)
