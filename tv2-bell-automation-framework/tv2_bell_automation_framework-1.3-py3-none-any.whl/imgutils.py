import os

import numpy as np

class Frame(np.ndarray):
    '''
    A frame of video
    '''
    def __new__(cls, array, dtype=None, order=None, time=None, _draw_sink=None):
        obj = np.asarray(array, dtype=dtype, order=order).view(cls)
        obj.time = time
        obj._draw_sink = _draw_sink
        return obj
    
    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.time = getattr(obj, 'time', None)
        self._draw_sink = getattr(obj, '_draw_sink', None)

    def __repr__(self):
        if len(self.shape) == 3:
            dimensions = "%dx%dx%d" % (
                self.shape[1], self.shape[0], self.shape[2]
            )
        else:
            dimensions = "%dx%d" % (self.shape[1], self.shape[0])
        return "<tv2test.Frame(time=%s, dimensions=%s)>" % (
            "None" if self.time is None else "%.3f" % self.time,
            dimensions
        )
