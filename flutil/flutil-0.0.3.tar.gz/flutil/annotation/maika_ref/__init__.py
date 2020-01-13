from ..parser import Parser
from .. import Annotation
from typing import List
from PIL import Image
import os.path


class MaikaRefParser(Parser):
    """
    A ``Parser`` that uses the filename of an image to parse the ID.
    """
    @staticmethod
    def parse_single(annot_file: str) -> List[Annotation]:
        """Return the annotations in the annotation file.

        :param str annot_file: the path of the annotation file, in
        this case this is simply an image file
        :returns: the annotations in the annotation file
        :rtype: List[Annotation]
        """
        basename = os.path.basename(annot_file)
        filename = os.path.splitext(basename)[0]
        _id = ''.join([c for c in filename
                       if not c.isdigit() or c == ' '])
        img = Image.open(annot_file)
        width, height = img.size
        return [Annotation(label=_id,
                           x_min=0,
                           y_min=0,
                           x_max=width,
                           y_max=height)]
