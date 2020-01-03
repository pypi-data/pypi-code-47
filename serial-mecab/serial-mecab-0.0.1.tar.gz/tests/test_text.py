"""Tests for text."""
from unittest import TestCase
from unittest.mock import MagicMock, call
import serialmecab.text as t
import serialmecab.token as tkn
import serialmecab.tokenizer as tknz


class TestText(TestCase):
    """Tests for Text."""

    def test_concat_concatenation(self):
        """Join with '。' if `text` is not empty."""
        actual = t.Text('a').concat(t.Text('b'))
        self.assertEqual(actual, t.Text('a。b'))

    def test_is_empty_empty_string_true(self):
        """Return true if text is ''."""
        self.assertTrue(t.Text('').is_empty())

    def test_is_empty_false(self):
        """Return true if the length of the text is more than one."""
        self.assertFalse(t.Text('a').is_empty())

    def test_extract_tokens(self):
        """Test for extract_tokens."""
        target = t.Text('none')
        tokens = MagicMock(spec=tkn.Tokens)
        tokenizer = MagicMock(spec=tknz.MecabTokenizer, return_value=tokens)
        expected = MagicMock()
        token_filter = MagicMock()
        tokens.filter_by = MagicMock(return_value=expected)

        actual = target.extract_tokens(tokenizer, token_filter)

        self.assertEqual(tokenizer.call_args_list, [call(target)])
        self.assertEqual(tokens.filter_by.call_args_list,
                         [call(token_filter)])
        self.assertEqual(actual, expected)
