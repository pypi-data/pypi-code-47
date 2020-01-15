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
Unified interfaces to "a priori" MOOP methods.

Functions
---------
- solve : Produces Pareto front for M > 2.
- solve_BOOP : Produces Pareto front for M = 2.
"""

from __future__ import absolute_import, division, print_function

__all__ = ['solve_moop', 'solve_boop']

from .core import WS, EC, NC


def solve_moop():
    raise NotImplementedError("method not implemented yet")
    pass


def solve_boop(funs, ds_ini=None, limits=None, constraints=None, jacobian=None,
               method='NC', options=None, *args, ** kwargs):

    """Producing the Pareto front of 2 objective functions.

    Parameters
    ----------
    funs : list
        List of two objective functions, callable.
        Each function must return a scalar.

    ds_ini : list or ndarray, shape (n,), optional
        If ndarray it is treated as initial guess.
        Array of real elements of size (n,),
        where 'n' is the number of independent variables.
        Else it is a list of initial Pareto points (ndarray).
        If the list contains only one Pareto point it will
        as a special initial guess. When the list contains
        2 or more points the Pareto front between these points
        is produced.

    limits : sequence or `design limits`, optional
        Sequence of ``(min, max)`` pairs for each element in `x`. None
               is used to specify no bound.

        See Scipy documentation

    constraints : {Constraint, dict} or List of {Constraint, dict}, optional
        Each dictionary with fields:

            type : str
                Constraint type: 'eq' for equality, 'ineq' for inequality.
            fun : callable
                The function defining the constraint.
            jac : callable, optional
                The Jacobian of `fun` (only for SLSQP).
            args : sequence, optional
                Extra arguments to be passed to the function and Jacobian.

        See Scipy documentation

    jacobian : list of {callable,  '2-point', '3-point', 'cs', bool}, optional
        Methods for computing the gradient vectors of each objective function.

    method : str or callable, optional
        Type of solver.  Should be one of
            - 'NC'        :ref:`(see here) <>`
            - 'PSE'       :ref:`(see here) <>`

        If not given, 'NC'

    options : dict, optional
        A dictionary of solver options. All methods accept the following
        generic options:

            maxiter : int
                Maximum number of iterations to perform. Depending on the
                method each iteration may use several function evaluations.
            disp : bool
                Set to True to print convergence messages.

        For method-specific options, see :func:`show_options()`.

    Returns
    -------
    res : OptimizeResult
        The optimization result represented as a ``OptimizeResult`` object.
        Important attributes are: ``x`` the solution array, ``success`` a
        Boolean flag indicating if the optimizer exited successfully and
        ``message`` which describes the cause of the termination. See
        `OptimizeResult` for a description of other attributes
    """

    # x0 = np.asarray(x0)
    # if x0.dtype.kind in np.typecodes["AllInteger"]:
    #     x0 = np.asarray(x0, dtype=float)

    if not isinstance(args, tuple):
        args = (args,)

    if method is None:
        method = 'NC'

    if callable(method):
        meth = "_custom"
    else:
        meth = method.lower()

    if options is None:
        options = {}
    else:
        options = dict(options)

    if meth == 'ws':
        WS_method = WS(funs=funs,
                       ds_ini=ds_ini,
                       lims=limits,
                       cons=constraints,
                       jac=jacobian,
                       options=options,
                       )

        return WS_method.solve()

    if meth == 'ec':
        EC_method = EC(funs=funs,
                       ds_ini=ds_ini,
                       lims=limits,
                       cons=constraints,
                       jac=jacobian,
                       options=options,
                       )

        return EC_method.solve()

    if meth == 'nc':
        NC_method = NC(funs=funs,
                       ds_ini=ds_ini,
                       lims=limits,
                       cons=constraints,
                       jac=jacobian,
                       options=options,
                       )

        return NC_method.solve()


    else:
        raise ValueError('Unknown solver %s' % method)






