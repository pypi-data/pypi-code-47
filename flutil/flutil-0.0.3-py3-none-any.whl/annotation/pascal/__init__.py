from typing import List
from collections import OrderedDict
from ..parser import Parser
from .. import Annotation
import xmltodict
from xml.parsers.expat import ExpatError
import logging


class PascalParser(Parser):

    @staticmethod
    def _get_annotations(xml: OrderedDict) -> List[Annotation]:
        try:
            if type(xml['annotation']['object']) is list:
                return [Annotation(label=o['name'],
                                   x_min=float(o['bndbox']['xmin']),
                                   y_min=float(o['bndbox']['ymin']),
                                   x_max=float(o['bndbox']['xmax']),
                                   y_max=float(o['bndbox']['ymax']))
                        for o in xml['annotation']['object']]
            else:
                o = xml['annotation']['object']
                return [Annotation(label=o['name'],
                                   x_min=float(o['bndbox']['xmin']),
                                   y_min=float(o['bndbox']['ymin']),
                                   x_max=float(o['bndbox']['xmax']),
                                   y_max=float(o['bndbox']['ymax']))]
        except KeyError as e:
            logging.warning(f'Annotation "{xml}" lacks key: {e}')
            return []

    @classmethod
    def parse_single(cls, annot_file: str):
        with open(annot_file) as annot:
            try:
                xml = xmltodict.parse(annot.read())
                annotations = cls._get_annotations(xml)
            except ExpatError as e:
                logging.warning(e)
                annotations = []

        return annotations

    @staticmethod
    def annots_to_file_contents(annotations: List[Annotation]):
        dict_annot = OrderedDict([('annotation',
                                  OrderedDict([('object',
                                                [{'name': a.label,
                                                  'bndbox': {'xmin':
                                                             a.x_min,
                                                             'ymin':
                                                             a.y_min,
                                                             'xmax':
                                                             a.x_max,
                                                             'ymax':
                                                             a.y_max}
                                                  }
                                                 for a in annotations
                                                 ])]))])
        return xmltodict.unparse(dict_annot, pretty=True)
