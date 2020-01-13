from ..parser import Parser
from .. import Annotation
from PIL import Image
import os.path
import re


class UnderScoreX2Parser(Parser):
    """
    A ``Parser`` that uses the part between two undescores (__) and the image
    extension as a label and the full image size as a bounding box.
    """
    @staticmethod
    def parse_single(annot_file):
        """Return the annotations in the annotation file.

        :param str annot_file: the path of the annotation file, in
        this case this is simply an image file
        :returns: the annotations in the annotation file
        :rtype: List[Annotation]
        """
        basename = os.path.basename(annot_file)
        p = re.compile('__([^.]*)\.(?:jpg|gif|png)')
        m = p.search(basename)
        if m and len(m.groups()) == 1:
            label = m.groups()[0]
        else:
            return []
        img = Image.open(annot_file)
        width, height = img.size
        return [Annotation(label=label,
                           x_min=0,
                           y_min=0,
                           x_max=width,
                           y_max=height)]
