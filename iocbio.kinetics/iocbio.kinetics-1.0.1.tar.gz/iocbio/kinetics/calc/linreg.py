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
from scipy.stats import linregress
from .generic import AnalyzerGeneric, AnalyzerGenericSignals, XYData, Stats
from iocbio.kinetics.constants import database_table_roi

class AnalyzerLinRegress(AnalyzerGeneric):
    """Linear regression analyzer"""

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)

    def fit(self):
        sx = len(list(self.experiment.x))
        sy = len(list(self.experiment.y))
        if sx < 2 or sx != sy:
            print('Number of experiment points is too small for linear fit or inconsistent')
            for k in ['r_value', 'r_squared', 'p_value', 'std_err']:
                if k in self.stats: del self.stats[k]
            self.slope, self.intercept = None, None
            return
        
        self.slope, self.intercept, self.r_value, self.p_value, self.std_err = linregress(self.experiment.x, self.experiment.y)
        self.calc = XYData(self.experiment.x,
                           self.experiment.x*self.slope + self.intercept)
        self.stats['r_value'] = Stats("r", "", self.r_value)
        self.stats['r_squared'] = Stats("r-squared", "", self.r_value**2)
        self.stats['p_value'] = Stats("p", "", self.p_value)
        self.stats['std_err'] = Stats("std err", "", self.std_err)


class AnalyzerLinRegressDB(AnalyzerLinRegress):

    database_table = 'linregress'
    
    @staticmethod
    def database_schema(db):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(AnalyzerLinRegressDB.database_table) +
                 "(data_id text not null PRIMARY KEY, " +
                 "slope double precision not null, intercept double precision, " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE)")

    def __init__(self, database, data, channel):
        self.database_schema(database)
        AnalyzerLinRegress.__init__(self, data.x(channel), data.y(channel).data)

        self.signals = AnalyzerGenericSignals()
        self.database = database
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.channel = channel

    def fit(self):
        AnalyzerLinRegress.fit(self)
        if self.slope is None or self.intercept is None:
            self.remove()
            return
        c = self.database
        if self.database.has_record(self.database_table, data_id=self.data_id):
            c.query("UPDATE " + self.database.table(self.database_table) +
                    " SET slope=:slope, intercept=:intercept WHERE data_id=:data_id",
                    slope=self.slope,
                    intercept=self.intercept,
                    data_id=self.data_id)
        else:
            c.query("INSERT INTO " + self.database.table(self.database_table) +
                    "(data_id, slope, intercept) VALUES(:data_id,:slope,:intercept)",
                    slope=self.slope,
                    intercept=self.intercept,
                    data_id=self.data_id)
        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self.database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data.data_id)
        self.signals.sigUpdate.emit()

    def update_data(self, data):
        AnalyzerLinRegress.update_data(self, data.x(self.channel), data.y(self.channel).data)
        self.fit()

    def update_event(self, event_name):
        self.data.event_name = event_name
        self.data.event_value = 0

    @staticmethod
    def slice(data, x0, x1):
        sdata = data.slice(x0, x1)
        return sdata

    @staticmethod
    def auto_slicer(data):
        return []
