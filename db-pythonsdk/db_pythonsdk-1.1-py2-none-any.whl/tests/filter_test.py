from db_pythonsdk.filter_operators import Eq, Gt, Gte, Lt, Lte 
import pytest


class TestFilters:

    """
    For each command, we test both while expecting the base
    filtering string as well as the logical operation string
    """

    def test_eq(self):
        request = Eq("data_column", "5")
        expected = "data_column=eq.5"
        actual = request.evaluate()
        assert(expected == actual)

        expected ="data_column.eq.5"
        actual = request.evaluate(logical_query=True)
        assert(expected == actual)


    def test_gt(self):
        request = Gt("data_column", "5")
        expected = "data_column=gt.5"
        actual = request.evaluate()
        assert(expected == actual)

        expected ="data_column.gt.5"
        actual = request.evaluate(logical_query=True)
        assert(expected == actual)


    def test_gte(self):
        request = Gte("data_column", "5")
        expected = "data_column=gte.5"
        actual = request.evaluate()
        assert(expected == actual)

        expected ="data_column.gte.5"
        actual = request.evaluate(logical_query=True)
        assert(expected == actual)


    def test_lt(self):
        request = Lt("data_column", "5")
        expected = "data_column=lt.5"
        actual = request.evaluate()
        assert(expected == actual)

        expected ="data_column.lt.5"
        actual = request.evaluate(logical_query=True)
        assert(expected == actual)


    def test_lte(self):
        request = Lte("data_column", "5")
        expected = "data_column=lte.5"
        actual = request.evaluate()
        assert(expected == actual)

        expected ="data_column.lte.5"
        actual = request.evaluate(logical_query=True)
        assert(expected == actual)

