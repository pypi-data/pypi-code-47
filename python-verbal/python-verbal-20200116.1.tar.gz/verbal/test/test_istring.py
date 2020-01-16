
from verbal.istring import istr
from nose.tools import *

def test_simple():
    "simple interpolation"
    a=1
    b="fish"
    c=123.123

    eq_(str(istr("{a}")), "1")
    eq_(str(istr("{b}")), "fish")
    eq_(str(istr("{c}")), "123.123")

def test_yaml():
    a = [1,2,3]
    eq_(str(istr("{a!y}")), "[1, 2, 3]\n")

