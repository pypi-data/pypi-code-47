from abc import abstractmethod, ABCMeta


class BaseFillna(metaclass=ABCMeta):

    def __init__(self, threshold):
        self.nan_threshold = threshold

    @abstractmethod
    def fillna(self, df):
        raise NotImplementedError()


class MeanFillna(BaseFillna):

    def fillna(self, df):
        columns = df.columns


class MedianFillna(BaseFillna):

    def fillna(self, df):
        columns = df.columns


class KneignborFillna(BaseFillna):

    def fillna(self, df):
        columns = df.columns
