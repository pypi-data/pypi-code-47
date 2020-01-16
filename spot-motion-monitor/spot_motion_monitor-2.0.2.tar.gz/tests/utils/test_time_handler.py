# This file is part of spot_motion_monitor.
#
# Developed for LSST System Integration, Test and Commissioning.
#
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from datetime import datetime

from freezegun import freeze_time
import pytz

from spot_motion_monitor.utils import TimeHandler

class TestTimeHandler():

    def test_parametersAfterConstruction(self):
        th = TimeHandler()
        th.timezone == "UTC"
        assert th.standard_format == "%Y%m%d_%H%M%S"

    @freeze_time("2019-11-26 13:45:23")
    def test_utc_timezone(self):
        th = TimeHandler()
        assert th.getTime() == datetime(2019, 11, 26, 13, 45, 23, tzinfo=pytz.utc)
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_134523"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T13:45:23+00:00"
        assert th.getFormattedTimeStamp(format="iso-fixed") == "2019-11-26T13:45:23"

    @freeze_time("2019-11-26 13:45:23")
    def test_tai_timezone(self):
        th = TimeHandler()
        th.timezone = "TAI"
        assert th.getTime() == datetime(2019, 11, 26, 13, 46, 00, tzinfo=pytz.utc)
        assert th.getTimeStamp() == 1574775960
        assert th.getFormattedTimeStamp() == "20191126_134600"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T13:46:00+00:00"
        assert th.getFormattedTimeStamp(format="iso-fixed") == "2019-11-26T13:46:00"

    @freeze_time("2019-11-26 13:45:23")
    def test_arizona_timezone(self):
        th = TimeHandler()
        th.timezone = "US/Arizona"
        dt = datetime(2019, 11, 26, 13, 45, 23).replace(tzinfo=pytz.utc)
        tz = pytz.timezone(th.timezone)
        dtl = dt.astimezone(tz)
        assert th.getTime() == dtl
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_064523"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T06:45:23-07:00"
        assert th.getFormattedTimeStamp(format="iso-fixed") == "2019-11-26T06:45:23"

    @freeze_time("2019-11-26 13:45:23")
    def test_chile_timezone(self):
        th = TimeHandler()
        th.timezone = "America/Santiago"
        dt = datetime(2019, 11, 26, 13, 45, 23).replace(tzinfo=pytz.utc)
        tz = pytz.timezone(th.timezone)
        dtl = dt.astimezone(tz)
        assert th.getTime() == dtl
        assert th.getTimeStamp() == 1574775923
        assert th.getFormattedTimeStamp() == "20191126_104523"
        assert th.getFormattedTimeStamp(format="iso") == "2019-11-26T10:45:23-03:00"
        assert th.getFormattedTimeStamp(format="iso-fixed") == "2019-11-26T10:45:23"

    def test_timezone_list(self):
        timezones = TimeHandler.getTimezones()
        assert len(timezones) == 593
        assert timezones.count("UTC") == 1
        assert timezones[0] == "UTC"
        assert timezones[1] == "TAI"

    def test_fix_formatting_time(self):
        input_string = "2019-11-26T10:45:23-03:00"
        output_string = "2019-11-26T10:45:23"
        assert TimeHandler.getFixedFormattedTime(input_string) == output_string
        input_string = "2019-11-26T13:46:00+00:00:00.0000"
        output_string = "2019-11-26T13:46:00"
        assert TimeHandler.getFixedFormattedTime(input_string) == output_string
