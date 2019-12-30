# Simple, slow interpreter of row-wise data. Everything is a data.Instance.

import math
import itertools

import numpy
import matplotlib.pyplot

from . import index, data, parser

# utils


class SymbolTable:
    def __init__(self, parent=None):
        self.parent = parent
        self.table = {}

    def __repr__(self):
        return "<SymbolTable ({0} symbols) {1}>".format(len(self.table), repr(self.parent))

    def get(self, where, line=None, source=None):
        if where in self.table:
            return self.table[where]
        elif self.parent is not None:
            return self.parent[where]
        else:
            raise parser.QueryError("symbol {0} is missing in some or all cases"
                                    "(prepend with '?' symbol name with to ignore)"
                                    .format(repr(where)),
                                    line,
                                    source)

    def __contains__(self, where):
        if where in self.table:
            return True
        elif self.parent is not None:
            return where in self.parent
        else:
            return False

    def __getitem__(self, where):
        return self.get(where)

    def __setitem__(self, where, what):
        self.table[where] = what

    def empty(self):
        return len(self.table) == 0

    def __iter__(self):
        for n in self.table:
            yield n


class Counter:
    def __init__(self, line=None, source=None):
        self.line, self.source = line, source
        self.n = 0
        self.sumw = 0.0
        self.sumw2 = 0.0

    @property
    def entries(self):
        return self.n

    @property
    def value(self):
        return self.sumw

    @property
    def error(self):
        return numpy.sqrt(self.sumw2)

    def __repr__(self):
        return "<{0} {1} ({2} +- {3})>".format(type(self).__name__, self.entries, self.value, self.error)

    def fill(self, w):
        self.n += 1
        self.sumw += w
        self.sumw2 += w**2


class DirectoryCounter(Counter):
    def __init__(self, title=None, line=None, source=None):
        super(DirectoryCounter, self).__init__(line=line, source=source)
        self.title = title
        self.n = 0
        self.sumw = 0.0
        self.sumw2 = 0.0
        self.table = {}

    def iterkeys(self, recursive=False):
        for n, x in self.table.items():
            yield n
            if recursive and isinstance(x, DirectoryCounter):
                for n2 in x.iterkeys(recursive=recursive):
                    yield n + "/" + n2

    def keys(self, recursive=False):
        return list(self.iterkeys(recursive=recursive))

    def allkeys(self):
        return self.keys(recursive=True)

    def __contains__(self, where):
        return where in self.table

    def __getitem__(self, where):
        try:
            i = where.index("/")
        except ValueError:
            return self.table[where]
        else:
            return self.table[where[:i]][where[i + 1:]]

    def __setitem__(self, where, what):
        self.table[where] = what


class Binning:
    pass


class Unspecified(Binning):
    def __repr__(self):
        return "Unspecified()"

    def num(self, data):
        return max(10, 2 * len(data)**(3**-1))

    def range(self, data):
        return None


class Regular(Binning):
    def __init__(self, numbins, low, high):
        self.numbins, self.low, self.high = numbins, low, high

    def __repr__(self):
        return "Regular({0}, {1}, {2})".format(self.numbins, self.low, self.high)

    def num(self, data):
        return self.numbins

    def range(self, data):
        return (self.low, self.high)


class Histogram(Counter):
    def __init__(self, binnings, title, line=None, source=None):
        super(Histogram, self).__init__(line=line, source=source)
        self.binnings, self.title = binnings, title
        self.data = []
        self.weights = []

    def __repr__(self):
        return "<Histogram {0} dim {1} entries>".format(len(self.binnings), len(self.data))

    def fill(self, x, w):
        assert len(x) == len(self.binnings)
        self.n += 1
        self.sumw += w
        self.sumw2 += w**2
        self.data.append(x)
        self.weights.append(w)

    def numpy(self):
        if len(self.binnings) == 1:
            return numpy.histogram(numpy.array(self.data),
                                   bins=self.binnings[0].num(self.data),
                                   range=self.binnings[0].range(self.data),
                                   weights=numpy.array(self.weights).reshape(-1, 1))
        else:
            return numpy.histogramdd(numpy.array(self.data),
                                     bins=[x.num(self.data) for x in self.binnings],
                                     range=[x.range(self.data) for x in self.binnings],
                                     weights=None)  # self.weights)

    def mpl(self):
        if len(self.binnings) == 1:
            counts, edges = self.numpy()
            centers = (edges[:-1] + edges[1:]) / 2.0
            matplotlib.pyplot.step(centers, counts, where="mid")
            matplotlib.pyplot.ylim(min(0, 1.1 * min(counts)), 1.1 * max(counts))
            matplotlib.pyplot.xlim(centers[0], centers[-1])
        else:
            raise NotImplementedError("drawing {0}-dimensional histogram in"
                                      "Matplotlib".format(len(self.binnings)))

