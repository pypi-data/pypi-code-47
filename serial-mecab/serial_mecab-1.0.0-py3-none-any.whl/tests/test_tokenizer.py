"""Tests for tokenizer_mecab."""
from unittest import TestCase
from unittest.mock import patch, call
import tempfile
import os.path
import MeCab
import joblib
import serialmecab.tokenizer as t


class TestMecabTokenizer(TestCase):
    """Tests for MecabTokenizer."""

    def setUp(self):
        self.tokenizer = t.MecabTokenizer(MeCab.Tagger())
        self.tempfile = tempfile.mktemp('mecab_tokenizer')

    def tearDown(self):
        if os.path.exists(self.tempfile):
            os.remove(self.tempfile)

    def test_instance(self):
        """MecabTokenizer extends Tokenizer class."""
        self.assertIsInstance(
            self.tokenizer, t.MecabTokenizer)

    def test_mecab(self):
        """MecabTokenizer uses MeCab for morphological analysis."""
        self.assertIsInstance(
            self.tokenizer.tagger, MeCab.Tagger)

    def test_callable(self):
        """Tokenize a text when it is called as a function."""
        tokens = self.tokenizer(
            '資本主義における覚悟は、破産と失業である')
        self.assertIsInstance(tokens, list)
        for token in tokens:
            self.assertIsInstance(token, str)

    def test_persistent(self):
        """MecabTokenizer is picklable."""
        joblib.dump(self.tokenizer, self.tempfile)

    def test_unpicklable(self):
        """A pickled MecabTokenizer is deserializable."""
        joblib.dump(self.tokenizer, self.tempfile)
        tokenizer = joblib.load(self.tempfile)

        self.assertIsInstance(tokenizer.tagger, MeCab.Tagger)

    def test_create_tagger(self):
        """Create a `MeCab.Tagger` object."""
        self.assertIsInstance(self.tokenizer._create_tagger(),
                              MeCab.Tagger)

    @patch('serialmecab.tokenizer.MecabTokenizer._create_tagger')
    def test_no_arg(self, create_tagger):
        """An argument is optional."""
        tokenizer = self.tokenizer.create()
        self.assertIsInstance(tokenizer, t.MecabTokenizer)
        self.assertEqual(create_tagger.call_args_list, [call()])

    @patch('MeCab.Tagger')
    def test_use_mecab_dicdir(self, tagger):
        """Accept mecab dicdir, and pass it to Mecab.Tagger."""
        pseudo_dicdir = 'path/to/dic/dir'

        self.tokenizer._create_tagger(pseudo_dicdir)

        self.assertEqual(tagger.call_args_list,
                         [call(f'-d {pseudo_dicdir}')])

    @patch('MeCab.Tagger')
    def test_not_use_mecab_dicdir(self, tagger):
        """dicdir is optional."""

        self.tokenizer._create_tagger()

        self.assertEqual(tagger.call_args_list, [call()])
