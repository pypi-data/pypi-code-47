# Standard Library
None

# Third Party
from pylatex.base_classes import Environment
from pylatex import Math
import sympy as sp

# Local
None

def ProbRational(p, q):
    return sp.Mul(p, sp.Rational(1,q), evaluate=False)

def sympy_tuple(vector):
    entry = map(sp.latex, vector)
    entries = ', '.join(entry)
    tex = f'$\\left({entries} \\right)$'
    return tex

class Array(Environment):
    content_separator = '\n'
    escape = False

class System(Math):

    size = 2

    def __init__(self, K, R, B):
        self.K = K
        self.R = R
        self.B = B

        # Create list of latex symbols for new columns and rows
        new_column = ['&' for i in range(K.rows)]
        new_row = [r'\\' for i in range(K.rows)]
        # Convert the relations to their TeX representaitons
        relmap = {
            "==": "=",
            ">": ">",
            "<": "<",
            ">=": r"\geq",
            "<=": r"\leq",
            "!=": r"\neq",
        }
        relations = [relmap[r.rel_op] for r in R]

        nb_of_vars = K.shape[1]
        if nb_of_vars == 2:
            x, y = sp.symbols('x y')
            X = sp.Matrix([x, y])
        elif nb_of_vars == 3:
            x, y, z = sp.symbols('x y z')
            X = sp.Matrix([x, y, z])
        else:
            raise ValueError(f'Systems with {nb_of_vars} variables is not yet supported.')

        # Create the array environment for the system
        system = Array(arguments='rcr')
        for row in zip(K*X, new_column, relations, new_column, B, new_row):
            statement = ' '.join(map(sp.latex, row))
            system.append(statement)

        super().__init__()
        self.append(system)

    ################################ DELETE BELOW ########## 20200103
"""class SystemTwoEquations(Environment):

    _latex_name = 'array'
    escape = False
    size = 2
    content_separator = '\n'

    def __init__(self, K, B):
        self.K = K
        self.B = B
        super().__init__(arguments='rcr')

        x, y = sp.symbols('x y')
        X = sp.Matrix([x, y])
        temp = K*X
        eqs = [sp.Eq(temp[row], B[row]) for row in range(self.size)]

        for eq in eqs:
            left, right = map(sp.latex, eq.args)
            self.append(f'{left} & = & {right} \\\\')"""

"""class System(Environment):

    _latex_name = 'array'
    escape = False
    size = 2
    content_separator = '\n'

    def __init__(self, K, R, B):
        self.K = K
        self.R = R
        self.B = B
        super().__init__(arguments='rcr')

        # Create list of latex symbols for new columns and rows
        new_column = ['&' for i in range(K.rows)]
        new_row = [r'\\' for i in range(K.rows)]
        # Convert the relations to their TeX representaitons
        relmap = {
            "==": "=",
            ">": ">",
            "<": "<",
            ">=": r"\geq",
            "<=": r"\leq",
            "!=": r"\neq",
        }
        relations = [relmap[r.rel_op] for r in R]

        nb_of_vars = K.shape[1]
        if nb_of_vars == 2:
            x, y = sp.symbols('x y')
            X = sp.Matrix([x, y])
        elif nb_of_vars == 3:
            x, y, z = sp.symbols('x y z')
            X = sp.Matrix([x, y, z])
        else:
            raise ValueError(f'Systems with {nb_of_vars} variables is not yet supported.')

        for row in zip(K*X, new_column, relations, new_column, B, new_row):
            statement = ' '.join(map(sp.latex, row))
            self.append(statement)"""