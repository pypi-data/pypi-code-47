from db_pythonsdk.filter_operators import Eq, Gt, Gte, Lt, Lte 
from db_pythonsdk.logical_operators import And, Or, Not 
import pytest


class TestLogic:

    """ 
    For each command we test both a regular and nested 
    version of the logical command. For instance, we may
    have an And statement nested within another And statement
    """

    eqr = Eq("data", "1")
    gtr = Gt("data", "5")
    gter = Gte("data", "5")
    ltr = Lt("data", "10")
    lter = Lte("data", "10")

    def test_and(self):
        queries = [self.gtr, self.ltr]
        request = And(queries)
        expected = "and=(data.gt.5, data.lt.10)"
        actual = request.evaluate()
        assert(expected == actual)

    def test_and_nested(self):
        queries = [self.gter, self.eqr, And([self.eqr, self.ltr])]
        request = And(queries)
        expected = "and=(data.gte.5, data.eq.1, and(data.eq.1, data.lt.10))"
        actual = request.evaluate()
        assert(expected == actual)
    
    def test_or(self):
        queries = [self.gter, self.ltr, self.eqr]
        request = Or(queries)
        expected = "or=(data.gte.5, data.lt.10, data.eq.1)"
        actual = request.evaluate()
        assert(expected == actual)

    def test_or_nested(self):
        queries = [self.gter, Or([self.eqr, self.ltr])]
        request = Or(queries)
        expected = "or=(data.gte.5, or(data.eq.1, data.lt.10))"
        actual = request.evaluate()
        assert(expected == actual)
    
    def test_not(self):
        request = Not(self.gter)
        expected = "data=not.gte.5"
        actual = request.evaluate()
        assert(expected == actual)

        queries  = self.lter, self.gtr
        request = Not(And(queries))
        expected = "not.and=(data.lte.10, data.gt.5)"
        actual = request.evaluate()
        assert(expected == actual)

    def test_not_nested(self):
        request = Not(And([self.lter, Not(self.eqr)]))
        expected = "not.and=(data.lte.10, data=not.eq.1)"
        actual = request.evaluate()
        assert(expected == actual)