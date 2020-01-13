"""
An Inputter provides the images.
"""
import time
from pathlib import Path
from PIL import Image
import cv2
from typing import Union, List

__all__ = [
    'Inputter',
    'DummyInputter',
    'WebcamInputter'
]


class Inputter:
    def __init__(self, delay=0, bs=1, has_aois=False):
        """
        :param int delay: the delay in milliseconds after yielding a list of
        images
        :param int bs: the batch size, i.e. how many images to yield per
        iteration
        :param bool has_aois: whether the yielded inputs contain a list of
        areas of interest to use for the image. Default: `False`
        """
        self.delay = delay
        self.bs = bs
        self.has_aois = has_aois

    def next_single(self):
        raise NotImplementedError

    def __next__(self):
        """Return the next list of inputs."""
        time.sleep(self.delay / 1000)
        inps = []
        for _ in range(self.bs):
            inps.append(self.next_single())

        return inps

    def __iter__(self):
        """Yield an input per iteration. When `self.has_aois` is `True`, the
        yielded input will be a tuple of a `PIL.Image` and a list of areas of
        interest for that image. When `self.has_aois` is `False`, the yielded
        input will simply be a `PIL.Image`."""
        while(True):
            try:
                yield next(self)
            except StopIteration:
                break


class DummyInputter(Inputter):
    def __init__(self, imgs: Union[Path, List[Path]], delay=0, bs=1,
                 img_to_aois: callable=None, recursive=False):
        """
        :param Union[Path, List[Path]] img_dir: directory containing the images
        to use, or a list of paths to the image files themselves
        :param int delay: the delay in milliseconds after yielding an image
        :param int bs: the batch size, i.e. how many images to yield per
        iteration
        :param callable img_to_aois: (optional) function taking the path of an
        image as input and returning a list of areas of interest to use for
        that image.
        :param bool recurive: recursively look for images in subdirectories of
        the given directory
        """
        super().__init__(delay=delay, bs=bs, has_aois=img_to_aois is not None)

        self.img_to_aois = img_to_aois
        if isinstance(imgs, Path):
            glob = imgs.rglob if recursive else imgs.glob
            self.img_gen = (p for p in glob('*')
                            if p.suffix.lower() in ['.jpg', '.jpeg', '.bmp',
                                                    '.png'])
        elif isinstance(imgs, List):
            self.img_gen = (p for p in imgs)

    def next_single(self):
        img = next(self.img_gen)

        if self.img_to_aois is not None:
            aois = self.img_to_aois(img)
            return img, aois
        else:
            return img


class WebcamInputter(Inputter):
    def __init__(self, camera=0, delay=0, bs=1, aois=None,
                 release_after_read=False, mirror=False):
        """
        :param int camera: the camera code to use for `cv2.VideoCapture`
        :param int delay: the delay in milliseconds after yielding an image
        :param int bs: the batch size, i.e. how many images to yield per
        iteration
        :param List aois: the aois for a webcam frame
        :param bool release_after_read: whether to release the webcam after a
        frame capture
        :param bool mirror: mirror the webcam input
        """
        super().__init__(delay=delay, bs=bs, has_aois=aois is not None)

        # Set up video capture
        self.camera = camera
        self.capture = cv2.VideoCapture(camera)
        self.release_after_read = release_after_read
        self.aois = aois
        self.mirror = mirror

    def next_single(self):
        if not self.capture.isOpened():
            self.capture.open(self.camera)
        _, frame = self.capture.read()

        if self.release_after_read:
            self.capture.release()

        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = cv2.flip(im, 1)
        if self.aois is not None:
            return Image.fromarray(im), self.aois
        else:
            return Image.fromarray(im)

    def __del__(self):
        self.capture.release()
