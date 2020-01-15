import copy
import operator

# Minimal duration of a trajectory
MIN_TIMESPAN = 4 * 60 * 60
# Maximal interval between consecutive points
MAX_INTERVAL = 2 * 3600
# Maximal speed accepted (knots)
MAX_SPEED = 30
# bounding box
LAT_MIN_MAX=(-90, 90)
LON_MIN_MAX=(-180, 180)

class MaxIntervalError(Exception):
    pass

class AreaError(Exception):
    pass

class SpeedError(Exception):
    pass

class Track:
    """Iteratively build a track

    Trying to be as close as possible as the one specified
    in MultitaskAIS

    - Thread Safety ?!
    - Where we're going we don't need thread safety !
    https://www.youtube.com/watch?v=G3AfIvJBcGo
    """
    def __init__(self,
                 lat_min_max=LAT_MIN_MAX,
                 lon_min_max=LON_MIN_MAX,
                 min_timespan=MIN_TIMESPAN,
                 max_interval=MAX_INTERVAL,
                 max_speed=MAX_SPEED):
        self._points = []
        self.lat_min, self.lat_max = lat_min_max
        self.lon_min, self.lon_max = lon_min_max
        self.min_timespan = min_timespan
        self.max_interval = max_interval
        self.max_speed = max_speed

    def points(self):
        return self._points

    def add(self, point):
        """Add a point in a trajectory
        1. It needs to be in the region
        2. The interval with the previous point should be less than max_interval
        3. The sog should be less than max_speed

        >>> from sesamelib.sesame_faust import BaseDynamicMessage
        >>> t = Track(lat_min_max=(-10, 10), lon_min_max=(-10, 10))

        >>> msg = BaseDynamicMessage(mmsi="1", x=1, y=11, tagblock_timestamp=0, true_heading=0, sog=1, cog=1)
        >>> t.add(msg)
        Traceback (most recent call last):
        ...
        AreaError: Latitude 11 out of bounds (10, -10)
        >>> len(t._points)
        0

        >>> msg = BaseDynamicMessage(mmsi="1", x=1, y=-11, tagblock_timestamp=0, true_heading=0, sog=1, cog=1)
        >>> t.add(msg)
        Traceback (most recent call last):
        ...
        AreaError: Latitude -11 out of bounds (10, -10)
        >>> len(t._points)
        0

        >>> msg = BaseDynamicMessage(mmsi="1", x=11, y=1, tagblock_timestamp=0, true_heading=0, sog=1, cog=1)
        >>> t.add(msg)
        Traceback (most recent call last):
        ...
        AreaError: Longitude 11 out of bounds (10, -10)

        >>> msg = BaseDynamicMessage(mmsi="1", x=-11, y=1, tagblock_timestamp=0, true_heading=0, sog=1, cog=1)
        >>> t.add(msg)
        Traceback (most recent call last):
        ...
        AreaError: Longitude -11 out of bounds (10, -10)
        >>> len(t._points)
        0

        >>> msg = BaseDynamicMessage(mmsi="1", x=1, y=1, tagblock_timestamp=0, true_heading=0, sog=50, cog=1)
        >>> t.add(msg)
        Traceback (most recent call last):
        ...
        SpeedError: Speed 50 is too fast

        >>> msg = BaseDynamicMessage(mmsi="1", x=1, y=1, tagblock_timestamp=0, true_heading=0, sog=1, cog=1)
        >>> t.add(msg)
        >>> msg = BaseDynamicMessage(mmsi="1", x=1, y=1, tagblock_timestamp=MAX_INTERVAL + 1, true_heading=0, sog=1, cog=1)
        >>> t.add(msg)
        Traceback (most recent call last):
        ...
        MaxIntervalError: The interval 7201 is greater than 7200
        >>> t.length()
        1
        """
        def test(value, pred):
            return value is not None and pred

        lat = point.y
        if test(lat, lat > self.lat_max or lat < self.lat_min):
            # TODO raise
            raise AreaError(f"Latitude {lat} out of bounds {self.lat_max, self.lat_min}")

        lon = point.x
        if test(lon, lon > self.lon_max or lon < self.lon_min):
            raise AreaError(f"Longitude {lon} out of bounds {self.lon_max, self.lon_min}")

        sog = point.sog
        if test(sog, sog > self.max_speed):
            raise SpeedError(f"Speed {sog} is too fast")

        if len(self._points) > 0:
            last = self._points[-1]
            interval = point.tagblock_timestamp - last.tagblock_timestamp
            if interval > self.max_interval:
                raise MaxIntervalError(f"The interval {interval} is greater than {self.max_interval}")

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

    def length(self):
        return len(self._points)

    def exceed(self):
        """
        >>> from sesamelib.sesame_faust import BaseDynamicMessage
        >>> msgs = [BaseDynamicMessage(mmsi="1", x=1, y=1, tagblock_timestamp=i, true_heading=0, sog=1, cog=1)
        ...        for i in range(10)]
        >>> t = Track(min_timespan=5)
        >>> for msg in msgs:
        ...    t.add(msg)
        >>> t.exceed()
        True
        """
        return self.timespan() > self.min_timespan

if __name__ == "__main__":
    import doctest
    doctest.testmod()
