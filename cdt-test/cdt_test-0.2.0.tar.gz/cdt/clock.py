import io
import site
import threading
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

        #     # 返回np.ndarray
        #     feature = cdt_creator.make_cdt_feature(command_clock, copy_clock, hour, minute, buffer)
        #     # xgb = XGB()
        #     # xgb.train('cdt_feature.csv', feature)

        rf_path = site.getsitepackages()[0] + '/cdt/rf.m'
        rf = joblib.load(rf_path)
        # 如果要换模型需要改explanation_creator.py
        # 返回label,支持该分类的解释，不支持该分类的解释 类型为List
        explanation_list = self.explanation_model.explain(rf, feature)
        return explanation_list