# functions


fcns = SymbolTable()

fcns["pi"] = data.ValueInstance(math.pi, None, index.DerivedColKey(parser.Literal(math.pi)))
fcns["e"] = data.ValueInstance(math.e, None, index.DerivedColKey(parser.Literal(math.e)))


class NumericalFunction:
    def __init__(self, name, fcn):
        self.name, self.fcn = name, fcn

    def __call__(self, node, symbols, counter, weight, rowkey):
        args = [runstep(x, symbols, counter, weight, rowkey) for x in node.arguments]
        for x in args:
            if x is None:
                return None
            if not (isinstance(x, data.ValueInstance) and isinstance(x.value, (int, float))):
                raise parser.QueryError("all arguments in {0} must be numbers (not lists or records)".format(self.name), x.line, x.source)

        try:
            result = self.fcn(*[x.value for x in args])
        except Exception as err:
            raise parser.QueryError(str(err), node.line, node.source)

        return data.ValueInstance(result, rowkey, index.DerivedColKey(node))


fcns["+"] = NumericalFunction("addition", lambda x, y: x + y)
fcns["-"] = NumericalFunction("subtraction", lambda x, y: x - y)
fcns["*"] = NumericalFunction("multiplication", lambda x, y: x * y)
fcns["/"] = NumericalFunction("division", lambda x, y: x / float(y))
fcns["%"] = NumericalFunction("modulus", lambda x, y: x % y)
fcns["*1"] = NumericalFunction("identity", lambda x: x)
fcns["*-1"] = NumericalFunction("negation", lambda x: -x)
fcns["**"] = NumericalFunction("exponentiation", lambda x, y: x**y)
fcns[">"] = NumericalFunction("greater-than", lambda x, y: x > y)
fcns[">="] = NumericalFunction("greater-or-equal-to", lambda x, y: x >= y)
fcns["<"] = NumericalFunction("less-than", lambda x, y: x < y)
fcns["<="] = NumericalFunction("less-or-equal-to", lambda x, y: x <= y)
fcns["abs"] = NumericalFunction("abs", abs)
fcns["round"] = NumericalFunction("round", round)
fcns["ceil"] = NumericalFunction("ceil", math.ceil)
fcns["factorial"] = NumericalFunction("factorial", math.factorial)
fcns["floor"] = NumericalFunction("floor", math.floor)
fcns["gcd"] = NumericalFunction("gcd", math.gcd)
fcns["isinf"] = NumericalFunction("isinf", math.isinf)
fcns["isnan"] = NumericalFunction("isnan", math.isnan)
fcns["ldexp"] = NumericalFunction("ldexp", math.ldexp)
fcns["exp"] = NumericalFunction("exp", math.exp)
fcns["expm1"] = NumericalFunction("expm1", math.expm1)
fcns["log"] = NumericalFunction("log", math.log)
fcns["log1p"] = NumericalFunction("log1p", math.log1p)
fcns["log10"] = NumericalFunction("log10", math.log10)
fcns["pow"] = NumericalFunction("pow", math.pow)
fcns["sqrt"] = NumericalFunction("sqrt", math.sqrt)
fcns["arccos"] = NumericalFunction("arccos", math.acos)
fcns["arcsin"] = NumericalFunction("arcsin", math.asin)
fcns["arctan"] = NumericalFunction("arctan", math.atan)
fcns["arctan2"] = NumericalFunction("arctan2", math.atan2)
fcns["cos"] = NumericalFunction("cos", math.cos)
fcns["hypot"] = NumericalFunction("hypot", math.hypot)
fcns["sin"] = NumericalFunction("sin", math.sin)
fcns["tan"] = NumericalFunction("tan", math.tan)
fcns["degrees"] = NumericalFunction("degrees", math.degrees)
fcns["radians"] = NumericalFunction("radians", math.radians)
fcns["arccosh"] = NumericalFunction("arccosh", math.acosh)
fcns["arcsinh"] = NumericalFunction("arcsinh", math.asinh)
fcns["arctanh"] = NumericalFunction("arctanh", math.atanh)
fcns["cosh"] = NumericalFunction("cosh", math.cosh)
fcns["sinh"] = NumericalFunction("sinh", math.sinh)
fcns["tanh"] = NumericalFunction("tanh", math.tanh)
fcns["erf"] = NumericalFunction("erf", math.erf)
fcns["erfc"] = NumericalFunction("erfc", math.erfc)
fcns["gamma"] = NumericalFunction("gamma", math.gamma)
fcns["lgamma"] = NumericalFunction("lgamma", math.lgamma)


