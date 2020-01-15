import numpy as np
from math import pi
from .core import FunctionWrapper, ConstraintWrapper, LimitWrapper, JacobianWrapper


def case(n):
    if n == 'sim_lin':
        return sim_lin()
    elif n == 'sim_lin_2':
        return sim_lin_2()
    elif n == 'sim_nlin':
        return sim_nlin()
    elif n == 'sim_lim':
        return sim_lim()
    elif n == 'sim_lim_2':
        return sim_lim_2()
    elif n == 'sim_con':
        return sim_con()
    elif n == 'sim_con_2':
        return sim_con_2()
    elif n == 'lim_con_nat':
        return lim_con_nat()
    elif n == 'BaK':
        return BaK()
    elif n == 'CaH':
        return CaH()
    elif n == 'FFf':
        return FFf()
    elif n == 'Tf4':
        return Tf4()
    elif n == 'Sf1':
        return Sf1()
    elif n == 'ZDT1':
        return ZDT1()
    elif n == 'ZDT1_extra':
        return ZDT1_extra()
    elif n == 'ZDT2':
        return ZDT2()
    elif n == 'ZDT2_extra':
        return ZDT2_extra()
    elif n == 'ZDT4':
        return ZDT4()
    elif n == 'ZDT6':
        return ZDT6()
    elif n == 'OaK':
        return OaK()
    elif n == 'CPT1':
        return CPT1()
    elif n == 'CEx':
        return CEx()
    elif n == 'LZf4':
        return LZf4()

    # Not working
    # elif n == 'Vif':
    #     return Vif()
    elif n == 'ZDT3':
        return ZDT3()
    elif n == 'disco':
        return disco()
    elif n == 'tintout':
        return tintout()
    elif n == 'KUR':
        return KUR()
    elif n == 'KUR_2':
        return KUR_2()
    elif n == 'ZTD2_2':
        return ZTD2_2()
    elif n == 'ZTD3_2':
        return ZTD3_2()


