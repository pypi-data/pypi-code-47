"""Utilities for tracking metrics."""

from enum import Enum

import numpy as np
import scipy.stats as spstats
import pandas as pd

import multiprocessing as mp

from medpy.metric import dc, assd, recall, precision, sensitivity, specificity, positive_predictive_value

from typing import Iterable, Sequence, Union


def _cv(y_pred: np.ndarray, y_true: np.ndarray):
    """Calculate coefficient of variation.

    Args:
        y_true (np.ndarray): Binary ground truth mask.
        y_pred (np.ndarray): Predicted ground truth mask.

    Returns:
        float: Coefficient of variation.
    """
    y_true = np.squeeze(y_true)
    y_pred = np.squeeze(y_pred)

    cv = np.std([np.sum(y_true), np.sum(y_pred)]) / np.mean([np.sum(y_true), np.sum(y_pred)])
    return cv


def _volumetric_overlap_error(y_pred: np.ndarray, y_true: np.ndarray):
    """Volumetric overlap error.

    Args:
        y_true (np.ndarray): Binary ground truth mask.
        y_pred (np.ndarray): Predicted ground truth mask.

    Returns:
        float: Volumetric overlap error.
    """

    y_true = y_true.flatten()
    y_pred = y_pred.flatten()

    y_true_bool = np.asarray(y_true, dtype=np.bool)
    y_pred_bool = np.asarray(y_pred, dtype=np.bool)
    TP = np.sum(y_true_bool * y_pred_bool, axis=-1)
    FP = np.sum(~y_true_bool * y_pred_bool, axis=-1)
    FN = np.sum(y_true_bool * ~y_pred_bool, axis=-1)

    mu = 1e-07

    voe = 1 - (TP + mu) / (TP + FP + FN + mu)

    return voe


class MetricOperation(Enum):
    """Operation to calculate group statistics.

    To evaluate the overall performance on a group, results for each member of the group is averaged.
    However, in many cases, this may not be the best option.

    The following operations are supported:

        1. MEAN
        2. MEDIAN
        3. RMS: Root mean square.
    """
    MEAN = 1, lambda x, **kwargs: np.mean(x, **kwargs)
    MEDIAN = 2, lambda x, **kwargs: np.median(x, **kwargs)
    RMS = 3, lambda x, **kwargs: np.sqrt(np.mean(x ** 2, **kwargs))

    def __new__(cls, keycode, func):
        obj = object.__new__(cls)
        obj._value_ = keycode
        obj.func = func
        return obj

    def compute(self, x: np.ndarray, **kwargs):
        """Compute operation.

        Args:
            x (np.ndarray): Array-like over which to compute operation.
            **kwargs: Keywords for numpy implementation of mean/median.
        """
        return self.func(x, **kwargs)


def __sem__(x, **kwargs):
    """Calculate standard error of the mean."""
    args = {'axis': 0, 'ddof': 0}
    args.update(**kwargs)

    return spstats.sem(x, **args)


class MetricError(Enum):
    """Error metrics.

        1. STANDARD_DEVIATION
        2. STANDARD_ERROR: Standard error of the mean.
    """
    STANDARD_DEVIATION = 1, lambda x, **kwargs: np.std(x, **kwargs)
    STANDARD_ERROR = 2, lambda x, **kwargs: __sem__(x, **kwargs)

    def __new__(cls, keycode, func):
        obj = object.__new__(cls)
        obj._value_ = keycode
        obj.func = func
        return obj

    def compute(self, x: np.ndarray, **kwargs):
        return self.func(x, **kwargs)


class SegMetric(Enum):
    """Standard metrics used to judge segmentation quality.

    Following metrics are supported:

        1. `DSC`: Dice score coefficient.
        2. `VOE`: Volumetric overlap error.
        3. `CV`: Coefficient of variation.
        4. `ASSD`: Average Symmetric Surface Distance
        5. `Precision`
        6. `Recall`
        7. `SENSITIVITY`
        8. `SPECIFICITY`
        9. `PPV`: Positive Predictive Value

    Note `ASSD` takes long time to compute.
    """
    DSC = 1, 'Dice Score Coefficient', dc, False
    VOE = 2, 'Volumetric Overlap Error', _volumetric_overlap_error, False
    CV = 3, 'Coefficient of Variation', _cv, False
    ASSD = 4, 'Average Symmetric Surface Distance', assd, True
    PRECISION = 5, 'Precision', precision, False
    RECALL = 6, 'Recall', recall, False
    SENSITIVITY = 7, 'Sensitivity', sensitivity, False
    SPECIFICITY = 8, 'Specificity', specificity, False
    PPV = 9, "Positive Predictive Value", positive_predictive_value, False

    def __new__(cls, key_code, full_name, func, use_voxel_spacing=False):
        obj = object.__new__(cls)
        obj._value_ = key_code
        obj.full_name = full_name
        obj.func = func
        obj.use_voxel_spacing = use_voxel_spacing
        return obj

    def compute(self, y_true, y_pred, voxel_spacing):
        """Compute metric for a single segmentation.

        Args:
            y_true (np.ndarray): Binary ground truth mask.
            y_pred (np.ndarray): Predicted ground truth mask.
            voxel_spacing (tuple[float]): Voxel dimensions (in mm).

        Returns:
            The computed metric.
        """
        if self.use_voxel_spacing:
            return self.func(y_pred, y_true, voxel_spacing)
        else:
            return self.func(y_pred, y_true)


