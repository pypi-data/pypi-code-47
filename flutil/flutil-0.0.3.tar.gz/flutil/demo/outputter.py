"""
An Outputter handles the processing results, e.g. visualization or logging.
"""
from pathlib import Path
import pandas as pd

__all__ = [
    'Outputter',
    'LogOutputter',
    'DataFrameOutputter'
]


class Outputter:
    """
    Handles the processing results, e.g. for visualization or logging.
    """
    def __init__(self, requires_original=False, requires_input=False,
                 is_streaming=False):
        """
        :param requires_original: whether the Outputter needs the original
        image as a PIL Image. Default: `False`.
        :param requires_input: whether the Outputter needs the input
        image from which the descriptor was extracted. Default: `False`.
        :param is_streaming: if `True`, the Outputter requires a continuous
        stream of images, e.g. for showing continuous video. Default: `False`.
        """
        self.requires_original = requires_original
        self.requires_input = requires_input
        self.is_streaming = is_streaming

    def __call__(self, df: pd.DataFrame):
        """
        :param pd.DataFrame df: DataFrame containing the result. It should have
        columns:

        - `image`: the `PIL.Image` from which the descriptor was extracted
        - `descriptor`: the extracted descriptor

        Optionally, it can also contain the columns:

        - `detection`: the region in the image from which the descriptor was
        extracted
        - `label`: the label obtained from classifying the descriptor
        - `AOI`: the area of interest used for detection or descriptor
        extraction. Other regions on the image where ignored.
        """
        raise NotImplementedError


class LogOutputter(Outputter):
    def __init__(self, out_csv: Path):
        super().__init__()
        self.out_csv = out_csv

    def __call__(self, df):
        if not self.out_csv.parent.exists():
            self.out_csv.parent.mkdir(parents=True)

        mode = 'a' if self.out_csv.exists() else 'w'
        with self.out_csv.open(mode) as f:
            (df.drop(labels=['nd_img'])
             .to_frame()
             .transpose()
             .to_csv(f, header=(mode == 'w'), index=False))


class DataFrameOutputter(Outputter):
    def __init__(self, requires_original=True, requires_input=True,
                 concat_dfs=True):
        """
        :param bool requires_input: if True, the input will be kept as a
        PIL.Image in the DataFrame in the column 'input'
        :param bool requires_original: if True, the original image will be kept
        as a PIL.Image in the DataFrame in the column 'original'
        :param bool concat_dfs: concatenate newly incoming `DataFrame`s to the
        previous `DataFrame`.
        """
        super().__init__(requires_original=requires_original,
                         requires_input=requires_input)
        self.df = None
        self.concat_dfs = concat_dfs

    def __call__(self, df: pd.DataFrame):
        if self.df is None or not self.concat_dfs:
            self.df = df
        else:
            self.df = pd.concat([self.df, df], ignore_index=True)
