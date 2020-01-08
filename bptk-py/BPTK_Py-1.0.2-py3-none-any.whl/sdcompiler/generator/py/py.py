#                                                       /`-
# _                                  _   _             /####`-
# | |                                | | (_)           /########`-
# | |_ _ __ __ _ _ __  ___  ___ _ __ | |_ _ ___       /###########`-
# | __| '__/ _` | '_ \/ __|/ _ \ '_ \| __| / __|   ____ -###########/
# | |_| | | (_| | | | \__ \  __/ | | | |_| \__ \  |    | `-#######/
# \__|_|  \__,_|_| |_|___/\___|_| |_|\__|_|___/  |____|    `- # /
#
# Copyright (c) 2019 transentis labs GmbH
# MIT License


import re


from ..contextBuilder import remove_nesting


def generate(IR):
    """
    The generator for python. Hands over the template and parseExpression function to the generic generator

    :param IR:
    :return:
    """
    from .jinja_template import template
    from ..contextBuilder import generate
    return generate(IR, template=template, parseExpression=parseExpression)


def parseExpression(expression):
    '''
    Parse expression / equation recursively and build code from IR (For python). You need to re-implement the return statements for getting it work for another target language
    :param expression:
    :return:
    '''
    lowercase_first_letter = lambda s: s[:1].lower() + s[1:] if s else ''

    '''
    Just make sure to lowercase module name
    '''
    if type(expression) is dict and expression["type"] == "identifier":
        expression["name"] = lowercase_first_letter(expression["name"])

    '''
    Remove "," from expression
    '''
    if not type(expression) is int and not type(expression) is float:
        if type(expression) is list or type(expression) is tuple:
            if "," in expression: expression.remove(",")

    '''
    Return if float or int
    '''
    if type(expression) is float or type(expression) is int:
        return expression

    '''
    Return if str
    '''
    if type(expression) is str:
        return expression

    '''
    Parse list (e.g. args) by joining parsing results for each element in list
    '''
    if type(expression) is list or type(expression) is tuple:
        result = []
        for elem in expression:
            result += [parseExpression(elem)]
            if len(result) == 0:
                return 0

        return ",".join([str(x) for x in result if str(x).replace(" ", "") != ","])

    '''
    Handle Identifiers
    '''
    if expression["type"] == 'identifier':
        return "self.memoize(\'{}\', t)".format(expression["name"])

    '''
    Handle Function Calls
    '''
    if expression["type"] == 'call':
        try:
            macro = builtins[expression["name"].lower()]
            return macro(expression["args"])
        except TypeError as e:
            print(expression)
            raise e
        except KeyError as e:

            raise e
            print(expression["name"].lower() + " has not been implemented yet! Skipping...")
            return "0"

    '''
    Handle Operators
    '''
    if expression["type"] == 'operator':
        try:
            conv = operators[expression["name"].lower().replace(" ", "")]

            # Some operators have 2 args (+,-,/), some only one (exp)
            try:
                return conv(expression["args"][0], expression["args"][1])
            except IndexError as e:
                return conv(expression["args"][0])

        except KeyError:
            raise Exception('Unknown Operator: {}'.format(expression))

    '''
    Array functions
    '''
    if expression["type"] == 'array':
        def array(name, args):

            vargs = []

            if type(args) is dict:
                args = [args]

            for elem in args:

                if "self.memoize" in elem:

                    vargs += ["\'+ " + parseExpression(elem) + "+\'"]
                else:
                    if type(elem) is dict:
                        elem = [elem]

                    if type(elem) is list and type(elem[0]) is dict and elem[0]["type"] == "call":
                        vargs += ["\'+ str(" + parseExpression(elem) + ")+\'"]
                    else:
                        vargs += [elem]

            return "self.memoize(\'{}[".format(name) + ",".join([str(parseExpression(x)) for x in vargs]) + "]\', t)"

        return str(array(expression["name"], expression["args"]))

    '''
    Comment
    '''
    if expression["type"] == 'comment':
        return "# " + str(" ".join(expression["args"]))

    '''
    Constants
    '''
    if expression["type"] == 'constant':
        return str(expression)

    '''
    Labels
    '''
    if expression["type"] == 'label':
        return expression["name"]

    '''
    Nothing
    '''
    if expression["type"].replace(" ", "") == '()':
        return 0

    raise Exception("Cannot parse expression: {}".format(expression))