class EqualityFunction:
    def __init__(self, negated):
        self.negated = negated

    def evaluate(self, node, left, right):
        if type(left) != type(right):
            out = False

        elif type(left) is data.ValueInstance:
            out = (left.value == right.value)

        elif type(left) is data.ListInstance:
            if len(left.value) == len(right.value):
                if self.negated:
                    for x, y in zip(left.value, right.value):
                        if self.evaluate(node, x, y):
                            return True
                    return False
                else:
                    for x, y in zip(left.value, right.value):
                        if not self.evaluate(node, x, y):
                            return False
                    return True
            else:
                out = False

        elif type(left) is data.RecordInstance:
            if left.row == right.row and set(left.fields()) == set(right.fields()):
                if self.negated:
                    for n in left.fields():
                        if self.evaluate(node, left[n], right[n]):
                            return True
                    return False
                else:
                    for n in left.fields():
                        if not self.evaluate(node, left[n], right[n]):
                            return False
                    return True
            else:
                out = False

        if self.negated:
            return not out
        else:
            return out

    def __call__(self, node, symbols, counter, weight, rowkey):
        args = [runstep(x, symbols, counter, weight, rowkey) for x in node.arguments]
        if any(x is None for x in args):
            return None
        assert len(args) == 2
        assert isinstance(args[0], data.Instance) and isinstance(args[1], data.Instance)
        return data.ValueInstance(self.evaluate(node, args[0], args[1]), rowkey, index.DerivedColKey(node))


fcns["=="] = EqualityFunction(False)
fcns["!="] = EqualityFunction(True)


class InclusionFunction(EqualityFunction):
    def evaluate(self, node, left, right):
        if type(right) != data.ListInstance:
            raise parser.QueryError("value to the right of 'in' must be a list", node.line, node.source)
        if self.negated:
            for x in right.value:
                if not EqualityFunction.evaluate(self, node, left, x):
                    return False
            return True
        else:
            for x in right.value:
                if EqualityFunction.evaluate(self, node, left, x):
                    return True
            return False


fcns[".in"] = InclusionFunction(False)
fcns[".not in"] = InclusionFunction(True)


class BooleanFunction:
    def __call__(self, node, symbols, counter, weight, rowkey):
        def iterate():
            for x in node.arguments:
                arg = runstep(x, symbols, counter, weight, rowkey)
                if arg is None:
                    yield None
                else:
                    if not (isinstance(arg, data.ValueInstance) and isinstance(arg.value, bool)):
                        raise parser.QueryError("arguments of '{0}' must be boolean".format(self.name), arg.line, arg.source)
                    yield arg.value
        result = self.fcn(iterate())
        if result is None:
            return None
        else:
            return data.ValueInstance(result, rowkey, index.DerivedColKey(node))


class NewListFunction:
    def __call__(self, node, symbols, counter, weight, rowkey):
        out = list(filter(None, [runstep(arg, symbols, counter, weight, rowkey) for arg in node.arguments]))
        return data.ListInstance(out, rowkey, index.DerivedColKey(node))


fcns['newlist'] = NewListFunction()

