from ..parser import Parser
from .. import Annotation
from typing import List
from PIL import Image
import re


class OpenReidParser(Parser):
    @staticmethod
    def parse_single(annot_file: str) -> List[Annotation]:
        """Return the annotations in the annotation file.

        :param str annot_file: the path of the annotation file, in
        this case this is simply an image file
        :returns: the annotations in the annotation file
        :rtype: List[Annotation]
        """
        pimg = Image.open(annot_file)
        pattern = ('(?P<person_id>\d{8})'
                   '_(?P<camera_id>\d{2})'
                   '_(?P<image_id>\d{4})\.jpg')
        m = re.search(pattern, annot_file)
        if m:
            person_id = m.group('person_id')
            camera_id = m.group('camera_id')
            name = '{}_{}'.format(person_id, camera_id)
            return [Annotation(label=name,
                               x_min=0,
                               y_min=0,
                               x_max=pimg.size[0],
                               y_max=pimg.size[1])]
        else:
            return []
