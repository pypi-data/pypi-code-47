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
# Generic analyzer used to show summarizing XY plots

from PyQt5.QtCore import pyqtSignal, QObject
from .generic import Stats, XYData, AnalyzerGeneric


class AnalyzerXYSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerXY(AnalyzerGeneric):

    def __init__(self, database, table_name, value_name, data, axisnames, axisunits):
        AnalyzerGeneric.__init__(self, [], []) # start with empty data

        self.signals = AnalyzerXYSignals()
        self.database = database
        self.table_name = table_name
        self.value_name = value_name
        self.experiment_id = data.experiment_id
        self.axisnames = axisnames
        self.axisunits = axisunits

        self.get_data()

    def get_data(self):
        c = self.database
        v0 = 0
        x = []
        y = []
        for row in c.query("SELECT " + self.value_name + " AS value, event_value FROM " +
                           self.database.table(self.table_name) +
                           " WHERE experiment_id=:experiment_id AND event_value IS NOT NULL ORDER BY event_value ASC",
                           experiment_id = self.experiment_id):
            x.append(row.event_value)
            y.append(row.value)
        self.experiment = XYData(x, y)
        self.signals.sigUpdate.emit()

    def update(self):
        self.get_data()
