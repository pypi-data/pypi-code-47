import timeit

from dask import dataframe as dd

from tqdm.auto import tqdm
from tqdm_dask_progressbar import TQDMDaskProgressBar

from swifter import _SwifterObject, suppress_stdout_stderr

SAMPLE_SIZE = 1000
N_REPEATS = 3


class Transformation(_SwifterObject):
    def __init__(
        self,
        obj,
        npartitions=None,
        dask_threshold=1,
        scheduler="processes",
        progress_bar=True,
        progress_bar_desc=None,
        allow_dask_on_strings=False,
    ):
        super().__init__(
            obj, npartitions, dask_threshold, scheduler, progress_bar, progress_bar_desc, allow_dask_on_strings
        )
        self._sample_pd = obj.iloc[: self._SAMPLE_SIZE]
        self._obj_pd = obj
        self._obj_dd = dd.from_pandas(obj, npartitions=npartitions)
        self._nrows = obj.shape[0]

    def _wrapped_apply(self, func, *args, **kwds):
        def wrapped():
            with suppress_stdout_stderr():
                self._sample_pd.apply(func, *args, **kwds)

        return wrapped

    def _dask_apply(self, func, *args, **kwds):
        if self._progress_bar:
            with TQDMDaskProgressBar(desc=self._progress_bar_desc or "Dask Apply"):
                return self._obj_dd.apply(func, *args, **kwds).compute(scheduler=self._scheduler)
        else:
            return self._obj_dd.apply(func, *args, **kwds).compute(scheduler=self._scheduler)

    def apply(self, func, *args, **kwds):
        """
        Apply the function to the transformed swifter object
        """
        # estimate time to pandas apply
        wrapped = self._wrapped_apply(func, *args, **kwds)
        timed = timeit.timeit(wrapped, number=N_REPEATS)
        sample_proc_est = timed / N_REPEATS
        est_apply_duration = sample_proc_est / self._SAMPLE_SIZE * self._nrows

        # No `allow_dask_processing` variable here, because we don't know the dtypes of the resampler object
        if est_apply_duration > self._dask_threshold:
            return self._dask_apply(func, *args, **kwds)
        else:  # use pandas
            if self._progress_bar:
                tqdm.pandas(desc=self._progress_bar_desc or "Pandas Apply")
                return self._obj_pd.progress_apply(func, *args, **kwds)
            else:
                return self._obj_pd.apply(func, *args, **kwds)


class Rolling(Transformation):
    def __init__(
        self,
        obj,
        npartitions=None,
        dask_threshold=1,
        scheduler="processes",
        progress_bar=True,
        progress_bar_desc=None,
        allow_dask_on_strings=False,
        **kwds
    ):
        super(Rolling, self).__init__(
            obj, npartitions, dask_threshold, scheduler, progress_bar, progress_bar_desc, allow_dask_on_strings
        )
        self._rolling_kwds = kwds.copy()
        self._sample_original = self._sample_pd.copy()
        self._sample_pd = self._sample_pd.rolling(**kwds)
        self._obj_pd = self._obj_pd.rolling(**kwds)
        self._obj_dd = self._obj_dd.rolling(**{k: v for k, v in kwds.items() if k not in ["on", "closed"]})

    def _dask_apply(self, func, *args, **kwds):
        try:
            # check that the dask rolling apply matches the pandas apply
            with suppress_stdout_stderr():
                tmp_df = (
                    dd.from_pandas(self._sample_original, npartitions=self._npartitions)
                    .rolling(**{k: v for k, v in self._rolling_kwds.items() if k not in ["on", "closed"]})
                    .apply(func, *args, **kwds)
                    .compute(scheduler=self._scheduler)
                )
            self._validate_apply(
                tmp_df.equals(self._sample_pd.apply(func, *args, **kwds)),
                error_message="Dask rolling apply sample does not match pandas rolling apply sample.",
            )
            if self._progress_bar:
                with TQDMDaskProgressBar(desc=self._progress_bar_desc or "Dask Apply"):
                    return self._obj_dd.apply(func, *args, **kwds).compute(scheduler=self._scheduler)
            else:
                return self._obj_dd.apply(func, *args, **kwds).compute(scheduler=self._scheduler)
        except (AttributeError, ValueError, TypeError, KeyError):
            if self._progress_bar:
                tqdm.pandas(desc=self._progress_bar_desc or "Pandas Apply")
                return self._obj_pd.progress_apply(func, *args, **kwds)
            else:
                return self._obj_pd.apply(func, *args, **kwds)


class Resampler(Transformation):
    def __init__(
        self,
        obj,
        npartitions=None,
        dask_threshold=1,
        scheduler="processes",
        progress_bar=True,
        progress_bar_desc=None,
        allow_dask_on_strings=False,
        **kwds
    ):
        super(Resampler, self).__init__(
            obj, npartitions, dask_threshold, scheduler, progress_bar, progress_bar_desc, allow_dask_on_strings
        )
        self._resampler_kwds = kwds.copy()
        self._sample_original = self._sample_pd.copy()
        self._sample_pd = self._sample_pd.resample(**kwds)
        self._obj_pd = self._obj_pd.resample(**kwds)
        self._obj_dd = self._obj_dd.resample(**{k: v for k, v in kwds.items() if k in ["rule", "closed", "label"]})

    def _wrapped_apply(self, func, *args, **kwds):
        def wrapped():
            with suppress_stdout_stderr():
                self._sample_pd.apply(func, *args, **kwds)

        return wrapped

    def _dask_apply(self, func, *args, **kwds):
        try:
            # check that the dask resampler apply matches the pandas apply
            with suppress_stdout_stderr():
                tmp_df = (
                    dd.from_pandas(self._sample_original, npartitions=self._npartitions)
                    .resample(**{k: v for k, v in self._resampler_kwds.items() if k in ["rule", "closed", "label"]})
                    .agg(func, *args, **kwds)
                    .compute(scheduler=self._scheduler)
                )
            self._validate_apply(
                tmp_df.equals(self._sample_pd.apply(func, *args, **kwds)),
                error_message="Dask resampler apply sample does not match pandas resampler apply sample.",
            )

            if self._progress_bar:
                with TQDMDaskProgressBar(desc=self._progress_bar_desc or "Dask Apply"):
                    return self._obj_dd.agg(func, *args, **kwds).compute(scheduler=self._scheduler)
            else:
                return self._obj_dd.agg(func, *args, **kwds).compute(scheduler=self._scheduler)
        except (AttributeError, ValueError, TypeError, KeyError):
            # use pandas -- no progress_apply available for resampler objects
            return self._obj_pd.apply(func, *args, **kwds)

    def apply(self, func, *args, **kwds):
        """
        Apply the function to the resampler swifter object
        """
        # estimate time to pandas apply
        wrapped = self._wrapped_apply(func, *args, **kwds)
        timed = timeit.timeit(wrapped, number=N_REPEATS)
        sample_proc_est = timed / N_REPEATS
        est_apply_duration = sample_proc_est / self._SAMPLE_SIZE * self._nrows

        # No `allow_dask_processing` variable here, because we don't know the dtypes of the resampler object
        if est_apply_duration > self._dask_threshold:
            return self._dask_apply(func, *args, **kwds)
        else:  # use pandas -- no progress_apply available for resampler objects
            return self._obj_pd.apply(func, *args, **kwds)