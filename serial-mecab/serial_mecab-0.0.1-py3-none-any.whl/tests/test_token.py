"""Tests for token."""
from unittest import TestCase
import serialmecab.token as t


class TestTokens(TestCase):
    """Tests for Tokens."""

    def test_to_primitive(self):
        """return the list of strs."""
        target = t.Tokens([t.Token('a'), t.Token('b')])
        self.assertEqual(target.to_primitive(), ['a', 'b'])

    def test_filter_by(self):
        """Test for filter_by."""
        target = t.Tokens([t.Token('a'), t.Token('b')])

        actual = target.filter_by(lambda token: token == t.Token('a'))
        self.assertEqual(actual, t.Tokens([t.Token('a')]))

    def test_apply_function(self):
        target = t.Tokens([t.Token('a'), t.Token('b')])
        actual = target.apply_function(lambda token: token.token)
        self.assertEqual(actual, ['a', 'b'])
