import json
import logging
import os
import random
import uuid
from pathlib import Path, PosixPath

import face_recognition
from PIL import Image

logger = logging.getLogger(__name__)

ACCEPTED_IMG_EXTENSIONS = ("png", "jpeg", "jpg")


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
                create_background_json(path, json_save_path)
        else:
            json_save_path = Path(f"{path}/faces.json")
            if "faces.json" in l_files:
                pass
            else:
                create_face_json(path, json_save_path)
        return json_save_path
    else:
        raise Exception(f"Provided path: '{path}' is neither a json or a folder")


def get_folder_img_params(folder_path: str, is_background: bool) -> list:
    """
    Read each image in 'folder_images_path' with extension 'ACCEPTED_IMG_EXTENSIONS' and creates a json with the face(s)
    parameters (list=[f_upper, f_right, f_lower, f_left]) and it's path
    :param folder_path: path to folder with the images to get the faces
    :param is_background: bool. If is_background is True, the algorithm will store ALL faces found in the image. Else
        it will save one face (because for face images only one face must appear on the image)
    :return: list with dictionaries {path, face_params} for each image on the folder 'face_images_path'
    """

    l_face_params = []
    folder_images: list = os.listdir(folder_path)
    for s_filename in folder_images:
        if s_filename.endswith(ACCEPTED_IMG_EXTENSIONS):
            im_path = Path(f"{folder_path}/{s_filename}")
            l_faces = get_face_params(im_path)

            if not is_background:  # only 1 face in each images
                if len(l_faces) == 1:
                    t_face = l_faces[0]  # only one face
                    l_face_params.append({"path": str(im_path), "t_face": t_face})
                elif len(l_faces) > 1:
                    logger.warning(f"Found more than one face in '{s_filename}'. Skipping face image")
                else:
                    logger.warning(f"No face found in '{s_filename}'. Try to make the frame a little bigger")
            else:  # background
                if l_faces:  # if there is at least one face
                    l_face_params.append({"path": str(im_path), "l_faces": l_faces})
                else:
                    logger.warning(f"No faces found in '{s_filename}' background")
        else:
            s_log = (
                f"Extensions' face image file {s_filename} not accepted. Accepted formats: {ACCEPTED_IMG_EXTENSIONS}"
            )
            logger.info(s_log)

    return l_face_params


def create_face_json(face_images_path, json_save_path) -> None:
    """
    Read each image in 'face_images_path' with extension 'ACCEPTED_IMG_EXTENSIONS' and creates a json with the face
    parameters (list=[f_upper, f_right, f_lower, f_left]) and it's path
    :param face_images_path: path to folder with the faces
    :param json_save_path: save path for the json with the parameters
    :return: None
    """
    face_params: list = get_folder_img_params(folder_path=face_images_path, is_background=False)
    json_face_params = json.dumps(face_params)

    with open(json_save_path, "w") as f:
        f.write(json_face_params)


def create_background_json(background_images_path, json_save_path) -> None:
    """
    Read each image in 'background_images_path' with extension 'ACCEPTED_IMG_EXTENSIONS' and creates a json with the
    faces parameters (list=[f_upper, f_right, f_lower, f_left]) and it's path
    :param background_images_path: path to folder with the background images
    :param json_save_path: save path for the json with the parameters
    :return: None
    """
    background_params: list = get_folder_img_params(folder_path=background_images_path, is_background=True)
    json_background_params = json.dumps(background_params)

    with open(json_save_path, "w") as f:
        f.write(json_background_params)


def check_return_png_path(im_path, root_folder):
    """
    Checks the image is in png and if not, converts it to png, saves it in the same folder and returns the new im path.
    If it is, returns the same path
    :param im_path:
    :param root_folder:
    :return:
    """
    if not im_path.endswith(".png"):

        im_name = im_path.replace("\\", "/").split("/")[-1].split(".")[0]

        im_jpg = Image.open(im_path)
        im_path = Path(f"{root_folder}/{im_name}.png")
        try:
            im_jpg.save(im_path)
            return im_path
        except IOError:
            raise
    else:
        return im_path


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
        l_background_faces = get_face_params(im_background)
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


def create_random_montage(montage_folder_path: str, b_path: str, f_path: str, only_face: bool) -> None:
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
    :return: None
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
    return


def create_montage_for_background(montage_folder_path: str, im_b_path: str, f_path: str, only_face: bool) -> None:
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
    :return: None
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
    return
