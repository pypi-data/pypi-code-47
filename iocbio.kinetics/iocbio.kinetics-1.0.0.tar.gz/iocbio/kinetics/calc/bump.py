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
#from scipy.stats import linregress
import numpy as np
from scipy.interpolate import interp1d, PchipInterpolator
from scipy.optimize import leastsq, brentq
from PyQt5.QtCore import pyqtSignal, QObject

from .generic import AnalyzerGeneric, XYData, Stats
from iocbio.kinetics.constants import database_table_roi


class BumpSpline:
    def __init__(self, x, y, xmax, nodes_before=6, nodes_after=6, enforce_monotonic=True):
        """
        """
        self.x = x
        self.y = y
        self.xmax = xmax
        self.nodes_before = nodes_before
        self.nodes_after = nodes_after
        self.enforce_monotonic = enforce_monotonic
        self.spline_ready = False

        self.calcspline()

    def calcspline(self):
        print("Fitting bump: %d + %d nodes; x: %f %f" % (self.nodes_before, self.nodes_after, self.x[0], self.x[-1]))
        try:
            dx0 = (self.xmax-self.x[0]) / self.nodes_before
            dx1 = (self.x[-1]-self.xmax) / self.nodes_after

            self.xx = np.append(np.linspace(self.x[0]-dx0/10, self.xmax, self.nodes_before),
                                np.linspace(self.xmax, self.x[-1]+dx1/10, self.nodes_after)[1:])
            yy = np.ones(self.xx.shape)
            r = leastsq(self.spline_error, yy)
            self.make_spline(r[0])
            self.spline_ready = True
        except:
            print("Spline fitting failed. Exception occured during spline fitting")

    def make_spline(self, yy):
        if self.enforce_monotonic:
            val = yy[0]
            zz = [val]
            for i in range(1,self.nodes_before):
                val += yy[i]**2
                zz.append(val)
            for i in range(self.nodes_before, len(yy)):
                val -= yy[i]**2
                zz.append(val)
            self.spline = PchipInterpolator(self.xx, zz)
        else:
            #self.spline = interp1d(self.xx, yy, kind="cubic")
            self.spline = PchipInterpolator(self.xx, yy)

    def spline_error(self, pars):
        self.make_spline(pars)
        return self.curr_error()

    def curr_error(self):
        return self.y - self.spline(self.x)
        #return self.y[1:-1] - self.spline(self.x[1:-1])
        #return self.y[1:self.xmax] - self.spline(self.x[1:self.xmax])

    def __call__(self, x):
        if self.spline_ready:
            return self.spline(x)
        return None

    def min(self):
        if not self.spline_ready: return None
        return min(self.spline(self.x[0]), self.spline(self.x[-1]))

    def max(self):
        if not self.spline_ready: return None
        return self.spline(self.xmax)

    def _intersect_error(self, x):
        return self.spline(x) - self.intersect_value

    def intersect(self, value):
        """
        Assuming that value is between minima and maxima, finds two argument values
        closest to the maxima at which spline is equal to value
        """
        if not self.spline_ready:
            return None, None

        self.intersect_value = value
        data = self.spline(self.x) - self.intersect_value

        i_raise, i_fall = None, None

        idx_max = (np.abs(self.x-self.xmax)).argmin()

        # raise
        i = idx_max-1
        while i >= 0:
            if data[i+1] > 0 and data[i] <= 0:
                i_raise = self.x[i] + (self.x[i+1]-self.x[i]) / (data[i+1] - data[i]) * (-data[i])
                break
            i -= 1

        # fall
        i = idx_max
        imax = len(data) - 1
        while i < imax:
            if data[i+1] < 0 and data[i] >= 0:
                i_fall = self.x[i] + (self.x[i+1]-self.x[i]) / (data[i] - data[i+1]) * (data[i])
                break
            i += 1

        return i_raise, i_fall

        # self.intersect_value = value
        # try:
        #     a ,b = brentq(self._intersect_error, self.x[0], self.xmax), brentq(self._intersect_error, self.xmax, self.x[-1])
        # except:
        #     print("Exception occured during zero finding")
        #     return None, None
        # return a, b


class AnalyzerBump(AnalyzerGeneric):
    """Bump analyzer"""

    def __init__(self, x, y):
        AnalyzerGeneric.__init__(self, x, y)

    def fit(self, n, nodes_before=6, nodes_after=6, points_per_node=None, max_nodes=100):
        self.stats = {}

        k = np.blackman(n)
        c = np.convolve(k, self.experiment.y, mode='same')
        if len(c) != len(self.experiment.x) or len(self.experiment.x) < 3:
            print("Seems that some data are missing, skipping analysis")
            return

        xloc = np.argmax(c)
        self.stats['arg to peak'] = Stats('arg to peak', '', self.experiment.x[ xloc ])

        if points_per_node is not None:
            nodes_before = min(max_nodes, max(1, int(xloc/points_per_node)))+1
            nodes_after = min(max_nodes, max(1, int((self.experiment.x.shape[0]-xloc)/points_per_node)))

        self.spline = BumpSpline(self.experiment.x, self.experiment.y,
                                 self.experiment.x[ np.argmax(c) ],
                                 nodes_before=nodes_before, nodes_after=nodes_after)

        if self.spline.spline_ready:
            self.calc = XYData(self.experiment.x, self.spline(self.experiment.x))
        else:
            self.calc = XYData(None, None)


