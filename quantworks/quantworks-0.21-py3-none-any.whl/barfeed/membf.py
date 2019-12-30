# QuantWorks
# 
# Copyright 2019 Tyler M Kontra
# Copyright 2011-2018 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>, Tyler M Kontra <tyler@tylerkontra.com@gmail.com>
"""

import datetime
import six

from quantworks import barfeed
from quantworks import bar
from quantworks import utils


class BaseMemoryBarFeed(barfeed.BaseBarFeed):
    
    """A non real-time BarFeed responsible for:
    - Holding bars in memory.
    - Aligning them with respect to time.
    Subclasses should:
    - Forward the call to start() if they override it.
    """

    def __init__(self, frequency, maxLen=None):
        super(BaseMemoryBarFeed, self).__init__(frequency, maxLen)

        self.__bars = {}
        self.__nextPos = {}
        self.__started = False
        self.__currDateTime = None

    def reset(self):
        self.__nextPos = {}
        for instrument in self.__bars.keys():
            self.__nextPos.setdefault(instrument, 0)
        self.__currDateTime = None
        super(BaseMemoryBarFeed, self).reset()

    def getCurrentDateTime(self):
        return self.__currDateTime

    def start(self):
        super(BaseMemoryBarFeed, self).start()
        self.__started = True

    def stop(self):
        pass

    def join(self):
        pass

    def addBarsFromSequence(self, instrument, bars):
        if self.__started:
            raise Exception("Can't add more bars once you started consuming bars")

        self.__bars.setdefault(instrument, [])
        self.__nextPos.setdefault(instrument, 0)

        # Add and sort the bars
        self.__bars[instrument].extend(bars)
        self.__bars[instrument].sort(key=lambda b: b.getDateTime())

        self.registerInstrument(instrument)

    def eof(self):
        ret = True
        # Check if there is at least one more bar to return.
        for instrument, bars in six.iteritems(self.__bars):
            nextPos = self.__nextPos[instrument]
            if nextPos < len(bars):
                ret = False
                break
        return ret

    def peekDateTime(self):
        ret = None

        for instrument, bars in six.iteritems(self.__bars):
            nextPos = self.__nextPos[instrument]
            if nextPos < len(bars):
                ret = utils.safe_min(ret, bars[nextPos].getDateTime())
        return ret

    def getNextBars(self):
        # All bars must have the same datetime. We will return all the ones with the smallest datetime.
        smallestDateTime = self.peekDateTime()

        if smallestDateTime is None:
            return None

        # Make a second pass to get all the bars that had the smallest datetime.
        ret = {}
        for instrument, bars in six.iteritems(self.__bars):
            nextPos = self.__nextPos[instrument]
            if nextPos < len(bars) and bars[nextPos].getDateTime() == smallestDateTime:
                ret[instrument] = bars[nextPos]
                self.__nextPos[instrument] += 1

        if self.__currDateTime == smallestDateTime:
            raise Exception("Duplicate bars found for %s on %s" % (list(ret.keys()), smallestDateTime))

        self.__currDateTime = smallestDateTime
        return bar.Bars(ret)

    def loadAll(self):
        for dateTime, bars in self:
            pass


class SimpleBarFeed(BaseMemoryBarFeed):
    """Base class for Iterable[Bar] based :class:`quantworks.barfeed.BarFeed`.

    .. note::
        This is a base class and should not be used directly.
    """

    def __init__(self, frequency, maxLen=None):
        super(SimpleBarFeed, self).__init__(frequency, maxLen)

        self.__barFilter = None
        self.__dailyTime = datetime.time(0, 0, 0)

    def getDailyBarTime(self):
        return self.__dailyTime

    def setDailyBarTime(self, time):
        self.__dailyTime = time

    def getBarFilter(self):
        return self.__barFilter

    def setBarFilter(self, barFilter):
        self.__barFilter = barFilter

    def _addBars(self, instrument, loadedBars):
        loadedBars = filter(
            lambda bar_: (bar_ is not None) and
                (self.__barFilter is None or self.__barFilter.includeBar(bar_)),
            loadedBars
        )
        self.addBarsFromSequence(instrument, loadedBars)