'''
Lambdas for operators
'''
operators = {
    "+": lambda lhs, rhs: "{} + {}".format(parseExpression(lhs), parseExpression(rhs)),
    "-": lambda lhs, rhs: "{} - {}".format(parseExpression(lhs), parseExpression(rhs)),
    "*": lambda lhs, rhs: "{} * {}".format(parseExpression(lhs), parseExpression(rhs)),
    "/": lambda lhs, rhs: "{} / {}".format(parseExpression(lhs), parseExpression(rhs)),
    "^": lambda lhs, rhs: "{} ** {}".format(parseExpression(lhs), parseExpression(rhs)),
    "=": lambda lhs, rhs: "{} == {}".format(parseExpression(lhs), parseExpression(rhs)),
    ">": lambda lhs, rhs: "{} > {}".format(parseExpression(lhs), parseExpression(rhs)),
    "<": lambda lhs, rhs: "{} < {}".format(parseExpression(lhs), parseExpression(rhs)),
    ">=": lambda lhs, rhs: "{} >= {}".format(parseExpression(lhs), parseExpression(rhs)),
    "<=": lambda lhs, rhs: "{} <= {}".format(parseExpression(lhs), parseExpression(rhs)),
    "<>": lambda lhs, rhs: "{} != {}".format(parseExpression(lhs), parseExpression(rhs)),
    "mod": lambda lhs, rhs: "{} % {}".format(parseExpression(lhs), parseExpression(rhs)),
    "()": lambda body: "( {} )".format(parseExpression(body)),
    "and": lambda lhs, rhs: "{} and {}".format(parseExpression(lhs), parseExpression(rhs)),
    "or": lambda lhs, rhs: "{} or {}".format(parseExpression(lhs), parseExpression(rhs)),
    "exp": lambda body: "np.exp( {} )".format(parseExpression(body)),
}


def pulse(*args):
    args = remove_nesting(args)
    volume = parseExpression(args[0]) if type(parseExpression(args[0])) is str else parseExpression(args[0])[0]

    first = None if len(args) == 1 else args[1][1]

    interval = None if len(args) == 1 else args[2][1]

    if first == interval == None:
        return '( ' + str(volume) + ' ) / self.dt'

    if first == None:
        first = ' self.starttime '

    if interval == None:
        return str(volume) + ' /self.dt if ' + str(first) + ' <= t else 0'

    if int(interval) == 0:
        return str(volume) + ' /self.dt if ' + str(first) + ' == t else 0'

    return str(volume) + '/ self.dt if ' + str(first) + ' <= t and ((t -' + str(first) + ') % ' + str(
        interval) + ') == 0 else 0'


def previous(args):

    res = parseExpression(args)

    body = res

    initial = None if (not type(res) is list) else res[1]
    pattern_selfdt = r"\(?\,?(self.[dt+\-]+)\)"
    body = re.sub(pattern_selfdt, "(self.dt-self.dt)", str(body))

    pattern_t = r"\(?\,? ([t+\-]+)\)"
    body = re.sub(pattern_t, ",t-self.dt)", body)

    if initial:

        return '(' + str(initial) + ') if t <= self.starttime else ' + '(' + str(body) + ')' if initial else str(body)
    else:

        return str(body)


def delay(*args):
    args = remove_nesting(args)
    input = str(parseExpression(args[0]))
    offset = str(parseExpression(args[1]))
    initial = str(parseExpression(args[2]))

    pattern = r"(^|[^a-zA-Z_\\.])t($|[^a-zA-Z_\\.])"
    clean = re.compile(pattern)

    tDelayed = re.sub(clean, r'\1( t - (' + str(offset) + r') )\2', input)

    return tDelayed if not initial else "self.delay( {},{},{},t)".format(tDelayed,offset,initial)


def if_(expression):
    condition = parseExpression(expression[0])
    then = parseExpression(expression[1])
    if type(then) is list and len(then) > 0: then = then[0]

    if then == "":
        then = "0"
    otherwise = parseExpression(expression[2])

    return '( (' + str(then) + ') if (' + str(condition) + ') else (' + str(otherwise) + ') )'

def sum_(*args):
    args = remove_nesting(args)
    if len(args) > 1:
        return 'sum([' + " , ".join([str(parseExpression(x)) for x in remove_nesting(args) if x != "," or x != ", "]) + '])'
    return 'sum(' + " , ".join([str(parseExpression(x)) for x in remove_nesting(args) if x != "," or x != ", "]) + ')'