class AnalyzerBumpDatabaseSignals(QObject):
    sigUpdate = pyqtSignal()


class AnalyzerBumpDatabase(AnalyzerBump):

    @staticmethod
    def database_schema(db, tablename, peak):
        db.query("CREATE TABLE IF NOT EXISTS " + db.table(tablename) +
                 "(data_id text not null, " +
                 "type text not null, value double precision, PRIMARY KEY(data_id, type), " +
                 "FOREIGN KEY (data_id) REFERENCES " + db.table(database_table_roi) + "(data_id) ON DELETE CASCADE" +
                 ")")

        viewname = tablename + "_amplitude"
        if not db.has_view(viewname):
            if peak:
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                        "r.experiment_id, r.data_id, r.event_name, r.event_value, vmax.value-vend.value AS amplitude " +
                        "FROM " + db.table(tablename) + " vmax " +
                        "INNER JOIN " + db.table(tablename) + " vend ON vmax.data_id=vend.data_id " +
                        "INNER JOIN " + db.table("roi") + " r ON vmax.data_id=r.data_id " +
                        "WHERE vmax.type='value max' AND vend.type='value end'")
            else:
                db.query("CREATE VIEW " + db.table(viewname) + " AS SELECT " +
                        "r.experiment_id, r.data_id, r.event_name, r.event_value, vend.value-vmin.value AS amplitude " +
                        "FROM " + db.table(tablename) + " vmin " +
                        "INNER JOIN " + db.table(tablename) + " vend ON vmin.data_id=vend.data_id " +
                        "INNER JOIN " + db.table("roi") + " r ON vmin.data_id=r.data_id " +
                        "WHERE vmin.type='value min' AND vend.type='value end'")


    def __init__(self, database, tablename, data, x, y,
                 peak=True, argname="time", valunit="AU"):
        self.database_schema(database, tablename, peak)
        AnalyzerBump.__init__(self, x, y)

        self.signals = AnalyzerBumpDatabaseSignals()
        self.database = database
        self._database_table = tablename
        self.data = data # used by event name reader
        self.data_id = data.data_id
        self.t_reference = None # has to be found in deriving class
        self.peak = peak
        self.argname = argname
        self.valunit = valunit

    def fit(self, n, nodes_before=6, nodes_after=6, points_per_node=None, max_nodes=100):
        if len(self.experiment.x) < 1:
            return # nothing to analyze

        if not self.peak:
            self.experiment = XYData(self.experiment.x, -self.experiment.y)

        AnalyzerBump.fit(self, n=n, nodes_before=nodes_before, nodes_after=nodes_after,
                         points_per_node=points_per_node, max_nodes=max_nodes)

        if not bool(self.stats):
            return # nothing calculated

        tp = self.stats['arg to peak'].value
        self.stats[self.argname + ' to peak'] = Stats(self.argname + ' to peak', 's',
                                           self.stats['arg to peak'].value - self.t_reference)
        del self.stats['arg to peak']

        if self.calc.y is not None:
            # find time constants
            mx = self.calc.y.max()
            mn = max( self.calc.y[0], self.calc.y[-1] )
            for v in [5, 10, 25, 37, 50, 75]:
                i_raise, i_fall = self.spline.intersect(mn + (mx-mn)*v/100.0)
                if i_raise is not None:
                    self.stats['before %02d' % v] = Stats(self.argname + ' before %02d%%' % v, 's', tp - i_raise)
                if i_fall is not None:
                    self.stats['after %02d' % v] = Stats(self.argname + ' after %02d%%' % v, 's', i_fall - tp)

        # flip the sign back if needed
        if not self.peak:
            self.experiment = XYData(self.experiment.x, -self.experiment.y)
            if self.calc.y is not None:
                self.calc = XYData(self.calc.x,-self.calc.y)

        if self.calc.y is not None:
            # find signal range
            self.stats['value max'] = Stats('Maximal value', self.valunit,
                                            self.calc.y.max())
            self.stats['value min'] = Stats('Minimal value', self.valunit,
                                            self.calc.y.min())
            self.stats['value start'] = Stats('Value at the start', self.valunit, self.calc.y[0])
            self.stats['value end'] = Stats('Value at the end', self.valunit, self.calc.y[-1])
        else:
            # find signal range
            self.stats['value max'] = Stats('Maximal value', self.valunit,
                                            self.experiment.y.max())
            self.stats['value min'] = Stats('Minimal value', self.valunit,
                                            self.experiment.y.min())

        if self.database is not None:
            c = self.database
            for k, v in self.stats.items():
                if self.database.has_record(self._database_table, data_id=self.data_id, type=k):
                    c.query("UPDATE " + self.database.table(self._database_table) +
                              " SET value=:value WHERE data_id=:data_id AND type=:type",
                              value=v.value, data_id=self.data_id, type=k)
                else:
                    c.query("INSERT INTO " + self.database.table(self._database_table) +
                              "(data_id, type, value) VALUES(:data_id,:type,:value)",
                              data_id=self.data_id, type=k, value=v.value)
        self.signals.sigUpdate.emit()

    def remove(self):
        c = self.database
        c.query("DELETE FROM " + self.database.table(self._database_table) +
                " WHERE data_id=:data_id",
                data_id=self.data_id)
        self.database = None # through errors if someone tries to do something after remove
        self.signals.sigUpdate.emit()