def sim_lin():  # Simple linear
    # Define objective functions
    def fun1(x):
        return (x[0] - 3)**2 + (x[1] - 3)**2 + 1

    def fun2(x):
        return (x[0] - 1)**2 + (x[1] - 1)**2 + 1

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # Initial Data set
    ds_ini = [np.array([3.0, 3.0]),
              np.array([1.0, 1.0])]

    # Jacobian
    def jac1(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    def jac2(x):
        return np.asarray([2 * (x[0] - 1), 2 * (x[1] - 1)], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def sim_lin_2():  # Simple non-linear
    # Define objective functions
    def fun1(x):
        return (x[0] - 3)**2 + (x[1] - 3)**2 + 1

    def fun2(x):
        return (x[0] - 1)**4 + (x[1] - 1)**4 + 1

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # Initial Data set
    ds_ini = [[np.array([3.0, 3.0]), 0],
              [np.array([1.0, 1.0]), 1]]

    # Jacobian
    def jac1(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    def jac2(x):
        return np.asarray([4 * (x[0] - 1)**3, 4 * (x[1] - 1)**3], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def sim_nlin():  # Simple non-linear
    # Define objective functions
    def fun1(x):
        return (x[0] - 3)**2 + (x[1] - 3)**2 + 1

    def fun2(x):
        return 0.25*(x[0] - 1)**2 + (x[1] - 1)**2 + 1

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # Initial Data set
    ds_ini = [[np.array([3.0, 3.0]), 0],
              [np.array([1.0, 1.0]), 1]]

    # Jacobian
    def jac1(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    def jac2(x):
        return np.asarray([0.5 * (x[0] - 1), 2 * (x[1] - 1)], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def sim_lim():  # Simple and limited
    # Define objective functions
    def fun1(x):
        return (x[0] - 3)**2 + (x[1] - 3)**2 + 2

    def fun2(x):
        return x[0] + 2*x[1]

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([2.6,2.2])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.array([3.0, 3.0]), 0],
              [np.array([0.0, 0.0]), 1]]

    # Jacobian
    def jac1(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    def jac2(x):
        return np.array([1., 2.])

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options
        # funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def sim_lim_2():  # Simple and limited
    # Define objective functions
    def fun1(x):
        return x[0] + 2 * x[1]

    def fun2(x):
        return (x[0] - 3) ** 2 + (x[1] - 3) ** 2 + 2


    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.array([0.0, 0.0]), 0],
              [np.array([3.0, 3.0]), 1]]

    # Jacobian
    def jac1(x):
        return np.array([1., 2.])

    def jac2(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def sim_con():   # Simple and constrained
    # Define objective functions
    def fun1(x):
        return (x[0] - 3)**2 + (x[1] - 3)**2 + 2

    def fun2(x):
        return x[0] + 2*x[1]

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: -(0.1*x[0]**2 - x[1] + 0.5)}]

    # initial Data set
    ds_ini = [[np.array([3.0, 3.0]), 0],
              [np.array([0.0, 0.5]), 1]]

    # Jacobian
    def jac1(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    def jac2(x):
        return np.array([1., 2.], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def sim_con_2():   # Simple and constrained
    # Define objective functions
    def fun1(x):
        return x[0] + 2 * x[1]

    def fun2(x):
        return (x[0] - 3) ** 2 + (x[1] - 3) ** 2 + 2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: -(0.1*x[0]**2 - x[1] + 0.5)}]

    # initial Data set
    ds_ini = [[np.array([0.0, 0.5]), 0],
              [np.array([3.0, 3.0]), 1]]

    # Jacobian
    def jac1(x):
        return np.array([1., 2.], dtype=float)

    def jac2(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def lim_con_nat():   # Simple and constrained
    # Define objective functions
    def fun1(x):
        return x[0] + 2 * x[1]

    def fun2(x):
        return (x[0] - 3) ** 2 + (x[1] - 3) ** 2 + 2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: -(0.1*x[0]**2 - x[1] - 0.1)}]

    # initial Data set
    ds_ini = [[np.array([0.0, 0.0]), 0],
              [np.array([3.0, 3.0]), 1]]

    # Jacobian
    def jac1(x):
        return np.array([1., 2.], dtype=float)

    def jac2(x):
        return np.asarray([2 * (x[0] - 3), 2 * (x[1] - 3)], dtype=float)

    jac = [jac1, jac2]

    # MOO method of updating sections
    moo_options = {}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def BaK():
    # Define objective functions
    def fun1(x):
        return 4*x[0]**2 + 4*x[1]**2

    def fun2(x):
        return (x[0] - 5)**2 + (x[1] - 5)**2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0.])

    # Limits
    limits = ([0., 5.], [0., 3.])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: -(((x[0] - 5)**2 + x[1]**2) - 25)},
                   {'type': 'ineq', 'fun': lambda x: (x[0] - 8)**2 + (x[1] + 3)**2 - 7.7}]


    # initial Data set
    ds_ini = [[np.asarray([0., 0.]), 0],
              [np.asarray([5., 3.]), 1]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'max_it': 1000, 'd1':0.01, 'd2':0.3}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def CaH():
    # Define objective functions
    def fun1(x):
        return 2 + (x[0] - 2)**2 + (x[1] - 1)**2

    def fun2(x):
        return 9*x[0] - (x[1] - 1)**2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0.])

    # Limits
    limits = ([-20., 20.], [-20., 20.])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: -(x[0]**2 + x[1]**2) + 225},
                   {'type': 'ineq', 'fun': lambda x: -(x[0] - 3*x[1] + 10.)}]


    # initial Data set
    ds_ini = [[np.asarray([1.1, 3.7]), 0],
              [np.asarray([ -4.84097722932 , 14.1973569421 ]), 1]]
    # ds_ini = [[np.asarray([1.09558503219 , 3.69852834406 ]), 0],
    #           [np.asarray([ -4.84097722932 , 14.1973569421 ]), 1]]
    # ds_ini = [[np.asarray([1.09558503219 , 3.69852834406 ]), 0],
    #           [np.asarray([-2.19940578791 , 2.6001980707]), 0],
    #           [np.asarray([ -4.84097722932 , 14.1973569421 ]), 1]]
      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 50, 'd1':0.01, 'd2':0.3}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def FFf():
    n = 20

    def fun1(x):
        sum = 0
        for i in range(0, n - 1):
            sum = sum + (x[i] - 1/np.sqrt(n)) ** 2
        f1 = 1 - np.exp(-sum)
        return f1

    def fun2(x):
        sum = 0
        for i in range(0, n - 1):
            sum = sum + (x[i] + 1/np.sqrt(n)) ** 2
        f2 = 1 - np.exp(-sum)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.zeros(n)

    # Limits
    limits = tuple([[-4.,4.] for i in range(n)])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[(1/np.sqrt(n))*np.ones(n), 0],
              [-(1/np.sqrt(n))*np.ones(n), 1]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 300, 'max_it': 50000, 'd1':0.01, 'd2':0.1}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def Tf4():
    n = 2

    def fun1(x):
        return x[0]**2 - x[1]

    def fun2(x):
        return -0.5*x[0]-x[1]-1

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.zeros(n)

    # Limits
    limits = tuple([[-7., 4.] for i in range(n)])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: 6.5 - x[0]/6 - x[1]},
                   {'type': 'ineq', 'fun': lambda x: 7.5 - 0.5*x[0] - x[1]},
                   {'type': 'ineq', 'fun': lambda x: 30 - 5.*x[0] - x[1]}]

    # initial Data set
    ds_ini = [[np.asarray([0., 4.]), 0],
              [np.asarray([4., 4.]), 1]]

      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 50, 'd1':0.01, 'd2':0.15}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def Sf1():
    n = 1

    def fun1(x):
        return x[0]**2

    def fun2(x):
        return (x[0] - 2)**2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.zeros(n)

    # Limits
    limits = tuple([[-1e10, 1e10] for i in range(n)])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.asarray([0.]), 0],
              [np.asarray([2.]), 1]]

      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 30e10, 'max_it': 50000, 'd1':0.01, 'd2':0.1}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def ZDT1():
    n = 30
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        return 1 + 9*(sum)/(n-1)

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / g(x))

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.random.random_sample((n,))
    x_ini[0] = 0.0

    # Limits
    limits = tuple([[0., 1.] for i in range(n)])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.zeros(n), 1]]
    ds_ini[1][0][0] = 1.

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'max_it': 10000, 'd1':0.001, 'd2':0.08}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def ZDT1_extra():
    n = 30
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        return 1 + 9*(sum)/(n-1)

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / g(x))

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    np.random.seed(12345)
    x_ini = np.random.random_sample((n,))
    x_ini[0] = 0.0

    # Limits
    limits = tuple([[0., 1.] for i in range(n)])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.zeros(n), 1]]
    ds_ini[1][0][0] = 1.
    ds_ini[0][0] = x_ini

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'max_it': 10000, 'd1':0.001, 'd2':0.08}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def ZDT2():
    n = 30
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        return 1 + 9*(sum**2)/29

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - (fun1(x) / g(x))**2

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.])
    # Limits
    limits = ([0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              )

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.zeros(n), 1]]
    ds_ini[1][0][0] = 1.

      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 20, 'max_it': 10000, 'd1':0.01, 'd2':0.1}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def ZDT2_extra():
    n = 30
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        return 1 + 9*(sum**2)/29

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - (fun1(x) / g(x))**2

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.])
    # Limits
    limits = ([0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              )

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.zeros(n), 1]]
    ds_ini[1][0][0] = 1.

      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 20, 'max_it': 10000, 'reversed': True, 'd1':0.01, 'd2':0.1}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def ZDT4():
    n = 10
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, n):
            sum = sum + (x[i]**2 - 10*np.cos(4*np.pi*x[i]))
        return 91 + sum

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / g(x))

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.zeros(n)
    x_ini[0] = 0.25000184

    # Limits
    limits = tuple([[0., 1.]] + [[-5., 5.] for i in range(n) if i > 0])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.zeros(n), 1]]
    ds_ini[1][0][0] = 1.0

    # [0.5  0.   0.   0.   0.   0.   0.   0.   0.   0.]

      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 30, 'max_it': 20000, 'd1':0.01, 'd2':0.1}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def ZDT6():
    n = 10
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, n):
            sum = sum + x[i]
        return 1 + 9*(sum/9)**(0.25)

    def fun1(x):
        return 1 - np.exp(-4*x[0])*(np.sin(6*np.pi*x[0]))**6

    def h(x):
        return 1 - (fun1(x) / g(x))**2

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.ones(n)

    # Limits
    limits = tuple([[0., 1.] for i in range(n)])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.zeros(n), 1]]
    # ds_ini[0][0][0] = 0.138926257009
    # ds_ini[1][0][0] = 0.08145779

    # ds_ini[1][0][0] = 0.08145779
    # ds_ini[0][0][0] = 0.164671216622

    ds_ini[0][0][0] = 0.08145
    ds_ini[1][0][0] = 0.0

      # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 140, 'max_it': 20000, 'd1':0.01, 'd2':0.005}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def OaK():
    n = 6
    # Define objective functions

    def fun1(x):
        return -25*(x[0] - 2)**2 - (x[1] - 2)**2 - (x[2] - 1)**2 - (x[3] - 4)**2 - (x[4] - 1)**2

    def fun2(x):
        sum = 0
        for i in range(n):
            sum += x[i]**2
        return sum

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.ones(n)

    # Limits
    limits = [[0., 10.] for i in range(n)]
    limits[2] = [1., 5.]
    limits[4] = [1., 5.]
    limits[3] = [0., 6.]

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: x[0] + x[1] - 2},
                   {'type': 'ineq', 'fun': lambda x: 6. - x[0] - x[1]},
                   {'type': 'ineq', 'fun': lambda x: 2 - x[1] + x[0]},
                   {'type': 'ineq', 'fun': lambda x: 2 - x[0] + 3*x[1]},
                   {'type': 'ineq', 'fun': lambda x: 4 - (x[2] - 3)**2 - x[3]},
                   {'type': 'ineq', 'fun': lambda x: (x[4] - 3)**2 + x[5] - 4}]

    # initial Data set
    ds_ini = [[np.asarray([5., 1.,  5., 0., 5., 0.]), 0],
              [np.asarray([1., 1.,  1., 0., 1., 0.]), 1]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 40, 'max_it': 20000, 'd1':0.01, 'd2':0.2}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def CPT1():
    n = 2
    # Define objective functions

    def fun1(x):
        return x[0]

    def fun2(x):

        return (1 + x[1])*np.exp(-x[0]/(1 + x[1]))

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.ones(n)

    # Limits
    limits = [[0., 1.] for i in range(n)]

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: fun2(x)/(0.858*np.exp(-0.541*fun1(x)))-1},
                   {'type': 'ineq', 'fun': lambda x: fun2(x)/(0.728*np.exp(-0.295*fun1(x)))-1},
                   ]

    # initial Data set
    ds_ini = [[np.asarray([0., 0.]), 0],
              [np.asarray([1., 0.225628442954]), 0]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 30, 'max_it': 10000, 'd1':0.01, 'd2':0.035}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def CEx():
    n = 2
    # Define objective functions

    def fun1(x):
        return x[0]

    def fun2(x):

        return (1 + x[1])/x[0]

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.ones(n)

    # Limits
    limits = [[0.1, 1.], [0., 5.]]

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: x[1] + 9*x[0] - 6},
                   {'type': 'ineq', 'fun': lambda x: -x[1] + 9*x[0] - 1},
                   ]

    # initial Data set
    ds_ini = [[np.asarray([0.38888889, 2.5]), 0],
              [np.asarray([1., 0.]), 0]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 30, 'max_it': 10000, 'd1':0.01, 'd2':0.15}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


