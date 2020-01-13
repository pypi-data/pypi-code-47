from ..parser import Parser
from .. import Annotation
from typing import List
from PIL import Image


class NoAnnotationParser(Parser):
    """
    A ``Parser`` that simply uses the image file path as a label and the full
    image size as a bounding box.
    """
    @staticmethod
    def parse_single(annot_file: str) -> List[Annotation]:
        """Return the annotations in the annotation file.

        :param str annot_file: the path of the annotation file, in
        this case this is simply an image file
        :returns: the annotations in the annotation file
        :rtype: List[Annotation]
        """
        img = Image.open(annot_file)
        width, height = img.size
        return [Annotation(label=annot_file,
                           x_min=0,
                           y_min=0,
                           x_max=width,
                           y_max=height)]
