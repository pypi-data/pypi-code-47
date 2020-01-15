"""Test libutil."""
import pytest

from bioplottemplates.libs import libutil

mk_list_test = [
    ('string', ['string']),
    (['string'], ['string']),
    ([1,2,3,4], [1,2,3,4]),
    ]

@pytest.mark.parametrize('input_,expected', mk_list_test)
def test_mk_list(input_, expected):
    assert libutil.make_list(input_, expected)
