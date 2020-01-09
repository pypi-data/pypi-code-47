from abc import ABCMeta, abstractmethod


class BaseAggregate(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def get_result(self, df):
        raise NotImplementedError()


class MeanAggregate(BaseAggregate):

    def __init__(self):
        pass

    def get_result(self, df):
        return 0, 0


class WeightedMeanAggregate(BaseAggregate):

    def __init__(self):
        pass

    def get_result(self, df):
        return 0, 0


class MedianAggregate(BaseAggregate):

    def __init__(self):
        pass

    def get_result(self, df):
        return 0, 0


class MaxVoteAggregate(BaseAggregate):

    def __init__(self):
        pass

    def get_result(self, df):
        return 0, 0
