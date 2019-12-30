# coding: utf-8
#
# Refs:
# - https://opencv-python-tutroals.readthedocs.io/en/latest/

import base64
import logging
import os
import re
import time
from typing import Union

import cv2
import findit
import numpy as np
import requests
from logzero import setup_logger
from PIL import Image, ImageDraw
from skimage.metrics import structural_similarity
import imutils


compare_ssim = structural_similarity


def color_bgr2gray(image: Union[np.ndarray, Image.Image]):
    """ change color image to gray
    Returns:
        opencv-image
    """
    if ispil(image):
        image = pil2cv(image)

    if len(image.shape) == 2:
        return image
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def template_ssim(image_a, image_b):
    """
    Refs:
        https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
    """
    a = color_bgr2gray(image_a)
    b = color_bgr2gray(image_b) # template (small)
    res = cv2.matchTemplate(a, b, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val


def compare_ssim(image_a, image_b, full=False):
    a = color_bgr2gray(image_a)
    b = color_bgr2gray(image_b) # template (small)
    return structural_similarity(a, b, full=full)


def compare_ssim_debug(image_a, image_b, color=(255, 0, 0)):
    """
    Args:
        image_a, image_b: opencv image or PIL.Image
        color: (r, g, b) eg: (255, 0, 0) for red

    Refs:
        https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
    """
    ima, imb = conv2cv(image_a), conv2cv(image_b)
    score, diff = compare_ssim(ima, imb, full=True)
    diff = (diff * 255).astype('uint8')
    _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    cv2color = tuple(reversed(color))
    im = ima.copy()
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(im, (x, y), (x+w, y+h), cv2color, 2)
    # todo: show image
    cv2pil(im).show()
    return im


def show_image(im: Union[np.ndarray, Image.Image]):
    pilim = conv2pil(im)
    pilim.show()


def pil2cv(pil_image):
    """ Convert from pillow image to opencv """
    # convert PIL to OpenCV
    pil_image = pil_image.convert('RGB')
    cv2_image = np.array(pil_image)
    # Convert RGB to BGR
    cv2_image = cv2_image[:, :, ::-1].copy()
    return cv2_image


def cv2pil(cv_image):
    """ Convert opencv to pillow image """
    return Image.fromarray(cv_image[:, :, ::-1].copy())


def iscv2(im):
    return isinstance(im, np.ndarray)


def ispil(im):
    return isinstance(im, Image.Image)


def conv2cv(im: Union[np.ndarray, Image.Image]) -> np.ndarray:
    if iscv2(im):
        return im
    if ispil(im):
        return pil2cv(im)
    raise TypeError("Unknown image type:", type(im))


def conv2pil(im: Union[np.ndarray, Image.Image]) -> Image.Image:
    if ispil(im):
        return im
    elif iscv2(im):
        return cv2pil(im)
    else:
        raise TypeError(f"Unknown image type: {type(im)}")


def _open_data_url(data, flag=cv2.IMREAD_COLOR):
    pos = data.find('base64,')
    if pos == -1:
        raise IOError("data url is invalid, head %s" % data[:20])

    pos += len('base64,')
    raw_data = base64.decodestring(data[pos:])
    image = np.asarray(bytearray(raw_data), dtype="uint8")
    image = cv2.imdecode(image, flag)
    return image


def _open_image_url(url: str, flag=cv2.IMREAD_COLOR):
    """ download the image, convert it to a NumPy array, and then read
    it into OpenCV format """
    content = requests.get(url).content
    image = np.asarray(bytearray(content), dtype="uint8")
    image = cv2.imdecode(image, flag)
    return image


def draw_point(im: Image.Image, x: int, y: int):
    """
    Mark position to show which point clicked

    Args:
        im: pillow.Image
    """
    draw = ImageDraw.Draw(im)
    w, h = im.size
    draw.line((x, 0, x, h), fill='red', width=5)
    draw.line((0, y, w, y), fill='red', width=5)
    r = min(im.size) // 40
    draw.ellipse((x - r, y - r, x + r, y + r), fill='red')
    r = min(im.size) // 50
    draw.ellipse((x - r, y - r, x + r, y + r), fill='white')
    del draw
    return im


def imread(data):
    """
    Args:
        data: local path or http url or data:image/base64,xxx
    
    Returns:
        opencv image
    
    Raises:
        IOError
    """
    if isinstance(data, np.ndarray):
        return data
    elif isinstance(data, Image.Image):
        return pil2cv(data)
    elif data.startswith('data:image/'):
        return _open_data_url(data)
    elif re.match(r'^https?://', data):
        return _open_image_url(data)
    elif os.path.isfile(data):
        im = cv2.imread(data)
        if im is None:
            raise IOError("Image format error: %s" % data)
        return im

    raise IOError("image read invalid data: %s" % data)


class ImageX(object):
    def __init__(self, d: "uiautomator2.Device"):
        """
        Args:
            d (uiautomator2 instance)
        """
        self.logger = setup_logger()
        self._d = d
        assert hasattr(d, 'click')
        assert hasattr(d, 'screenshot')

        # self.logger.setLevel(logging.INFO)

    def send_click(self, x, y):
        return self._d.click(x, y)
    
    def getpixel(self, x, y):
        """
        Returns:
            (r, g, b)
        """
        screenshot = self.screenshot()
        return screenshot.convert("RGB").getpixel((x, y))

    def match(self, imdata: Union[np.ndarray, str]):
        """
        Args:
            imdata: file, url, pillow or opencv image object
        
        Returns:
            templateMatch result
        """
        cvimage = imread(imdata)
        fi = findit.FindIt(engine=['template'],
                           engine_template_scale=(0.9, 1.1, 3),
                           pro_mode=True)
        fi.load_template("template", pic_object=cvimage)

        target = self._d.screenshot(format='opencv')
        raw_result = fi.find("target", target_pic_object=target)
        result = raw_result['data']['template']['TemplateEngine']
        target_sim = result['target_sim']  # 相似度  similarity

        return {"similarity": target_sim, "point": result['target_point']}

    def __wait(self, imdata, timeout=30.0, threshold=0.8):
        deadline = time.time() + timeout
        while time.time() < deadline:
            m = self.match(imdata)
            sim = m['similarity']
            self.logger.debug("similarity %.2f [~%.2f], left time: %.1fs", sim,
                              threshold, deadline - time.time())
            if sim < threshold:
                continue
            time.sleep(.1)
            return m

    def wait(self, imdata, timeout=30.0):
        m = self.__wait(imdata, timeout=timeout, threshold=0.8)
        if m is None:
            return m
        # time.sleep(.1)
        return self.__wait(imdata, timeout=timeout, threshold=0.9)

    def click(self, imdata, timeout=30.0):
        """
        Args:
            imdata: file, url, pillow or opencv image object
        """
        res = self.wait(imdata, timeout=timeout)
        if res is None:
            raise RuntimeError("image object not found")
        x, y = res['point']
        return self.send_click(x, y)


def _main():
    ima = imread("http://localhost:17310/widgets/00006/template.jpg")
    imb = imread("http://localhost:17310/widgets/00007/template.jpg")
    compare_ssim_debug(ima, imb, color=(0, 0, 255))
    return
    im = imread("https://www.baidu.com/img/bd_logo1.png")
    assert im.shape == (258, 540, 3)
    print(im.shape)

    im = imread("../tests/testdata/AE86.jpg")
    print(im.shape)
    assert im.shape == (193, 321, 3)

    pim = cv2pil(im)
    assert pim.size == (321, 193)

    taobao = imread("screenshot.jpg")
    import findit

    fi = findit.FindIt(engine=['template'],
                       engine_template_scale=(1, 1, 1),
                       pro_mode=True)
    fi.load_template("template", pic_object=taobao)


if __name__ == "__main__":
    _main()

    # import uiautomator2 as u2
    # d = u2.connect()
    # bg = d.screenshot(format="opencv")
    # res = fi.find("target", target_pic_object=bg)
    # from pprint import pprint
    # pprint(res)
    # {'target_name': 'target',
    #  'target_path': None,
    #  'data': {
    #       'template': {
    #           'TemplateEngine': {
    #               'conf': {
    #                   'engine_template_cv_method_name': 'cv2.TM_CCOEFF_NORMED',
    #                   'engine_template_cv_method_code': 5,
    #                   'engine_template_scale': (1, 1, 1),
    #                   'engine_template_multi_target_max_threshold': 0.99,
    #                   'engine_template_multi_target_distance_threshold': 10.0,
    #                   'engine_template_compress_rate': 1.0},
    #               'target_point': [111, 1713],
    #               'target_sim': 0.9984192848205566,
    #               'raw': {'min_val': -0.4805332124233246,
    #               'max_val': 0.9984192848205566,
    #               'min_loc': [990, 1266],
    #               'max_loc': [111, 1713],
    #               'all': [[111.0, 1713.5]]},
    #               'ok': True}}}}
    # x, y = res["data"]["template"]["TemplateEngine"]["target_point"]
    # d.click(x, y)