def LZf4():  # LZf4 problem
    n = 30

    J1 = list(range(2, n, 2))
    J2 = list(range(1, n, 2))

    # Define objective functions
    def fun1(x):
        sum = 0
        for i in range(0, len(x) - 1):
            if i in J1:
                sum = sum +  (x[i] - 0.8*x[0]*np.cos((6*np.pi*x[0] + i*np.pi/(n-1))/3))**2
        f1 = x[0] + 2*sum/len(J1)
        return f1

    def fun2(x):
        sum = 0
        for i in range(0, len(x) - 1):
            if i in J2:
                sum = sum + (x[i] - 0.8 * x[0] * np.sin((6 * np.pi * x[0] + i * np.pi / (n - 1))))**2
        f2 = 1 - np.sqrt(x[0]) + 2 * sum / len(J2)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.zeros(n)

    # Limits
    limits = tuple([[0., 1.]] + [[-1., 1.] for i in range(n) if i > 0])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.zeros(n), 0],
              [np.ones(n), 1]]
    for i in range(0, n - 1):
        if i in J1:
            ds_ini[1][0][i] = 0.8 * np.cos((6 * np.pi + i * np.pi / (n - 1)) / 3)
        if i in J2:
            ds_ini[1][0][i] = 0.8 * np.sin((6 * np.pi + i * np.pi / (n - 1)))


    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 200, 'max_it': 100000, 'dd_method':{'df':np.asarray([0.05, -0.05])}, 'd1':0.01, 'd2':0.1}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


