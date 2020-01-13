import copy
import operator


class Trajectory:
    def __init__(self, max_timespan):
        self._points = []
        self.max_timespan = max_timespan

    def add(self, point):
        # we control the "size" of the list and its timespan here
        if self.exceed():
            self._points.pop(0)
        self._points.append(point)
        sorted(self._points, key=operator.attrgetter("tagblock_timestamp"))

    def timespan(self):
        if len(self._points) < 1:
            return 0
        start = self._points[0].tagblock_timestamp
        end = self._points[-1].tagblock_timestamp
        return end - start

    def exceed(self):
        return self.timespan() > self.max_timespan