# Three-valued logic
# https://en.wikipedia.org/wiki/Three-valued_logic#Kleene_and_Priest_logics


class AndFunction(BooleanFunction):
    @property
    def name(self):
        return "and"

    def fcn(self, iterate):
        first = next(iterate)
        if first is False:
            return False
        elif first is None:
            second = next(iterate)
            if second is False:
                return False
            else:
                return None
        elif first is True:
            return next(iterate)


class OrFunction(BooleanFunction):
    @property
    def name(self):
        return "or"

    def fcn(self, iterate):
        first = next(iterate)
        if first is False:
            return next(iterate)
        elif first is None:
            second = next(iterate)
            if second is True:
                return True
            else:
                return None
        elif first is True:
            return True


class NotFunction(BooleanFunction):
    @property
    def name(self):
        return "not"

    def fcn(self, iterate):
        first = next(iterate)
        if first is None:
            return None
        else:
            return not first


fcns[".and"] = AndFunction()
fcns[".or"] = OrFunction()
fcns[".not"] = NotFunction()


def ifthenelse(node, symbols, counter, weight, rowkey):
    predicate = runstep(node.arguments[0], symbols, counter, weight, rowkey)
    if predicate is None:
        return None

    if not (isinstance(predicate, data.ValueInstance) and isinstance(predicate.value, bool)):
        raise parser.QueryError("predicte of if/then/else must evaluate to true or false", node.arguments[0].line, node.source)
    if predicate.value:
        return runstep(node.arguments[1], symbols, counter, weight, rowkey)
    elif len(node.arguments) == 2:
        return None
    else:
        return runstep(node.arguments[2], symbols, counter, weight, rowkey)


fcns[".if"] = ifthenelse


class MinMaxFunction:
    def __init__(self, ismin):
        self.ismin = ismin

    def __call__(self, node, symbols, counter, weight, rowkey):
        container = runstep(node.arguments[0], symbols, counter, weight, rowkey)
        if container is None:
            return None

        if not isinstance(container, data.ListInstance):
            raise parser.QueryError("left of '{0}' must be a list"
                                    .format("min by" if self.ismin else "max by"),
                                    node.arguments[0].line,
                                    node.arguments[0].source)

        assert rowkey == container.row
        bestval, bestobj = None, None

        for x in container.value:
            if not isinstance(x, data.RecordInstance):
                raise parser.QueryError("left of '{0}' must contain records"
                                        .format("min by" if self.ismin else "max by"),
                                        node.arguments[0].line,
                                        node.arguments[0].source)

            scope = SymbolTable(symbols)
            for n in x.fields():
                scope[n] = x[n]

            result = runstep(node.arguments[1], scope, counter, weight, x.row)
            if result is not None:
                if isinstance(result, data.ValueInstance) and isinstance(result.value, (int, float)):
                    result = result.value
                else:
                    raise parser.QueryError("right of '{0}' must resolve to a number"
                                            .format("min by" if self.ismin else "max by"),
                                            node.arguments[1].line,
                                            node.arguments[1].source)
                if bestval is None or (self.ismin and result < bestval) or (not self.ismin and result > bestval):
                    bestval = result
                    bestobj = x

        return bestobj   # maybe None (if list is empty or all results are unknown)


fcns[".min"] = MinMaxFunction(True)
fcns[".max"] = MinMaxFunction(False)


def wherefcn(node, symbols, counter, weight, rowkey):
    container = runstep(node.arguments[0], symbols, counter, weight, rowkey)
    if container is None:
        return None

    if not isinstance(container, data.ListInstance):
        raise parser.QueryError("left of 'where' must be a list", node.arguments[0].line, node.arguments[0].source)

    assert rowkey == container.row
    out = data.ListInstance([], rowkey, index.DerivedColKey(node))

    for x in container.value:
        if not isinstance(x, data.RecordInstance):
            raise parser.QueryError("left of 'where' must contain records", node.arguments[0].line, node.arguments[0].source)

        scope = SymbolTable(symbols)
        for n in x.fields():
            scope[n] = x[n]

        result = runstep(node.arguments[1], scope, counter, weight, x.row)
        if result is not None:
            if not (isinstance(result, data.ValueInstance) and isinstance(result.value, bool)):
                raise parser.QueryError("right or 'where' must be boolean", node.arguments[1].line, node.arguments[1].source)
            if result.value:
                out.append(x)

    return out


