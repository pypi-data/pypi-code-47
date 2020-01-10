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
import copy, uuid
import numpy as np


class Carrier:
    def __init__(self, name, unit, data):
        self.name = name
        self.unit = unit
        self.data = data


class Data(object):
    """Class for representing recorded data"""

    def __init__(self, experiment_id,
                 comment = None,
                 data = {},
                 xname = None,
                 xunit = None,
                 xlim = None,
                 config = {},
                 type = None,
                 type_generic = None,
                 name = None,
                 time = None,
                 data_id = None,
                 add_range=0.05):

        if data_id is None:
            data_id = str(uuid.uuid4())

        self._data = data
        self._xname = xname
        self._xunit = xunit
        self._xlim = xlim
        self.config = config
        self.type = type
        self.type_generic = type_generic
        self.name = name
        self.time = time
        self.experiment_id = experiment_id
        self.data_id = data_id
        self.event_name = None
        self.event_value = None
        self.add_range = add_range
        k = list(self._data.keys())

    def x(self, name):
        if name is None:
            return self.x(name=self._rep_key)
        return self._data[name]['x']

    def xlim(self):
        return self._xlim

    @property
    def xname(self):
        return self._xname

    @property
    def xunit(self):
        return self._xunit

    def y(self, name):
        return self._data[name]['y']

    def keys(self):
        return self._data.keys()

    def slice(self, x0, x1, data_id=None, event_name=None, event_value=None):
        a = copy.deepcopy(self)
        if data_id is None:
            data_id = str(uuid.uuid4())
        a.data_id = data_id
        a.event_name = event_name
        a.event_value = event_value
        a._xlim = (x0, x1)

        for k in a._data.keys():
            
            i0 = np.argmin(np.abs(self._data[k]['x']-x0))
            i1 = np.argmin(np.abs(self._data[k]['x']-x1))
            a._data[k]['x'] = a._data[k]['x'][i0:i1]
            a._data[k]['y'].data = a._data[k]['y'].data[i0:i1]
        return a

    def new_range(self, x0):
        minx, maxx = self.xlim()
        w = self.add_range*(maxx-minx)
        return [x0, x0+w]

    def __repr__(self):
        s = 'type: %s; expid: %s; dataid: %s\nx: %s ' % (self.type, self.experiment_id, self.data_id,
                                                         self._xname)
        # if self.x.data is not None: s += "%f..%f" % (self.x.data[0], self.x.data[-1])
        # s += "; data:"
        # for i in self.data:
        #     s += i + " "
        # s += "\nconfig:\n"
        # for k, v in self.config.items():
        #     s += k + ": " + str(v) + "\n"

        return s
