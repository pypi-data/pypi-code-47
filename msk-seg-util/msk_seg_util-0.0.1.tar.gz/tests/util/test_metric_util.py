import unittest

import numpy as np

from msk_seg_util.util.metric_util import SegMetric
from msk_seg_util.util.metric_util import SegMetricsProcessor


class TestSegMetricsProcessor(unittest.TestCase):
    _MASK = np.asarray(
        [
            [
                [[1, 1], [0, 0]],
                [[0, 1], [0, 0]],
            ],
            [
                [[1, 1], [1, 1]],
                [[1, 1], [1, 1]],
            ],
            [
                [[1, 0], [0, 1]],
                [[1, 0], [0, 0]],
            ],
            [
                [[0, 0], [0, 1]],
                [[0, 0], [0, 0]],
            ]

        ])
    _MASK = np.transpose(_MASK, (1, 2, 3, 0))

    _PREDICTION = np.asarray(
        [
            [
                [[0, 1], [1, 0]],
                [[0, 1], [1, 0]],
            ],
            [
                [[0, 0], [0, 1]],
                [[1, 1], [0, 1]],
            ],
            [
                [[1, 1], [1, 1]],
                [[1, 1], [1, 0]],
            ],
            [
                [[0, 1], [1, 1]],
                [[0, 0], [0, 0]],
            ]

        ])
    _PREDICTION = np.transpose(_PREDICTION, (1, 2, 3, 0))

    _CLASS_NAMES = ('Class-1', 'Class-2', 'Class-3', 'Class-4')
    _VOXEL_SPACING = (1, 1, 1)
    _METRICS = [SegMetric.DSC, SegMetric.VOE, SegMetric.CV, SegMetric.ASSD, SegMetric.PRECISION, SegMetric.RECALL,
                SegMetric.SENSITIVITY, SegMetric.SPECIFICITY, SegMetric.PPV]

    def test_batch_compute_metrics(self):
        manager = SegMetricsProcessor(metrics=self._METRICS, class_names=self._CLASS_NAMES)

        scan_data = []
        for i in range(10):
            scan_data.append(('Scan%d' % i, self._MASK, self._PREDICTION, self._VOXEL_SPACING))

        manager.batch_compute_metrics(scan_data, num_workers=2)

    def test_compute_metrics(self):
        manager = SegMetricsProcessor(metrics=self._METRICS, class_names=self._CLASS_NAMES)
        manager.compute_metrics('Scan1', self._MASK, self._PREDICTION, self._VOXEL_SPACING)
        manager.compute_metrics('Scan2', self._MASK, self._PREDICTION, self._VOXEL_SPACING)


if __name__ == '__main__':
    unittest.main()