fcns[".where"] = wherefcn


def groupfcn(node, symbols, counter, weight, rowkey):
    container = runstep(node.arguments[0], symbols, counter, weight, rowkey)
    if container is None:
        return None

    if not isinstance(container, data.ListInstance):
        raise parser.QueryError("left of 'group by' must be a list", node.arguments[0].line, node.arguments[0].source)

    assert rowkey == container.row
    out = data.ListInstance([], rowkey, index.DerivedColKey(node))
    groupindex = index.RowIndex([])   # new, never-before-seen index (two groupbys can't be merged)
    groups = {}

    for x in container.value:
        if not isinstance(x, data.RecordInstance):
            raise parser.QueryError("left of 'group by' must contain records", node.arguments[0].line, node.arguments[0].source)

        scope = SymbolTable(symbols)
        for n in x.fields():
            scope[n] = x[n]

        result = runstep(node.arguments[1], scope, counter, weight, x.row)
        if result is not None:
            if isinstance(result, data.ValueInstance):
                groupkey = result.value
            elif isinstance(result, data.ListInstance):
                groupkey = tuple(sorted(y.row for y in result.value))
            elif isinstance(result, data.RecordInstance):
                groupkey = result.row

            if groupkey not in groups:
                groupindex.array.append(rowkey.index + (len(groups),))
                groups[groupkey] = data.ListInstance([], groupindex[-1], index.DerivedColKey(node))
                out.append(groups[groupkey])

            groups[groupkey].append(x)

    return out


fcns[".group"] = groupfcn


class SetFunction:
    def __call__(self, node, symbols, counter, weight, rowkey):
        left, right = [runstep(x, symbols, counter, weight, rowkey) for x in node.arguments]
        if left is None or right is None:
            return None

        if not isinstance(left, data.ListInstance):
            raise parser.QueryError("left and right of '{0}' must be lists"
                                    .format(self.name),
                                    node.arguments[0].line,
                                    node.arguments[0].source)
        if not isinstance(right, data.ListInstance):
            raise parser.QueryError("left and right of '{0}' must be lists"
                                    .format(self.name),
                                    node.arguments[1].line,
                                    node.arguments[1].source)

        assert rowkey == left.row and rowkey == right.row

        if not all(isinstance(x, data.RecordInstance) for x in left.value):
            raise parser.QueryError("left and right of '{0}' must contain records"
                                    .format(self.name),
                                    node.arguments[0].line,
                                    node.arguments[0].source)
        if not all(isinstance(x, data.RecordInstance) for x in right.value):
            raise parser.QueryError("left and right of '{0}' must contain records"
                                    .format(self.name),
                                    node.arguments[1].line,
                                    node.arguments[1].source)

        out = data.ListInstance([], rowkey, index.DerivedColKey(node))
        self.fill(rowkey, left, right, out, node)
        return out


class CrossFunction(SetFunction):
    name = "cross"

    def fill(self, rowkey, left, right, out, node):
        i = 0
        for x in left.value:
            for y in right.value:
                if not isinstance(x, data.RecordInstance):
                    raise parser.QueryError("left and right of 'cross' must contain records",
                                            node.arguments[0].line,
                                            node.arguments[0].source)
                if not isinstance(y, data.RecordInstance):
                    raise parser.QueryError("left and right of 'cross' must contain records",
                                            node.arguments[1].line,
                                            node.arguments[1].source)

                row = index.RowKey(rowkey.index + (i,), index.CrossRef(x.row.ref, y.row.ref))
                i += 1

                obj = data.RecordInstance({}, row, out.col)
                for n in x.fields():
                    obj[n] = x[n]
                for n in y.fields():
                    if n not in obj:
                        obj[n] = y[n]

                out.append(obj)


fcns[".cross"] = CrossFunction()


