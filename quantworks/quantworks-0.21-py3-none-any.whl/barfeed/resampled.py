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


from quantworks import barfeed
from quantworks.dataseries import resampled
from quantworks import resamplebase
from quantworks import bar


class BarsGrouper(resamplebase.Grouper):
    def __init__(self, groupDateTime, bars, frequency):
        resamplebase.Grouper.__init__(self, groupDateTime)
        self.__barGroupers = {}
        self.__frequency = frequency

        # Initialize BarGrouper instances for each instrument.
        for instrument, bar_ in bars.items():
            barGrouper = resampled.BarGrouper(groupDateTime, bar_, frequency)
            self.__barGroupers[instrument] = barGrouper

    def addValue(self, value):
        # Update or initialize BarGrouper instances for each instrument.
        for instrument, bar_ in value.items():
            barGrouper = self.__barGroupers.get(instrument)
            if barGrouper:
                barGrouper.addValue(bar_)
            else:
                barGrouper = resampled.BarGrouper(self.getDateTime(), bar_, self.__frequency)
                self.__barGroupers[instrument] = barGrouper

    def getGrouped(self):
        bar_dict = {}
        for instrument, grouper in self.__barGroupers.items():
            bar_dict[instrument] = grouper.getGrouped()
        return bar.Bars(bar_dict)


class ResampledBarFeed(barfeed.BaseBarFeed):

    def __init__(self, barFeed, frequency, maxLen=None):
        super(ResampledBarFeed, self).__init__(frequency, maxLen)

        if not isinstance(barFeed, barfeed.BaseBarFeed):
            raise Exception("barFeed must be a barfeed.BaseBarFeed instance")

        if not resamplebase.is_valid_frequency(frequency):
            raise Exception("Unsupported frequency")

        # Register the same instruments as in the underlying barfeed.
        for instrument in barFeed.getRegisteredInstruments():
            self.registerInstrument(instrument)

        self.__values = []
        self.__barFeed = barFeed
        self.__grouper = None
        self.__range = None

        barFeed.getNewValuesEvent().subscribe(self.__onNewValues)

    def __onNewValues(self, dateTime, value):
        if self.__range is None:
            self.__range = resamplebase.build_range(dateTime, self.getFrequency())
            self.__grouper = BarsGrouper(self.__range.getBeginning(), value, self.getFrequency())
        elif self.__range.belongs(dateTime):
            self.__grouper.addValue(value)
        else:
            self.__values.append(self.__grouper.getGrouped())
            self.__range = resamplebase.build_range(dateTime, self.getFrequency())
            self.__grouper = BarsGrouper(self.__range.getBeginning(), value, self.getFrequency())

    def getCurrentDateTime(self):
        return self.__barFeed.getCurrentDateTime()

    def barsHaveAdjClose(self):
        return self.__barFeed.barsHaveAdjClose()

    def getNextBars(self):
        ret = None
        if len(self.__values):
            ret = self.__values.pop(0)
        return ret

    def eof(self):
        return len(self.__values) == 0

    def join(self):
        pass

    def peekDateTime(self):
        # We can't determine when the next event will be generated since it'll
        # depend on the values generated by the barfeed being wrapped.
        return None

    def start(self):
        super(ResampledBarFeed, self).start()

    def stop(self):
        pass

    def checkNow(self, dateTime):
        if self.__range is not None and not self.__range.belongs(dateTime):
            self.__values.append(self.__grouper.getGrouped())
            self.__grouper = None
            self.__range = None
