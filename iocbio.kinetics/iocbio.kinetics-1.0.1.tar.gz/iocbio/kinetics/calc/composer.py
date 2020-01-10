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
from .generic import AnalyzerGeneric
from .generic import Stats

from collections import OrderedDict
from PyQt5.QtCore import pyqtSignal, QObject


class AnalyzerComposeSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerCompose(AnalyzerGeneric):
    """Generic analyzer consisting of sub-analyzers"""

    def __init__(self):
        AnalyzerGeneric.__init__(self, None, None)
        self.analyzers = OrderedDict()
        self.signals = AnalyzerComposeSignals()

    def add_analyzer(self, key, analyzer):
        self.analyzers[key] = analyzer
        self.analyzers[key].signals.sigUpdate.connect(self._update_stats)
        self.analyzers[key].signals.sigUpdate.connect(self.signals.sigUpdate)
        self._update_stats()

    def list_analyzers(self):
        return list(self.analyzers.keys())

    def fit(self):
        for key, a in self.analyzers.items():
            a.fit()

    def remove(self):
        for key, a in self.analyzers.items():
            a.remove()

    def update(self):
        for key, a in self.analyzers.items():
            a.update()

    def update_data(self, data):
        for key, a in self.analyzers.items():
            a.update_data(data)

    def update_event(self, event_name):
        for key, a in self.analyzers.items():
            a.update_event(event_name)

    def _update_stats(self):
        self.stats = {}
        for key, a in self.analyzers.items():
            for sk, sv in a.stats.items():
                self.stats[key + ": " + sk] = Stats(key + ": " + sv.human, sv.unit, sv.value)
