import unittest
from collections import defaultdict

from .dummy_loader import VeryDumbLoader
from .dummy_loader_multi import DummyTrainTestLoader
from .dummy_loader_multi import DummyTrainValidateTestLoader
from dbispipeline.dataloaders.wrappers import LimitingLoader
from dbispipeline.dataloaders.testing_utils import DataloaderUnitTest


class TestLimitingLoader(DataloaderUnitTest):

    def test_max_both(self):
        loader = LimitingLoader(
                max_targets=7,
                max_documents_per_target=8,
                loader_class=VeryDumbLoader,
                n_samples=500,
                n_classes=20)
        xtrain, ytrain = loader.load()
        self._loader_sanity_check(xtrain, ytrain)

        self.assertLessEqual(len(set(ytrain)), 7)
        self.assertLessEqual(len(xtrain), 7 * 8)
        d = defaultdict(list)
        for x, y in zip(xtrain, ytrain):
            d[y].append(x)
        for key, value in d.items():
            self.assertLessEqual(len(value), 8)

    def test_max_targets(self):
        loader = LimitingLoader(
                max_targets=7,
                max_documents_per_target=None,
                loader_class=VeryDumbLoader,
                n_samples=500,
                n_classes=20)
        xtrain, ytrain = loader.load()
        self._loader_sanity_check(xtrain, ytrain)

        self.assertLessEqual(len(set(ytrain)), 7)

    def test_max_documents(self):
        loader = LimitingLoader(
                max_targets=None,
                max_documents_per_target=8,
                loader_class=VeryDumbLoader,
                n_samples=500,
                n_classes=20)
        xtrain, ytrain = loader.load()
        self._loader_sanity_check(xtrain, ytrain)

        self.assertLessEqual(len(set(ytrain)), 20)
        self.assertLessEqual(len(xtrain), 20 * 8)
        d = defaultdict(list)
        for x, y in zip(xtrain, ytrain):
            d[y].append(x)
        for key, value in d.items():
            self.assertLessEqual(len(value), 8)

    def test_first(self):
        loader = LimitingLoader(
                max_targets=10,
                max_documents_per_target=None,
                strategy='first',
                loader_class=VeryDumbLoader,
                n_samples=500,
                n_classes=10)
        xtrain, ytrain = loader.load()
        self._loader_sanity_check(xtrain, ytrain)
        self.assertEqual(set(ytrain), set([x for x in range(10)]))

    def test_random(self):
        loader = LimitingLoader(
                max_targets=10,
                max_documents_per_target=8,
                strategy='random',
                loader_class=VeryDumbLoader,
                n_samples=500,
                n_classes=20)
        data = loader.load()
        xtrain, ytrain = loader.load()
        self._loader_sanity_check(xtrain, ytrain)
        self.assertNotEqual(set(ytrain), set(range(10)))

    def test_multiloader(self):
        pass

    def test_train_test_loader(self):
        loader = LimitingLoader(
            max_targets=10,
            max_documents_per_target=9,
            strategy='first',
            loader_class=DummyTrainTestLoader)
        train, test = loader.load()
        self._loader_sanity_check(*train, *test)

    def test_train_test_validation_loader(self):
        loader = LimitingLoader(
            max_targets=10,
            max_documents_per_target=9,
            strategy='first',
            loader_class=DummyTrainValidateTestLoader)
        train, validate, test = loader.load()
        self._loader_sanity_check(*train, *validate, *test)

    def test_invalid_max_targets(self):
        loader_arguments = {
            'max_targets': 0,
            'max_documents_per_target': 10,
            'loader': VeryDumbLoader,
            'n_classes': 10,
            'n_samples': 10,
        }
        self.assertRaises(ValueError, LimitingLoader, *loader_arguments)

    def test_invalid_strategy(self):
        loader_arguments = {
            'max_targets': 10,
            'max_documents_per_target': 10,
            'strategy': 'foobar',
            'loader': VeryDumbLoader,
            'n_classes': 10,
            'n_samples': 10,
        }
        self.assertRaises(ValueError, LimitingLoader, *loader_arguments)

    def test_invalid_documents_per_target(self):
        loader_arguments = {
            'max_targets': 10,
            'max_documents_per_target': 0,
            'loader': VeryDumbLoader,
            'n_classes': 10,
            'n_samples': 10,
        }
        self.assertRaises(ValueError, LimitingLoader, *loader_arguments)