class JoinFunction(SetFunction):
    name = "join"

    def fill(self, rowkey, left, right, out, node):
        rights = {x.row: x for x in right.value}

        for x in left.value:
            r = rights.get(x.row)
            if r is not None:
                obj = data.RecordInstance({n: x[n] for n in x.fields()}, x.row, out.col)

                for n in r.fields():
                    if n not in obj:
                        obj[n] = r[n]

                out.append(obj)


fcns[".join"] = JoinFunction()


class UnionFunction(SetFunction):
    name = "union"

    def fill(self, rowkey, left, right, out, node):
        seen = {}

        for x in left.value + right.value:
            if x.row in seen:
                obj = seen[x.row]
            else:
                obj = data.RecordInstance({}, x.row, out.col)

            for n in x.fields():
                if n not in obj:
                    obj[n] = x[n]

            if x.row not in seen:
                seen[x.row] = obj
                out.append(obj)


fcns[".union"] = UnionFunction()


class ExceptFunction(SetFunction):
    name = "except"

    def fill(self, rowkey, left, right, out, node):
        rights = {x.row for x in right.value}

        for x in left.value:
            if x.row not in rights:
                out.append(x)


fcns[".except"] = ExceptFunction()


class ReducerFunction:
    def __init__(self, name, typecheck, identity, fcn):
        self.name, self.typecheck, self.identity, self.fcn = name, typecheck, identity, fcn

    @staticmethod
    def numerical(x):
        "numbers"
        return isinstance(x, data.ValueInstance) and isinstance(x.value, (int, float)) and not isinstance(x.value, bool)

    @staticmethod
    def boolean(x):
        "booleans (true or false)"
        return isinstance(x, data.ValueInstance) and isinstance(x.value, bool)

    def __call__(self, node, symbols, counter, weight, rowkey):
        if len(node.arguments) != 1:
            raise parser.QueryError("reducer function {0} takes exactly one argument".format(repr(self.name)), node.line, node.source)

        arg = runstep(node.arguments[0], symbols, counter, weight, rowkey)
        if arg is None:
            return None

        if not isinstance(arg, data.ListInstance):
            raise parser.QueryError("reducer function {0} must be given a list (not a value or record)"
                                    .format(repr(self.name)),
                                    node.arguments[0].line,
                                    node.source)

        if self.typecheck is not None:
            for x in arg.value:
                if not self.typecheck(x):
                    raise parser.QueryError("reducer function {0} must be given a list of {1}"
                                            .format(repr(self.name), self.typecheck.__doc__),
                                            node.arguments[0].line, node.source)

        if len(arg.value) == 0 and self.identity is None:
            return None
        elif len(arg.value) == 0:
            return data.ValueInstance(self.identity, rowkey, index.DerivedColKey(node))
        else:
            try:
                result = self.fcn([x.value for x in arg.value])
            except Exception as err:
                raise parser.QueryError(str(err), node.line, node.source)
            else:
                return data.ValueInstance(result, rowkey, index.DerivedColKey(node))


fcns["count"] = ReducerFunction("count", None, 0, len)
fcns["sum"] = ReducerFunction("sum", ReducerFunction.numerical, 0, sum)
fcns["min"] = ReducerFunction("min", ReducerFunction.numerical, None, min)
fcns["max"] = ReducerFunction("max", ReducerFunction.numerical, None, max)
fcns["any"] = ReducerFunction("any", ReducerFunction.boolean, False, any)
fcns["all"] = ReducerFunction("all", ReducerFunction.boolean, True, all)

# run


