# bchhun, {2019-07-24}

from PyQt5.QtCore import QObject, pyqtSlot
from .. import AnalyzeBase

"""

"""


class SampleUserAcquisition(AnalyzeBase):

    def __init__(self):
        super(SampleUserAcquisition, self).__init__()
        self.c = 0

    @AnalyzeBase.emitter
    def update(self):
        print("calling overridden update")
        self.c += 1
        return self.c


class receiver(QObject):

    def __init__(self):
        super(receiver, self).__init__()
        self.ref = 0

    @pyqtSlot(object)
    def rslot(self, value):
        self.ref = 10*value

    def connection(self, signalemitter):
        signalemitter.acquisition_signal.connect(self.rslot)


def test_simple_receiver():
    t = SampleUserAcquisition()
    r = receiver()
    r.connection(t)

    t.update()

    assert(t.c == 1)
    assert(r.ref == 10)


# todo: emitter test: decoration of func with arg, kwarg, no arg
# todo: recever test: decoration of func with arg, kwarg, no arg
# todo: bidi test: ""
# todo: multiple decoration test: same as above but add before/after decorators

class Emitter:

    # ============= decorator emitter / receivers ====================
    @classmethod
    def emitter(cls, channel=0):

        def emitter_wrap(func):
            def emitter_wrap_func(self, *args):
                out = func(self, *args)
                cls.analysis_signals[channel].QChannel.emit(out)
                return out
            emitter_wrap_func.emitter_channel = channel
            return emitter_wrap_func

        return emitter_wrap