# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Copyright (C) 2019-2020
#   Laboratory of Systems Biology, Department of Cybernetics,
#   School of Science, Tallinn University of Technology
#  This file is part of project: IOCBIO Kinetics
#
import numpy as np
from .generic import AnalyzerGeneric, AnalyzerGenericSignals, XYData, Stats
from ..constants import database_table_roi


class AnalyzerMeanMedStd(AnalyzerGeneric):
    """Analyzer finding mean, median, and std"""

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)

    def fit(self):
        self.stats['mean'] = Stats("mean", "", np.mean(self.experiment.y))
        self.stats['median'] = Stats("median", "", np.median(self.experiment.y))
        self.stats['std'] = Stats("std", "", np.std(self.experiment.y))
        self.calc = XYData(self.experiment.x,
                           self.experiment.x*0 + self.stats['mean'].value)


class AnalyzerMeanMedStdDB(AnalyzerMeanMedStd):
    @staticmethod
    def database_schema(db, tablename):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(tablename) +
                 "(data_id text not null PRIMARY KEY, " +
                 "mean double precision not null, median double precision, std double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE)")

    def __init__(self, database, data, tablename, channel):
        self.database_schema(database, tablename)
        AnalyzerMeanMedStd.__init__(self, data.x(channel), data.y(channel).data)

        self.signals = AnalyzerGenericSignals()
        self.database = database
        self._database_table = tablename
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.channel = channel

    def fit(self):
        AnalyzerMeanMedStd.fit(self)
        c = self.database
        if self.database.has_record(self._database_table, data_id=self.data_id):
            c.query("UPDATE " + self.database.table(self._database_table) +
                    " SET mean=:mean, median=:median, std=:std WHERE data_id=:data_id",
                    mean=self.stats['mean'].value,
                    median=self.stats['median'].value,
                    std=self.stats['std'].value,
                    data_id=self.data_id)
        else:
            c.query("INSERT INTO " + self.database.table(self._database_table) +
                    "(data_id, mean, median, std) VALUES(:data_id,:mean,:median,:std)",
                    mean=self.stats['mean'].value,
                    median=self.stats['median'].value,
                    std=self.stats['std'].value,
                    data_id=self.data_id)
        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self._database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerMeanMedStd.update_data(self, data.x(self.channel), data.y(self.channel).data)
        self.fit()

    def update_event(self, event_name):
        pass