##------------ Discontinuous problems ------------##
def KUR():  # KUR problem
    # Define objective functions
    def fun1(x):
        sum = 0
        for i in range(0, len(x) - 1):
            sum = sum - 10 * np.exp(-0.2 * np.sqrt((x[i]) ** 2 + (x[i + 1]) ** 2))
        f1 = sum
        return f1

    def fun2(x):
        sum = 0
        for i in range(0, len(x)):
            sum = sum + (np.abs(x[i]) ** 0.8 + 5 * (np.sin((x[i]))) ** 3)
        f2 = sum
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0.0, 0.0, 0.0])

    # Limits
    limits = ([-5, 5], [-5, 5], [-5, 5])

    # Constraints
    constraints = None

    # initial Data set
    # ds = [[np.asarray([0.0, 0.0, 0.0]),0],
    #       [np.asarray([-1.5216198, 0.0, 0.0]),1],
    #       [np.asarray([0.0, 0.0, -1.5216198]),1],
    #       [np.asarray([-1.5216198, 0.0, -1.5216198]),1],
    #       [np.asarray([-1.5216198, -1.5216198, -1.5216198]),1]]

    ds_ini = [[np.asarray([-1.00940081e-08,   8.19811851e-09,   5.71849748e-09]),0],
          [np.asarray([-8.56028533e-14,  -5.08347373e-14,  -1.52161916e+00]),1],
          [np.asarray([ -1.52161912e+00,  -1.10468205e-13,  -1.52161897e+00]),1],
          [np.asarray([-1.52161954, -1.52161821, -1.5216178 ]),1]]

    # Jacobian
    jac = '3-point'

    # MOO method of updating sections
    moo_options = {'Npar': 300, 'delta': 40, 'finish_min': False, 'SOOP_options':{'Restricted':True}, 'd1':0.01, 'd2':0.02}

    # wrap functions
    funcs = FunctionWrapper(funcs)
    limits = LimitWrapper(limits, len(x_ini))
    constraints = ConstraintWrapper(constraints)
    jac = JacobianWrapper(funcs.funcs_ini, jac)

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options


