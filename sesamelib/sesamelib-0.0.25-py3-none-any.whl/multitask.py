import copy
import operator


class Trajectory:
    def __init__(self, max_timespan):
        self._points = []
        self.max_timespan = max_timespan

    def points(self):
        return self.points

    def add(self, point):
        self._points.append(point)
        sorted(self._points, key=operator.attrgetter("tagblock_timestamp"))

    def timespan(self):
        if len(self._points) < 1:
            return 0
        start = self._points[0].tagblock_timestamp
        end = self._points[-1].tagblock_timestamp
        return end - start

    def reset(self):
        self._points = []

    def exceed(self):
        return self.timespan() > self.max_timespan