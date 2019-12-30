'''
Functions
'''

__author__ = "Matthew Byrne"
__date__ = "11/12/19"

from pymaths.constants.maths import Pi as pi, e

## FACTORIAL ##
def factorial(n):
    if n != 0:
        return n * factorial(n-1)

    else:
        return 1


## FINDING SEVERAL ITEMS IN AN ARRAY ##
def find(a, *terms):
    for term in terms:
        if term in a:
            return a.find(term)
    
    return len(a)


## LOGARITHM ##
def l1(a):
    n = 2**10
    return n*(a**(1/n) - 1)

log = lambda base, x: l1(x)/l1(base)
log2 = lambda x: log(2, x)
log10 = lambda x: log(10, x)
ln = lambda x: log(e, x)

## SIGMA FUNCTION ##
def sigma(Set, expression, term="x"):
    try:
        _ = int(expression[-1])
        thing = False

    except:
        if expression[-1] != term and expression[-1] != ")":
            thing = True
        else:
            thing = False


    expression = expression.replace("^", "**").split(term)
    a = [i for i in expression]
    a.pop()

    for I, i in enumerate(a):
        try:
            _ = int(i[-1])
            expression[I] = i + "*"
        except:
            expression[I] = i

    expression = term.join(expression) + term if thing else term.join(expression)
    total = 0

    for i in Set:
        total += eval(expression.replace(term, str(i)))

    return total
       
def sinr(x): # returns the value of sin given an angle in radians
    return sigma(range(0, 10), f"((-1)**n)/factorial(2n+1) * {x}**(2n+1)", "n")
        
def cosr(x):
    return sigma(range(0, 10), f"((-1)**n)/factorial(2n) * {x}**(2n)", "n")
        
def tanr(x):
    return sinr(x)/cosr(x)

def sin(x):
    a = x * (pi/180)
    return sinr(a)

def cos(x):
    a = x * (pi/180)
    return cosr(x)

def tan(x):
    return sin(x)/cos(x)