def min_(*args):
    args = remove_nesting(args)
    if len(args) > 1:
        return 'min([' + " , ".join([str(parseExpression(x)) for x in remove_nesting(args) if x != "," or x != ", "]) + '])'
    return 'min(' + " , ".join([str(parseExpression(x)) for x in remove_nesting(args) if x != "," or x != ", "]) + ')'


def max_(*args):
    args = remove_nesting(args)
    if len(args) > 1:
        return 'max([' + " , ".join([str(parseExpression(x)) for x in remove_nesting(args) if x != "," or x != ", "]) + '])'
    else:
        return 'max( ' + " , ".join([str(parseExpression(x)) for x in remove_nesting(args) if x != "," or x != ", "]) + ')'

def size_(*args):
    args = remove_nesting(args)
    if type(args) is float or type(args) is int:
        return args

    if type(args) is dict:
        args = [args]

    if type(args) is list:
        if len(args) == 1:
            return "len( " + parseExpression(args[0]) + ")"
        else:
            return 'len([' + " , ".join([str(parseExpression(x)) for x in args]) + '])'


def mean_(*args):
    args = remove_nesting(args)
    if len(args) > 1:
        return 'np.mean([' + " , ".join([str(parseExpression(x)) for x in args]) + '])'
    else:
        return 'np.mean(' + " , ".join([str(parseExpression(x)) for x in args]) + ')'

def prod_(*args):
    args = remove_nesting(args)
    if len(args) > 1:
        return 'np.product([' + "+".join([str(parseExpression(x)) for x in args]) + '])'
    return 'np.product(' + " , ".join([str(parseExpression(x)) for x in args]) + ')'


def random_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    min = args[0] if type(args[0]) is str or type(args[0]) is float else args[0][0]
    max = args[1] if type(args[1]) is str or type(args[1]) is float else args[1][0]

    if len(args) > 2:
        seed = args[2] if type(args[2]) is str or type(args[2]) is float else args[2][0]
        return '(random_with_seed({}) * (('.format(seed) + str(max) + ') - (' + str(min) + ')) + (' + str(min) + '))'

    return '(random.random() * ((' + str(max) + ') - (' + str(min) + ')) + (' + str(min) + '))'

def beta_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    a = parseExpression(args[0])
    b = parseExpression(args[1])

    if len(args) > 2:
        seed = args[2]
        return 'beta_with_seed({},{},{})'.format(a,b,seed)

    return 'np.random.beta({},{})'.format(a,b)

def combinations_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    n = parseExpression(args[0])
    r = parseExpression(args[1])

    return '(math.factorial({}) / (math.factorial({}) * math.factorial({}-{})))'.format(n,r,n,r)

def binomial_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    n = parseExpression(args[0])
    p = parseExpression(args[1])

    if len(args) > 2:
        seed = args[2]
        return 'binomial_with_seed({},{},{})'.format(n,p,seed)

    return 'np.random.binomial({},{})'.format(n,p)

def exprnd_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    lambda_ = parseExpression(args[0])


    if len(args) == 2:
        seed = args[1]
        return 'exprnd_with_seed({},{})'.format(lambda_,seed)

    return 'np.random.exponential({})'.format(lambda_)

def gamma_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    shape = parseExpression(args[0])

    if (len(args) == 2):
        scale = parseExpression(args[1])
        return 'np.random.gamma({},{})'.format(shape, scale)

    if len(args) > 2:
        scale = parseExpression(args[1])
        seed = args[2]
        return 'gamma_with_seed({},{},{})'.format(shape,scale,seed)

    return 'np.random.gamma({})'.format(shape)

def geometric_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    p = parseExpression(args[0])

    if len(args) == 2:
        seed = args[1]
        return 'geometric_with_seed({},{})'.format(p,seed)

    return 'np.random.geometric({})'.format(p)

def normal_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass
    mean = args[0] if type(args[0]) is str or type(args[0]) is float else args[0][0]
    dev = args[1] if type(args[1]) is str or type(args[1]) is float else args[1][0]

    if len(args) > 2:
        seed = args[2] if type(args[2]) is str or type(args[2]) is float else args[2][0]
        return ' ((( math.sqrt( -2 * math.log( random_with_seed({}) ) ) * math.cos( 2 * math.pi * random_with_seed({}) )) * ('.format(
            seed, seed) + str(
            dev) + ')) + (' + str(mean) + '))'

    return ' ((( math.sqrt( -2 * math.log( random.random() ) ) * math.cos( 2 * math.pi * random.random() )) * (' + str(
        dev) + ')) + (' + str(mean) + '))'

