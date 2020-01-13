"""
A Processor takes input images, processes them and yields an output.
"""
from typing import List
import pandas as pd

from .inputter import Inputter
from ..detect import Detector
from ..extract import Extractor
from ..classifier import Classifier
from .outputter import Outputter

__all__ = [
    'Processor'
]


class Processor:
    def __init__(self,
                 inputter: Inputter,
                 extractor: Extractor,
                 outputters: List[Outputter],
                 detector: Detector=None,
                 classifier: Classifier=None):
        """Wrapper around a demo set-up for gender classification.

        :param Inputter inputter: An `Inputter` providing the images
        :param Detector detector: (optional) A `Detector` that detects the
        relevant elements in the image
        :param Extractor extractor: An `Extractor` that yields a descriptor
        for an image or a detection
        :param Classifier classifier: (optional) A `Classifier` that can
        classify descriptors
        :param List[Outputter] outputters: A list of `Outputter`s that, for
        example, will visualize the outputs
        """
        self.inputter = inputter
        self.detector = detector
        self.extractor = extractor
        self.classifier = classifier
        self.outputters = outputters

    def process_next(self):
        inps = next(self.inputter)
        self.process_inputs(inps)

    def process_inputs(self, inputs):
        if self.inputter.has_aois:
            imgs, aois = tuple(zip(*inputs))
        else:
            imgs = inputs
            aois = None

        if self.detector is not None:
            # Detect
            self.detector.imgs = imgs
            self.detector.aois = aois
            df_dets = self.detector.get_detections()
            dets = (df_dets.groupby('image')['detection']
                    .agg(lambda group: group.tolist())
                    .tolist())
        else:
            dets = None

        # Extract
        self.extractor.imgs = imgs
        self.extractor.dets = dets
        self.extractor.include_input = any(o.requires_input
                                           for o in self.outputters)
        self.extractor.include_original = any(o.requires_original
                                              for o in self.outputters)
        df_descrs = self.extractor.get_descriptors().dropna()

        # Classify
        if self.classifier is not None and len(df_descrs) > 0:
            df_clf = self.classifier.classify(df_descrs)
            df = df_descrs.merge(df_clf, left_index=True, right_index=True)
        else:
            df = df_descrs

        # Output
        for outputter in self.outputters:
            if outputter.is_streaming and len(df) == 0:
                df = pd.DataFrame([{'original': img} for img in imgs])
            outputter(df=df)

    def run(self):
        for inps in iter(self.inputter):
            self.process_input(inps)