############# Not working ############################


def LZF4():
    # Define objective functions
    def fun1(x):
        return 2 + (x[0] - 2)**2 + (x[1] - 1)**2

    def fun2(x):
        return 9*x[0] - (x[1] - 1)**2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0.])

    # Limits
    limits = ([-20., 20.], [-20., 20.])

    # Constraints
    constraints = [{'type': 'ineq', 'fun': lambda x: -(x[0]**2 + x[1]**2) + 225},
                   {'type': 'ineq', 'fun': lambda x: -(x[0] - 3*x[1] + 10.)}]


    # initial Data set
    # ds_ini = [[np.asarray([1.1, 3.7]), 0],
    #           [np.asarray([ -4.84097722932 , 14.1973569421 ]), 1]]
    # ds_ini = [[np.asarray([1.09558503219 , 3.69852834406 ]), 0],
    #           [np.asarray([ -4.84097722932 , 14.1973569421 ]), 1]]
    ds_ini = [[np.asarray([1.09558503219 , 3.69852834406 ]), 0],
              [np.asarray([-2.19940578791 , 2.6001980707]), 0],
              [np.asarray([ -4.84097722932 , 14.1973569421 ]), 1]]
      # Jacobian
    jac = None

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def disco():   # Discontinuous
    # Define objective functions
    def a(x):
        return 1 + 9*(x[1] - 1)**2

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / a(x)) - (fun1(x) / a(x)) * np.sin((1.5/2.5) * pi * fun1(x))

    def fun2(x):
        f2 = 0.1*a(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.array([3, 4])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.array([0.0, 1.0]), 0],
              [np.array([1.163, 1.0]), 1],
              [np.array([4.2485, 1.0]), 1]]

    # ds_ini = [[np.array([0.0, 0.9939631]), 0],
    #           [np.array([1.16359019,  1.00024886]), 1],
    #           [np.array([4.24886734,  1.0653759]), 1]]

    # Jacobian
    jac = None

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def tintout():  # 2 in 3 out
    # Define objective functions
    def fun1(x):
        return (x[0] - 1)**2 + (x[1] - 1)**2 + 1

    def fun2(x):
        return (x[0] - 4)**2 + (x[1] - 2)**2 + 1

    def fun3(x):
        return (x[0] - 2)**2 + (x[1] - 4)**2 + 1

    funcs = [fun1, fun2, fun3]

    # Initial input
    x_ini = np.array([1, 1])

    # Limits
    limits = ([0, 5], [0, 5])

    # Constraints
    constraints = None

    # Initial Data set
    ds_ini = [[np.array([1.0, 1.0]), 0],
              [np.array([4.0, 2.0]), 1],
              [np.array([2.0, 4.0]), 2]]

    # Jacobian
    def jac1(x):
        return np.asarray([2 * (x[0] - 1), 2 * (x[1] - 1)], dtype=float)

    def jac2(x):
        return np.asarray([2 * (x[0] - 4), 2 * (x[1] - 2)], dtype=float)

    def jac3(x):
        return np.asarray([2 * (x[0] - 2), 2 * (x[1] - 4)], dtype=float)

    jac = [jac1, jac2, jac3]

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def ZTD2_2():
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        return 1 + 9*(sum**2)/29

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - (fun1(x) / g(x))**2

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun2, fun1]

    # Initial input
    x_ini = np.asarray([0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.])
    # Limits
    limits = ([0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              )

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.asarray([1., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 0],
              [np.asarray([0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1]]

      # Jacobian
    jac = None

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def ZTD2_2t():
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        # return 1 + 9*(sum**2)/29
        return 1 + 9*sum/29

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / g(x)) - (fun1(x) / g(x)) * np.sin(10 * pi * fun1(x))

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.])
    # Limits
    limits = ([0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              )

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.asarray([0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 0],
              [np.asarray([0.083, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.257763, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.45388, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.65251159, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.85183286, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1]]

      # Jacobian
    jac = None

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def ZDT3():
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        # return 1 + 9*(sum**2)/29
        return 1 + 9*sum/29

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / g(x)) - (fun1(x) / g(x)) * np.sin(10 * pi * fun1(x))

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.])
    # Limits
    limits = ([0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              )

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.asarray([0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 0],
              [np.asarray([0.083, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.257763, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.45388, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.65251159, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1],
              [np.asarray([0.85183286, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1]]

      # Jacobian
    jac = None

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def ZTD3_2():
    # Define objective functions
    def g(x):
        sum = 0
        for i in range(1, len(x)):
            sum = sum + x[i]
        # return 1 + 9*(sum**2)/29
        return 1 + 9*sum/29

    def fun1(x):
        return x[0]

    def h(x):
        return 1 - np.sqrt(fun1(x) / g(x)) - (fun1(x) / g(x)) * np.sin(10 * pi * fun1(x))

    def fun2(x):
        f2 = g(x)*h(x)
        return f2

    funcs = [fun1, fun2]

    # Initial input
    x_ini = np.asarray([0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0.])
    # Limits
    limits = ([0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
              )

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.asarray([0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 0],
              [np.asarray([0.85183286, 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.,
                           0., 0., 0., 0., 0.]), 1]]

      # Jacobian
    jac = None

    # Hessian
    hess = None

    # MOO method of updating sections
    moo_method = None
    moo_options = {}

    # Method for initialization of the data set
    ini_method = None
    ini_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, \
           hess, moo_method, ini_method, moo_options, ini_options

def KURtest():  # KUR problem
    # Define objective functions
    def fun1(x):
        sum = 0
        for i in range(0, len(x) - 1):
            sum = sum - 10 * np.exp(-0.2 * np.sqrt((x[i]) ** 2 + (x[i + 1]) ** 2))
        f1 = sum
        return f1

    def fun2(x):
        sum = 0
        for i in range(0, len(x)):
            sum = sum + (np.abs(x[i]) ** 0.8 + 5 * (np.sin((x[i]))) ** 3)
        f2 = sum
        return f2

    funcs = [fun1, fun2]

    # Initial input
    # x0 = np.asarray([-1.5216198, 0.0, -1.5216198])
    x_ini = np.asarray([0.0, 0.0, 0.0])
    # x0 = np.asarray([4.0, 4.0, 4.0])

    # Limits
    limits = ([-5, 5], [-5, 5], [-5, 5])

    # Constraints
    constraints = None
    # initial Data set
    # ds = [[np.asarray([0.0, 0.0, 0.0]),0],
    #       [np.asarray([-1.5216198, 0.0, 0.0]),1],
    #       [np.asarray([0.0, 0.0, -1.5216198]),1],
    #       [np.asarray([-1.5216198, 0.0, -1.5216198]),1],
    #       [np.asarray([-1.5216198, -1.5216198, -1.5216198]),1]]

    ds_ini = [[np.asarray([-1.00940081e-08,   8.19811851e-09,   5.71849748e-09]),0],
          [np.asarray([-1.5216198, 0.0, 0.0]),1],
          [np.asarray([-8.56028533e-14,  -5.08347373e-14,  -1.52161916e+00]),1],
          [np.asarray([ -1.52161912e+00,  -1.10468205e-13,  -1.52161897e+00]),1],
          [np.asarray([-1.52161954, -1.52161821, -1.5216178 ]),1]]

    # ds = [[np.asarray([-1.00940081e-08,   8.19811851e-09,   5.71849748e-09]),0],
    #       # [np.asarray([-1.5216198, 0.0, 0.0]),1],
    #       [np.asarray([-8.56028533e-14,  -5.08347373e-14,  -1.52161916e+00]),1]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {}

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options

def KUR_2():  # KUR problem
    # Define objective functions
    def fun1(x):
        sum = 0
        for i in range(0, len(x) - 1):
            sum = sum - 10 * np.exp(-0.2 * np.sqrt((x[i]) ** 2 + (x[i + 1]) ** 2))
        f1 = sum
        return f1

    def fun2(x):
        sum = 0
        for i in range(0, len(x)):
            sum = sum + (np.abs(x[i]) ** 0.8 + 5 * (np.sin((x[i]))) ** 3)
        f2 = sum
        return f2

    funcs = [fun2, fun1]

    # Initial input
    # x0 = np.asarray([-1.5216198, 0.0, -1.5216198])
    x_ini = np.asarray([0.0, 0.0, 0.0])
    # x0 = np.asarray([4.0, 4.0, 4.0])

    # Limits
    limits = ([-5, 5], [-5, 5], [-5, 5])

    # Constraints
    constraints = None

    # initial Data set
    ds_ini = [[np.asarray([-1.52161954, -1.52161821, -1.5216178]), 0],
              [np.asarray([-1.00940081e-08,   8.19811851e-09,   5.71849748e-09]), 1]]

    # Jacobian
    jac = None

    # MOO method of updating sections
    moo_options = {'Npar': 50, 'nsample': 4}

    return funcs, x_ini, ds_ini, limits, constraints, jac, moo_options