def gammaln_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass
    if len(args) > 1:
        print("GAMMALM only supported with one argument. Skipping all other arguments")

    x = parseExpression(args[0])

    return 'gammaln({})'.format(x)

def factorial_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass
    n = parseExpression(args[0])
    return "math.factorial({})".format(n)

def step_(*args):
    args = remove_nesting(args)
    for elem in args:
        try:
            elem.remove(",")
        except:
            pass
    height = parseExpression(args[0])
    time = parseExpression(args[1])

    return "(0 if t < " + str(time) + " else " + str(height) + ")"

def rank_(*args):
    args = remove_nesting(args)

    for elem in args:
        try:
            elem.remove(",")
        except:
            pass

    rank = remove_nesting(args[-1])
    if (type(rank)) is list:
        for elem in rank:
            try:
                elem.remove(",")
            except:
                pass

    rank = parseExpression(rank)
    if len(args) > 2:
        return "self.rank([" + ",".join(parseExpression(arg) for arg in args[:-1]) + "], " + str(rank) + ")"

    return "self.rank(" + ",".join(parseExpression(arg) for arg in args[:-1]) + ", " + str(rank) + ")"


builtins = {

    # Simulation Buildins
    'dt': lambda *args: 'self.dt',
    'starttime': lambda *args: ' self.starttime ',
    'stoptime': lambda *args: ' self.stoptime ',
    'time': lambda *args: ' t ',
    'pi': lambda *args: ' math.pi ',

    # Array builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Array_builtins.htm
    'size': lambda *args: size_(args) ,

    'stddev': lambda *args: 'np.std(' + ','.join([str(parseExpression(x)) for x in args]) + ')',

    'sum': lambda *args: 'np.sum(' + "+".join([str(parseExpression(x)) for x in args]) + ')',

    'mean': lambda *args: mean_(args),

    'rank': lambda *args : rank_(args),

    # Data builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Data_builtins.htm
    'previous': lambda args: previous(args),

    # Mathematical builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Mathematical_builtins.htm
    'abs': lambda body: 'abs( ' + str(body) + ' )',

    'max': lambda *args: max_(args),

    'min': lambda *args: min_(args),

    'prod': lambda *args: prod_(args),

    'int': lambda body: 'math.floor( ' + body + ' )',

    'sin': lambda body: 'math.sin(' + body + ' )',

    'cos': lambda body: 'math.cos(' + body + ')',

    'tan': lambda body: 'math.tan(' + body + ')',

    'round': lambda body: 'round(' + body + ')',

    'arccos' : lambda body: 'np.arccos(' + body + ')',

    'arcsin' : lambda body: 'np.arcsin(' + body + ')',

    'arctan': lambda body: 'np.arctan(' + body + ')',

    'savediv': lambda nominator, denominator, onzero: '0' if onzero is None else str(
        onzero) + ' if ' + denominator + ' == 0 else ' + nominator + ' / ' + denominator,

    'step': lambda *args: step_(args),

    # Logical builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Logical_builtins.htm
    'if': lambda expression: if_(expression),
    # then, condition, otherwise :  '( (' + then + ') if (' + condition + ') else (' + otherwise + ') )',

    # Delay builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Delay_builtins.htm
    'delay': lambda *args: delay(args),

    'exp': operators['exp'],

    # Data builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Data_builtins.htm
    'init': lambda args: parseExpression(args).replace(", t", ", self.starttime"),

    # Statistical builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Statisticall_builtins.htm
    'normal': lambda *args: normal_(args),
    # lambda mean, dev, seed:  ' ((( math.sqrt( -2 * math.log( random.random() ) ) * math.cos( 2 * math.pi * random.random() )) * (' + str(dev) + ')) + (' + str(mean) + '))',

    'random': lambda *args: random_(args),

    'beta': lambda *args : beta_(args),

    'binomial' : lambda *args : binomial_(args),

    'combinations' : lambda *args: combinations_(args),

    'gamma' : lambda *args: gamma_(args),

    'factorial': lambda *args: factorial_(args),

    'exprnd' : lambda *args : exprnd_(args),

    'gammaln' : lambda *args : gammaln_(args),

    'geometric' : lambda *args : geometric_(args),

    # Test input builtins
    # http://www.iseesystems.com/Helpv10/Content/Reference/Builtins/Test_input_builtins.htm
    'pulse': lambda *args: pulse(*args)

}
