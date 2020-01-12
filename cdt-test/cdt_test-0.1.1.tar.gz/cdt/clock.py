# import cdt_feature_creator
# from explanation_creator import Explanation
# import numpy as np
# import io
# import threading
# from sklearn.externals import joblib


# def test():
#     cdt_creator = cdt_feature_creator.CdtModel()
#     explanation_creator = Explanation()
#
#     # *_clock 都为np.ndarray ,hour,minute为要求的时间，buffer为缓冲
#     command_clock = np.loadtxt(open("20991568653277626_1.csv", "rb"), delimiter=",", skiprows=0)
#     copy_clock = np.loadtxt(open("20991568653277626_2.csv", "rb"), delimiter=",", skiprows=0)
#
#     # 将 list 转为 numpy.ndarray
#     # command_clock = np.array(command_clock)
#     # copy_clock = np.array(copy_clock)
#
#     hour = 3
#     minute = 25
#     buffer = io.BytesIO()
#
#     # 返回np.ndarray
#     feature = cdt_creator.make_cdt_feature(command_clock, copy_clock, hour, minute, buffer)
#     # xgb = XGB()
#     # xgb.train('cdt_feature.csv', feature)
#
#     rf = joblib.load('rf.m')
#     # 如果要换模型需要改explanation_creator.py
#     # 返回label,支持该分类的解释，不支持该分类的解释 类型为List
#     print(explanation_creator.explain(rf, feature))
#
#
# test()

# class CDT(object):
#     def __init__(self):
#         pass

import io
import threading
import numpy as np
from sklearn.externals import joblib

from cdt.cdt_feature_creator import CdtModel
from cdt.explanation_creator import Explanation


class Clock(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Clock, "_instance"):
            with Clock._instance_lock:
                if not hasattr(Clock, "_instance"):
                    Clock._instance = object.__new__(cls)
        return Clock._instance

    model = CdtModel()
    explanation_model = Explanation()

    def detect(self, command_clock, copy_clock, hour, minute):
        # *_clock 都为np.ndarray ,hour,minute为要求的时间，buffer为缓冲
        # command_clock = np.loadtxt(open("excel.csv", "rb"), delimiter=",", skiprows=0)
        # copy_clock = np.loadtxt(open("excel2.csv", "rb"), delimiter=",", skiprows=0)
        # hour = 5
        # minute = 40
        buffer = io.BytesIO()

        # 返回np.ndarray
        feature = self.model.make_cdt_feature(command_clock, copy_clock, hour, minute, buffer)

        rf = joblib.load('cdt/rf.m')
        # 如果要换模型需要改explanation_creator.py
        # 返回label,支持该分类的解释，不支持该分类的解释 类型为List
        explanation_list = self.explanation_model.explain(rf, feature)
        return explanation_list


# command_clock = np.loadtxt(open("20991568653277626_1.csv", "rb"), delimiter=",", skiprows=0)
# copy_clock = np.loadtxt(open("20991568653277626_2.csv", "rb"), delimiter=",", skiprows=0)
# clock = Clock()
# print(clock.detect(command_clock, copy_clock, 5, 40))


