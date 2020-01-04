"Simple parser for Garmin TCX files."
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time
from lxml import objectify

namespace = 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'
extension_namespace = 'http://www.garmin.com/xmlschemas/ActivityExtension/v2'

class TCXParser:

    def __init__(self, tcx_file):
        tree = objectify.parse(tcx_file)
        self.root = tree.getroot()
        self.activity = self.root.Activities.Activity
        self._time_stopped = 0

    def hr_values(self):
        return [int(x.text) for x in self.root.xpath('//ns:HeartRateBpm/ns:Value', namespaces={'ns': namespace})]

    def power_values(self):
        result = []
        for x in self.root.xpath('//ns3:TPX/ns3:Watts', namespaces={'ns3': extension_namespace}):
            result.append(int(x.text))
        return result

    def altitude_points(self):
        return [float(x.text) for x in self.root.xpath('//ns:AltitudeMeters', namespaces={'ns': namespace})]

    def position_values(self):
        return [
            (float(pos.LatitudeDegrees.text),
             float(pos.LongitudeDegrees.text))
            for pos in self.root.xpath('//ns:Trackpoint/ns:Position', namespaces={'ns': namespace})]

    def distance_values(self):
        return self.root.findall('.//ns:Trackpoint/ns:DistanceMeters', namespaces={'ns': namespace})

    def time_values(self):
        return [x.text for x in self.root.xpath('//ns:Time', namespaces={'ns': namespace})]

    def cadence_values(self):
        return [int(x.text) for x in self.root.xpath('//ns:Cadence', namespaces={'ns': namespace})]

    def speed_values(self):
        speeds = []
        distance_data = self.distance_values()
        distance_data_size = len(distance_data)
        time_stopped = 0
        for i in range(0, distance_data_size - 1):
            if i == 0:
                speeds.append(0)
            elif i == distance_data_size - 1:
                speeds.append(speeds[i - 1])
            else:
                speed = distance_data[i+1] - distance_data[i]
                if speed <= 0:
                    time_stopped += 1
                    continue
                speeds.append(speed)

        self._time_stopped = time_stopped
        return speeds

    @property
    def latitude(self):
        if hasattr(self.activity.Lap.Track.Trackpoint, 'Position'):
            return self.activity.Lap.Track.Trackpoint.Position.LatitudeDegrees.pyval

    @property
    def longitude(self):
        if hasattr(self.activity.Lap.Track.Trackpoint, 'Position'):
            return self.activity.Lap.Track.Trackpoint.Position.LongitudeDegrees.pyval

    @property
    def activity_type(self):
        return self.activity.attrib['Sport'].lower()

    @property
    def started_at(self):
        return self.activity.Lap[0].attrib["StartTime"]

    @property
    def completed_at(self):
        return self.activity.Lap[-1].Track.Trackpoint[-1].Time.pyval

    @property
    def cadence_avg(self):
        return self.activity.Lap[-1].Cadence

    @property
    def distance(self):
        distance_values = self.distance_values()
        return distance_values[-1] if distance_values else 0

    @property
    def distance_units(self):
        return 'meters'

    @property
    def duration(self):
        """Returns duration of workout in seconds."""
        return sum(lap.TotalTimeSeconds for lap in self.activity.Lap)

    @property
    def calories(self):
        return sum(lap.Calories for lap in self.activity.Lap)

    @property
    def hr_avg(self):
        """Average heart rate of the workout"""
        hr_data = self.hr_values()
        return int(sum(hr_data) / len(hr_data))

    @property
    def power_avg(self):
        """Average power of the workout"""
        power_data = self.power_values()
        return int(sum(power_data) / len(power_data))

    @property
    def avg_speed(self):
        """Average speed of the workout in m/s"""
        speed_data = self.speed_values()
        if len(speed_data) > 0:
            return round(int(sum(speed_data) / len(speed_data)), 1)
        else:
            return 0

    @property
    def time_stopped(self):
        """Time stopped in seconds"""
        if self._time_stopped == 0:
            self.speed_values() # if the speed values function was not called, calls it to force calculation

        return self._time_stopped

    @property
    def moving_time(self):
        """Time moving in seconds"""
        return int(self.duration - self._time_stopped)

    @property
    def hr_max(self):
        """Maximum heart rate of the workout"""
        return max(self.hr_values())

    @property
    def speed_max(self):
        """Maximum speed of the workout in m/s"""
        return round(max(self.speed_values()), 1)

    @property
    def power_max(self):
        """Maximum power of the workout"""
        return max(self.power_values())

    @property
    def hr_min(self):
        """Minimum heart rate of the workout"""
        return min(self.hr_values())

    @property
    def pace(self):
        """Average pace (mm:ss/km for the workout"""
        secs_per_km = self.duration / (self.distance / 1000)
        return time.strftime('%M:%S', time.gmtime(secs_per_km))

    @property
    def altitude_avg(self):
        """Average altitude for the workout"""
        altitude_data = self.altitude_points()
        return sum(altitude_data) / len(altitude_data)

    @property
    def altitude_max(self):
        """Max altitude for the workout"""
        altitude_data = self.altitude_points()
        return max(altitude_data)

    @property
    def altitude_min(self):
        """Min altitude for the workout"""
        altitude_data = self.altitude_points()
        return min(altitude_data)

    @property
    def ascent(self):
        """Returns ascent of workout in meters"""
        total_ascent = 0.0
        altitude_data = self.altitude_points()
        for i in range(len(altitude_data) - 1):
            diff = altitude_data[i+1] - altitude_data[i]
            if diff > 0.0:
                total_ascent += diff
        return total_ascent

    @property
    def descent(self):
        """Returns descent of workout in meters"""
        total_descent = 0.0
        altitude_data = self.altitude_points()
        for i in range(len(altitude_data) - 1):
            diff = altitude_data[i+1] - altitude_data[i]
            if diff < 0.0:
                total_descent += abs(diff)
        return total_descent

    @property
    def cadence_max(self):
        """Returns max cadence of workout"""
        cadence_data = self.cadence_values()
        return max(cadence_data)

    @property
    def activity_notes(self):
        """Return contents of Activity/Notes field if it exists."""
        return getattr(self.activity, 'Notes', '')