def runstep(node, symbols, counter, weight, rowkey):
    if isinstance(node, parser.Literal):
        return data.ValueInstance(node.value, None, index.DerivedColKey(node))

    elif isinstance(node, parser.Symbol):
        if node.maybe and node.symbol not in symbols:
            return None
        return symbols[node.symbol]

    elif isinstance(node, parser.Block):
        scope = SymbolTable(symbols)
        result = None
        for x in node.body:
            result = runstep(x, scope, counter, weight, rowkey)
        return result

    elif isinstance(node, parser.Call):
        function = runstep(node.function, symbols, counter, weight, rowkey)
        if function is None:
            return None
        if callable(function):
            return function(node, symbols, counter, weight, rowkey)
        else:
            raise parser.QueryError("not a function; cannot be called", node.line, node.source)

    # elif isinstance(node, parser.GetItem):
    #     raise NotImplementedError(node)

    elif isinstance(node, parser.GetAttr):
        obj = runstep(node.object, symbols, counter, weight, rowkey)
        if obj is None:
            return None

        def unwrap(obj):
            if isinstance(obj, data.ListInstance):
                out = data.ListInstance([], obj.row, obj.col)
                for x in obj:
                    out.append(unwrap(x))
                return out

            elif isinstance(obj, data.RecordInstance):
                if node.field not in obj:
                    if node.maybe:
                        return None
                    else:
                        raise parser.QueryError("attribute {0} is missing in some or all"                      "cases (use '?.' instead of '.' to ignore)"
                                                .format(repr(node.field)),
                                                node.object.line,
                                                node.source)
                else:
                    return obj[node.field]

            else:
                raise parser.QueryError("value to the left of '.' (get-attribute) must be a record or a list of records", node.object.line, node.source)

        return unwrap(obj)

    elif isinstance(node, parser.Pack):
        container = runstep(node.container, symbols, counter, weight, rowkey)
        if container is None:
            return None

        if not isinstance(container, data.ListInstance):
            raise parser.QueryError("value to the left of 'as' must be a list", node.container.line, node.source)

        assert rowkey == container.row
        out = data.ListInstance([], rowkey, index.DerivedColKey(node))

        for i, tup in enumerate(itertools.combinations(container.value, len(node.names))):
            row = index.RowKey(rowkey.index + (i,), index.CrossRef.fromtuple(x.row.ref for x in tup))
            obj = data.RecordInstance({}, row, out.col)
            for n, x in zip(node.names, tup):
                obj[n] = x
            out.append(obj)

        return out

    elif isinstance(node, parser.With):
        container = runstep(node.container, symbols, counter, weight, rowkey)
        if container is None:
            return None

        if not isinstance(container, data.ListInstance):
            raise parser.QueryError("value to the left of '{0}' must be a list".format("to" if node.new else "with"), node.container.line, node.source)

        assert rowkey == container.row
        out = data.ListInstance([], rowkey, index.DerivedColKey(node))

        for x in container.value:
            if not isinstance(x, data.RecordInstance):
                raise parser.QueryError("value to the left of 'with' must contain records", node.container.line, node.source)

            if isinstance(node.body, list):
                scope = SymbolTable(symbols)
                for n in x.fields():
                    scope[n] = x[n]

                if node.new:
                    scope = SymbolTable(scope)

                for subnode in node.body:
                    runstep(subnode, scope, counter, weight, x.row)

                out.append(data.RecordInstance({n: scope[n] for n in scope}, x.row, out.col))

            else:
                scope = SymbolTable(symbols)
                for n in x.fields():
                    scope[n] = x[n]

                out.append(runstep(node.body, scope, counter, weight, x.row))

        return out

    elif isinstance(node, parser.Has):
        return data.ValueInstance(all(x in symbols for x in node.names), rowkey, index.DerivedColKey(node))

    elif isinstance(node, parser.Assignment):
        value = runstep(node.expression, symbols, counter, weight, rowkey)
        if value is not None:
            symbols[node.symbol] = value

    elif isinstance(node, parser.Histogram):
        if node.name not in counter:
            binnings = []
            for axis in node.axes:
                if axis.binning is None:
                    binnings.append(Unspecified())

                elif (isinstance(axis.binning, parser.Call) and
                      isinstance(axis.binning.function, parser.Symbol) and axis.binning.function.symbol == "regular" and
                      len(axis.binning.arguments) == 3 and
                      isinstance(axis.binning.arguments[0], parser.Literal) and isinstance(axis.binning.arguments[0].value, int) and
                      isinstance(axis.binning.arguments[1], parser.Literal) and isinstance(axis.binning.arguments[1].value, (int, float)) and
                      isinstance(axis.binning.arguments[2], parser.Literal) and isinstance(axis.binning.arguments[2].value, (int, float))):
                    binnings.append(Regular(axis.binning.arguments[0].value, axis.binning.arguments[1].value, axis.binning.arguments[2].value))

                else:
                    raise parser.QueryError("histogram binning must match one of these patterns: regular(int, float, float)", node.line, node.source)

            if node.titled is None:
                title = None
            else:
                title = runstep(node.titled, symbols, counter, weight, rowkey)
                if title is not None:
                    if isinstance(title, data.ValueInstance) and isinstance(title.value, str):
                        title = title.value
                    else:
                        raise parser.QueryError("histogram title must evaluate to a string", node.titled.line, node.titled.source)

            counter[node.name] = Histogram(binnings, title, line=node.line, source=node.source)

        datum = []
        for axis in node.axes:
            component = runstep(axis.expression, symbols, counter, weight, rowkey)
            if isinstance(component, data.ValueInstance) and isinstance(component.value, (int, float)):
                datum.append(component.value)
            elif component is None:
                datum.append(None)
            else:
                raise parser.QueryError("histograms can only be filled with numbers (not lists of numbers or records)", axis.line, axis.source)

        if node.weight is not None:
            result = runstep(node.weight, symbols, counter, weight, rowkey)
            if result is None:
                weight = 0.0
            elif isinstance(result, data.ValueInstance) and isinstance(result.value, (int, float)):
                weight = weight * result.value
            else:
                raise parser.QueryError("histogram weight must be a number", node.weight.line, node.weight.source)

        if all(x is not None for x in datum):
            counter[node.name].fill(datum, weight)
        elif any(x is not None for x in datum):
            raise parser.QueryError("components must all be missing or none be missing", node.line, node.source)

    elif isinstance(node, parser.Vary):
        outscope = None

        for trial in node.trials:
            scope = SymbolTable(symbols)
            for assignment in trial.assignments:
                runstep(assignment, scope, counter, weight, rowkey)
            if trial.name not in counter:
                counter[trial.name] = DirectoryCounter(line=trial.line, source=trial.source)
            counter[trial.name].fill(weight)

            if outscope is None:
                scope = outscope = SymbolTable(scope)
            for x in node.body:
                runstep(x, scope, counter[trial.name], weight, rowkey)

        if outscope is not None:
            for n in outscope:
                symbols[n] = outscope[n]

    elif isinstance(node, parser.Cut):
        if node.name not in counter:
            if node.titled is None:
                title = None
            else:
                title = runstep(node.titled, symbols, counter, weight, rowkey)
                if title is not None:
                    if isinstance(title, data.ValueInstance) and isinstance(title.value, str):
                        title = title.value
                    else:
                        raise parser.QueryError("cut title must evaluate to a string", node.titled.line, node.titled.source)
            counter[node.name] = DirectoryCounter(title, line=node.line, source=node.source)

        result = runstep(node.expression, symbols, counter, weight, rowkey)
        if result is None:
            return None

        if not (isinstance(result, data.ValueInstance) and isinstance(result.value, bool)):
            raise parser.QueryError("cut expression must evaluate to true or false", node.expression.line, node.expression.source)
        if result.value is False:
            return None

        if node.weight is not None:
            result = runstep(node.weight, symbols, counter, weight, rowkey)
            if result is None:
                return None
            if not (isinstance(result, data.ValueInstance) and isinstance(result.value, (int, float))):
                raise parser.QueryError("cut weight must evaluate to a number", node.weight.line, node.weight.source)
            weight = weight * result.value

        counter[node.name].fill(weight)

        for x in node.body:
            runstep(x, symbols, counter[node.name], weight, rowkey)

    else:
        assert False, repr(type(node), node)


def run(source, dataset):
    if not isinstance(source, parser.AST):
        source = parser.parse(source)

    output = dataset.newempty()
    counter = DirectoryCounter()
    for entry in dataset:
        if not isinstance(entry, data.RecordInstance):
            raise parser.QueryError("entries must be records (outermost array structure must be RecordArray)")

        original = SymbolTable(fcns)
        for n in entry.fields():
            original[n] = entry[n]
        modified = SymbolTable(original)

        counter.fill(1.0)
        for node in source:
            runstep(node, modified, counter, 1.0, entry.row)

        if not modified.empty():
            out = entry.newempty()
            for n in modified:
                out[n] = modified[n]
            output.append(out)

    return output, counter