class SegMetricsProcessor(object):
    """This class processes, handles, and stores common segmentation metrics.

    Args:
        metrics (Sequence[SegMetric]): Metrics to analyze.
        class_names (Sequence[str]): Names of different classes to segment, in order of input channels.
        metric_computations (Sequence[MetricOperation], optional): Operations to perform on all metrics.
            Defaults to :obj:`(MetricOperation.MEAN, MetricOperation.RMS, MetricOperation.MEDIAN,
            MetricError.STANDARD_DEVIATION)`.
        error_metric (MetricError): Defaults to :obj:`MetricError.STANDARD_DEVIATION`.
    """

    # Default is to capitalize all metric names. If another name is, please specify here.
    __METRICS_DISPLAY_NAMES = {SegMetric.DSC: SegMetric.DSC.name,
                               SegMetric.VOE: SegMetric.VOE.name,
                               SegMetric.CV: SegMetric.CV.name,
                               SegMetric.ASSD: 'ASSD (mm)',
                               SegMetric.PRECISION: 'Precision',
                               SegMetric.RECALL: 'Recall',
                               SegMetric.SENSITIVITY: 'Sensitivity',
                               SegMetric.SPECIFICITY: 'Specificity',
                               SegMetric.PPV: SegMetric.PPV.name}

    # Default is to calculate mean for every metric expect coefficient of variation (CV),
    # which uses root-mean-squared (RMS).
    __DEFAULT_METRIC_COMPUTATIONS = (MetricOperation.MEAN,
                                     MetricOperation.RMS,
                                     MetricOperation.MEDIAN,
                                     MetricError.STANDARD_DEVIATION,
                                     )

    def __init__(self, metrics: Sequence[SegMetric], class_names: Sequence[str],
                 metric_computations: Sequence[MetricOperation] = __DEFAULT_METRIC_COMPUTATIONS,
                 error_metric: MetricError = MetricError.STANDARD_DEVIATION):
        self.metrics = metrics
        self.__metric_names = [self.__METRICS_DISPLAY_NAMES[m] for m in self.metrics]

        self.class_names = class_names

        self.__scan_ids = []
        self.__scan_seg_data = dict()
        self.__data = dict()
        self.__is_data_stale = False

        # Default computations to perform on each metric.
        self.metric_computations = metric_computations
        self.error_metric = error_metric

        self.__dataframe = None

    def _compute_metrics(self, y_true: np.ndarray, y_pred: np.ndarray, voxel_spacing: tuple):
        """Internal helper for computing metrics.

        Args:
            y_true (np.ndarray): Binary ground truth mask.
            y_pred (np.ndarray): Predicted ground truth mask.
            voxel_spacing (tuple[float]): Voxel dimensions (in mm).

        Returns:
            pd.DataFrame: A DataFrame indexed by class names (rows) and spanned by metrics (columns).

            TODO: Draw table
        """
        assert type(y_true) is np.ndarray and type(y_pred) is np.ndarray, "y_true and y_pred must be numpy arrays"
        assert y_true.shape == y_pred.shape, "Shape mismatch: y_true and y_pred must have the same shape"
        assert y_true.ndim == 3 or y_true.ndim == 4, "Arrays must be (Y,X,Z) or (Y, X, Z, #classes)"

        if y_true.ndim == 3:
            y_true = y_true[..., np.newaxis]
            y_pred = y_pred[..., np.newaxis]

        assert y_true.shape[-1] == len(self.class_names), "Expected %d classes. Got %d" % (len(self.class_names),
                                                                                           y_true.shape[-1])
        num_classes = len(self.class_names)

        metrics_data = []
        for m in self.metrics:
            metrics_data.append([m.compute(y_true[..., c], y_pred[..., c], voxel_spacing) for c in range(num_classes)])

        return pd.DataFrame(metrics_data, index=self.__metric_names, columns=self.class_names)

    def _to_dataframe(self, scan_ids):
        """Internal helper to convert metric data into dataframe.

        Format:

              ID |                 Scan1 | Scan2 | Scan3 | Scan4 | Scan5 | ...
            ------------------------------------------------------------------
            Metric     Class
            ------------------------------------------------------------------
            Metric1    Class1
            Metric1    Class2
               .        .
               .        .
               .        .
            Metric2    Class1
            Metric2    Class2
               .        .
               .        .
               .        .

        Args:
            scan_ids: Scan ids to organize in dataframe.

        Returns:
            pd.DataFrame: A pandas Dataframe.
        """
        scan_data = []

        for scan_id in scan_ids:
            df = self.__scan_seg_data[scan_id]
            df.insert(0, 'ID', [scan_id] * len(df))
            scan_data.append(df)

        df = pd.concat(scan_data)
        df.insert(1, 'Metric', df.index)
        df = pd.melt(df, id_vars=['ID', 'Metric'], var_name='Class')
        df = df.reset_index(drop=True)
        df = df.pivot_table(index=['Metric', 'Class'], columns='ID')
        df.columns = df.columns.droplevel(0)

        return df

    def _unroll_compute_metrics(self, data_args):
        """Wrapper for computing metrics.

        Args:
            data_args (tuple): Tuple of (:obj:`scan_id`, :obj:`y_true`, :obj:`y_pred`, :obj:`voxel_spacing`).
        """
        return self._compute_metrics(data_args[1], data_args[2], data_args[3])

    def batch_compute_metrics(self, data: Iterable, num_workers: int=0):
        """Compute segmentation metrics for volume in batch using multiprocessing library.

        Args:
            data (:obj:`Iterable[tuple]`): An iterable of tuples of ``(scan_id, y_true, y_pred, voxel_spacing)``
            num_workers (:obj:`int`, optional): Number of workers to use. Defaults to `0`, meaning processes will be run
                on main thread with single worker.
        """
        scan_ids = [d[0] for d in data]
        overlapping_scan_ids = set(self.__scan_ids).intersection(set(scan_ids))
        if len(overlapping_scan_ids) != 0:
            raise ValueError('Scan id(s) %s exist.' % overlapping_scan_ids)

        with mp.Pool(num_workers) as p:
            results = p.map(self._unroll_compute_metrics, data)

        for ind, result in enumerate(results):
            scan_id = scan_ids[ind]
            self.__scan_ids.append(scan_id)
            self.__scan_seg_data[scan_id] = result

    def compute_metrics(self, scan_id: Union[str, int], y_true: np.ndarray, y_pred: np.ndarray, voxel_spacing: tuple):
        """Compute segmentation metrics for volume.

        Args:
            scan_id (:obj:`Union[str, int]`): The scan id.
            y_true (:obj:`np.ndarray`): 3D or 4D ground truth binary mask of shape ``(Y, X, Z, [# Classes])``.
            y_pred (np.ndarray): 3D or 4D prediction binary mask of shape ``(Y, X, Z, [# Classes])``.
            voxel_spacing (tuple[float]): Voxel dimensions (in mm).

        Returns:
            str: Summary of scan metrics.

        Raises:
            ValueError: If ``scan_id`` exists.
        """
        if scan_id in self.__scan_ids:
            raise ValueError('Scan id already exists, use different id')

        metrics_data = self._compute_metrics(y_true, y_pred, voxel_spacing)

        self.__scan_ids.append(scan_id)
        self.__scan_seg_data[scan_id] = metrics_data
        self.__is_data_stale = True

        return self.scan_summary(scan_id)

    def scan_summary(self, scan_id: Union[str, int], sep: str= ','):
        """Provide summary of segmentation metrics for a specific sample.

        Metrics are summarized by averaging metrics across all classes. To get the raw matrix, use
        :obj:`self.scan_data(id)`.

        Args:
            scan_id (Union[str, int]): The scan id.
            sep (str): Delimiter between entries. Defaults to ``''``.

        Returns:
            str: Performance summary for scan.
        """
        scan_data = self.__scan_seg_data[scan_id]
        avg_data = scan_data.mean(axis=1)

        metrics = avg_data.index.tolist()

        basic_format = '%s: %0.3f' + ('%s ' % sep)
        summary_str_format = basic_format * len(metrics)
        summary_str_format = summary_str_format[:-2]

        data = []
        for name in avg_data.index.tolist():
            data.extend([name, avg_data[name]])

        return summary_str_format % (tuple(data))

    def summary(self):
        computation_result = []
        df = self.dataframe
        for m_computation in self.metric_computations:
            cr = m_computation.compute(df, axis=1)
            if not isinstance(cr, pd.DataFrame):
                cr = pd.DataFrame(cr, index=df.index)
            cr.columns = [m_computation.name]
            computation_result.append(cr)

        return pd.concat(computation_result, axis=1)

    def scan_data(self, scan_id: Union[str, int]) -> pd.DataFrame:
        """Get performance table for a scan.

        Args:
             scan_id (Union[str, int]): The scan id.

        Returns:
            pd.DataFrame: Performance table for scan.
        """
        return self.__scan_seg_data[scan_id]

    @property
    def dataframe(self):
        """pd.DataFrame: Metrics as DataFrame.

        The dataframe is indexed first by the metric, then by the class. The columns correspond to the different
        samples.

        Format:

              ID                  Scan1   Scan2   Scan3   Scan4   Scan5   ...
            Metric     Class
            ------------------------------------------------------------------
            Metric1    Class1
            Metric1    Class2
               .        .
               .        .
               .        .
            Metric2    Class1
            Metric2    Class2
               .        .
               .        .
               .        .
        """
        if self.__dataframe is None or self.__is_data_stale:
            self.__dataframe = self._to_dataframe(self.__scan_ids)
            self.__is_data_stale = False

        return self.__dataframe
