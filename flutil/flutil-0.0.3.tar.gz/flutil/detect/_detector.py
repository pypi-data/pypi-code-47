from typing import Union, Iterable, List
from pathlib import Path
import numpy as np
import pandas as pd
from PIL.Image import Image
from tqdm import tqdm
from ._detection import Detection
from ..extract import Extractor


class Detector(Extractor):
    def __init__(self, imgs: Iterable[Union[str, Path, Image, np.ndarray]],
                 bs: int = 1, **kwargs):
        """
        :param Iterable[Union[str, Path, Image, np.ndarray]] imgs: the image
        paths
        :param int bs: the batch size
        :param kwargs: kwargs to pass to Extractor
        """
        super().__init__(imgs=imgs, bs=bs, **kwargs)

    def _desc2dets(self, desc: np.ndarray) -> List[Detection]:
        """Return the `Detection`s that correspond with the given descriptor.

        :param np.ndarray desc: the descriptor
        :rtype: List[Detection]
        :returns: the `Detection`s that correspond with the given descriptor
        """
        raise NotImplementedError

    def __iter__(self):
        for row in super()._raw_iter():
            # A descriptor corresponds to zero or more detections
            dets = self._desc2dets(row['descriptor'])

            if 'detection' in row.index:
                # Put the detection into the correct coordinate frame
                dets = [det + row['detection'].tl for det in dets]

            row = self.clean_row(row)
            row.drop(labels='descriptor', inplace=True)

            row['detection'] = dets
            yield row

    def get_detections(self) -> pd.DataFrame:
        rows = [*tqdm(self, total=len(self))]

        new_rows = []
        for row in rows:
            if len(row['detection']) == 0:
                new_row = row
                new_row['detection'] = None
                new_rows.append(new_row.to_dict())
                continue

            new_row = {k: v for k, v in row.items()
                       if k != 'detection'}

            for det in row['detection']:
                new_rows.append({**new_row, 'detection': det})

        return pd.DataFrame(new_rows).reset_index(drop=True)
