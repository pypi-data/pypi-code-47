# Copyright 2019-- Derk Kappelle
#
# This file is part of MooPy, a Python package with
# Multi-Objective Optimization (MOO) tools.
#
# MooPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MooPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MooPy.  If not, see <http://www.gnu.org/licenses/>.

"""
Collection of scalarization techniques for Multiple run methods.
"""

from __future__ import absolute_import, division, print_function

import numpy as np
from scipy.optimize import minimize


def SOOP_NC(self, x):
    pass


def SOOP_EC(self, x):

    dp = self.get_dp(x)

    # g_i(x) >= 0, i = 1, ..., m

    con = [{'type': 'ineq', 'fun': lambda x: dp.f[0] - self.funcs.single_func(0)(x), }]
    # if self.jac.jac_ini == '2-point' or self.jac.jac_ini == '3-point': %%%%%%%%'jac': self.jac.single_grad_neg(1)
    #     con[0]['jac'] = self.jac.jac_ini jac=self.jac.single_grad(0)

    cons = self.constraints.add_constraint(con)

    res = minimize(self.funcs.single_func(1), dp.x, bounds=self.limits.lims_ini,
                   constraints=cons, )

    if np.all(dp.x == res.x):
        return dp
    else:
        return self.get_dp(res.x)

















