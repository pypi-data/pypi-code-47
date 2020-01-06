#

"""Tests for the ``Runedate`` class."""

from datetime import timedelta

from cresbot.runescape.runedate import Runedate


def test_repr_epoch():
    """
	"""
    expected = "Runedate(runedate=0.00)"
    runedate = Runedate(0)

    assert repr(runedate) == expected


def test_str_epoch():
    """
	"""
    expected = "0.00"
    runedate = Runedate(0)

    assert str(runedate) == expected


def test_from_datetime_epoch():
    """
	"""
    expected = "0.00"
    runedate = Runedate.from_datetime(Runedate.EPOCH)

    assert str(runedate) == expected


def test_to_datetime_epoch():
    """
	"""
    runedate = Runedate(0)
    assert runedate.to_datetime() == Runedate.EPOCH


def test_to_iso8601_epoch():
    """
	"""
    expected = "2002-02-27T00:00:00Z"
    runedate = Runedate(0)

    assert runedate.to_iso8601() == expected


def test_eq_datetime_epoch():
    """
	"""
    runedate = Runedate.from_datetime(Runedate.EPOCH)
    assert runedate == Runedate.EPOCH


def test_lt_datetime_epoch():
    """
	"""
    runedate = Runedate.from_datetime(Runedate.EPOCH)
    assert runedate < (Runedate.EPOCH + timedelta(days=1))


def test_le_datetime_epoch():
    """
	"""
    runedate = Runedate.from_datetime(Runedate.EPOCH)
    assert runedate <= (Runedate.EPOCH + timedelta(days=1))


def test_gt_datetime_epoch():
    """
	"""
    runedate = Runedate.from_datetime(Runedate.EPOCH + timedelta(days=1))
    assert runedate > Runedate.EPOCH


def test_ge_datetime_epoch():
    """
	"""
    runedate = Runedate.from_datetime(Runedate.EPOCH + timedelta(days=1))
    assert runedate >= Runedate.EPOCH
