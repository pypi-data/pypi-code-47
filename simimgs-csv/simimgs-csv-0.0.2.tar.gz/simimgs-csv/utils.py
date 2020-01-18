import time
import cv2
import numpy
from skimage.metrics import structural_similarity


def timed_call(f, args):
    """Call function f with arguments args and time its run time.

    Args:
        f: The function to call
        args: The arguments to pass to f

    Returns:
        Return the result of the function call and how much time it takes as tuple e.g. (result, time).
    """
    start_time = time.time()
    result = f(*args)
    elapsed_time = time.time() - start_time
    return result, round(elapsed_time, 3)


def get_similarity(image1_path: str, image2_path: str) -> float:
    """Compute image similarity between a pair of images pointed by image1_path nad image2_path using SSIM.

    Args:
        image1_path: File Path to image 1.
        image2_path: File Path to image 2.

    Returns:
        A score between 0 and 1(inclusive on both ends). 0 means identical images and 1 means completely
        different images.
    """
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    img2 = numpy.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
    score = 1 - structural_similarity(img1, img2, multichannel=True)
    return round(score, 2)
