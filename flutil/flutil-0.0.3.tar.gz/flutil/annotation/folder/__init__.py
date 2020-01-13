from ..parser import Parser
from .. import Annotation
from typing import List
from PIL import Image
import os.path


class FolderParser(Parser):
    """
    A ``Parser`` that uses the folder name of an image to parse the ID.
    """
    @staticmethod
    def parse_single(annot_file: str) -> List[Annotation]:
        """Return the annotations in the annotation file.

        :param str annot_file: the path of the annotation file, in
        this case this is simply an image file
        :returns: the annotations in the annotation file
        :rtype: List[Annotation]
        """
        folder = os.path.basename(os.path.dirname(annot_file))
        img = Image.open(annot_file)
        width, height = img.size
        return [Annotation(label=folder,
                           x_min=0,
                           y_min=0,
                           x_max=width,
                           y_max=height)]
