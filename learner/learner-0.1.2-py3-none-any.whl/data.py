"""Define the Classes for Data"""
import logging
from pathlib import Path

from torch.utils.data import random_split
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST, EMNIST, FashionMNIST
from torchvision.datasets import CIFAR10, CIFAR100

logger = logging.getLogger(__name__)


class Data:
    """Simple Class to wrap the datasets for machine learning tasks"""

    def __init__(self, ds: Dataset,
                 valid_ds: Dataset = None,
                 test_ds: Dataset = None,
                 auto_split: bool = False,
                 split_ratio: float = 0.2,
                 train_dl_kwargs: dict = None,
                 valid_dl_kwargs: dict = None,
                 test_dl_kwargs: dict = None):
        """Use this Class to create a Data instance for leaner to learn

        Args:
            ds (Dataset): a PyTorch Dataset for training and / or validation
            valid_ds (Dataset): a PyTorch Dataset for validation, optional
            test_ds (Dataset): a PyTorch Dataset for testing, optional
            auto_split (bool): if True and `valid_ds` is None, then create a valid set from `ds`
            split_ratio (float): split ratio for the valid set, must between 0 and 1
            train_dl_kwargs (dict): optional arguments for creating train dataloader
            valid_dl_kwargs (dict): optional arguments for creating valid dataloader
            test_dl_kwargs (dict): optional arguments for creating test dataloader
        """
        if auto_split and (valid_ds is None):
            valid_size = int(len(ds) * split_ratio)
            train_size = len(ds) - valid_size
            self._train_ds, self._valid_ds = random_split(ds, [train_size, valid_size])
        else:
            self._train_ds = ds
            self._valid_ds = valid_ds
        self._test_ds = test_ds

        if train_dl_kwargs and ('batch_size' in train_dl_kwargs):
            train_bs = train_dl_kwargs['batch_size']
            _ = train_dl_kwargs.pop('batch_size')
        else:
            train_bs = 8

        if valid_dl_kwargs and ('batch_size' in valid_dl_kwargs):
            valid_bs = valid_dl_kwargs['batch_size']
            _ = valid_dl_kwargs.pop('batch_size')
        else:
            valid_bs = 8

        if test_dl_kwargs and ('batch_size' in test_dl_kwargs):
            test_bs = test_dl_kwargs['batch_size']
            _ = test_dl_kwargs.pop('batch_size')
        else:
            test_bs = 8

        self.train_dl_kwargs = train_dl_kwargs or {}
        self.valid_dl_kwargs = valid_dl_kwargs or {}
        self.test_dl_kwargs = test_dl_kwargs or {}

        self._train_dl = DataLoader(self.train_ds, batch_size=train_bs, **self.train_dl_kwargs)
        self._valid_dl = DataLoader(self.valid_ds, batch_size=valid_bs, **self.valid_dl_kwargs)
        self._test_dl = DataLoader(self.test_ds, batch_size=test_bs, **self.test_dl_kwargs)

        self._datatype = None
        self._datatypes = ('image', 'text', 'tabular')

    def has_valid(self):
        return True if self.valid_ds else False

    def has_test(self):
        return True if self.test_ds else False

    @property
    def train_ds(self):
        return self._train_ds

    @train_ds.setter
    def train_ds(self, ds: Dataset):
        self._train_ds = ds
        self._train_dl = DataLoader(ds, **self.train_dl_kwargs)

    @property
    def valid_ds(self):
        return self._valid_ds

    @valid_ds.setter
    def valid_ds(self, ds: Dataset):
        self._valid_ds = ds
        self._valid_dl = DataLoader(ds, **self.valid_dl_kwargs)

    @property
    def test_ds(self):
        return self._test_ds

    @test_ds.setter
    def test_ds(self, ds: Dataset):
        self._test_ds = ds
        self._test_dl = DataLoader(ds, **self.test_dl_kwargs)

    @property
    def train_dl(self):
        return self._train_dl

    @train_dl.setter
    def train_dl(self, dl: DataLoader):
        self._train_dl = dl
        self._train_ds = dl.dataset

    @property
    def valid_dl(self):
        return self._valid_dl

    @valid_dl.setter
    def valid_dl(self, dl: DataLoader):
        self._valid_dl = dl
        self._valid_ds = dl.dataset

    @property
    def test_dl(self):
        return self._test_dl

    @test_dl.setter
    def test_dl(self, dl):
        self._test_dl = dl
        self._test_ds = dl.dataset

    @property
    def train_bs(self):
        return self.train_dl.batch_size

    @train_bs.setter
    def train_bs(self, batch_size: int):
        self._train_dl = DataLoader(self.train_ds, batch_size=batch_size, **self.train_dl_kwargs)

    @property
    def valid_bs(self):
        return self.valid_dl.batch_size

    @valid_bs.setter
    def valid_bs(self, batch_size: int):
        self._valid_dl = DataLoader(self.valid_ds, batch_size=batch_size, **self.valid_dl_kwargs)

    @property
    def test_bs(self):
        return self.test_dl.batch_size

    @test_bs.setter
    def test_bs(self, batch_size: int):
        self._test_dl = DataLoader(self.test_ds, batch_size=batch_size, **self.test_dl_kwargs)

    @property
    def datatype(self):
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        assert datatype in self._datatypes, f"Support datatypes: {', '.join(self._datatypes)}"
        self._datatype = datatype

    def show(self, n=5):
        assert isinstance(n, int) and (0 < n < 33)
        if self.datatype == 'image':
            pass
        elif self.datatype == 'text':
            pass
        elif self.datatype == 'tabular':
            pass
        else:
            raise ValueError("You must set a valid datatype before calling this method.")

    def __repr__(self):
        train_size = len(self.train_ds)
        valid_size = len(self.valid_ds) if self.has_valid else 0
        test_size = len(self.test_ds) if self.has_test else 0
        size_info = f"Train: {train_size}, Valid: {valid_size}, Test: {test_size}"
        datatype = f"{self.datatype}".title() if self.datatype else ''
        return f"{datatype}{self.__class__.__name__}  {size_info}"

    def __len__(self):
        train_size = len(self.train_ds)
        valid_size = len(self.valid_ds) if self.has_valid else 0
        logging.info(f"Train: {train_size}, Valid: {valid_size}.")
        return train_size + valid_size

    def __getitem__(self, idx):
        return self.train_ds[idx]


def load_mnist(root=None, transform=None, target_transform=None, download=True):
    root = root or Path("~/.learner/dataset").expanduser()
    train_ds = MNIST(root, train=True, download=download, transform=transform, target_transform=target_transform)
    test_ds = MNIST(root, train=False, download=download, transform=transform, target_transform=target_transform)
    data = Data(train_ds, test_ds=test_ds, auto_split=True)
    return data


def load_emnist(split, root=None, transform=None, target_transform=None, download=True):
    root = root or Path("~/.learner/dataset").expanduser()
    train_ds = EMNIST(root=root, split=split, train=True, download=download, transform=transform, target_transform=target_transform)
    test_ds = EMNIST(root=root, split=split, train=False, download=download, transform=transform, target_transform=target_transform)
    data = Data(train_ds, test_ds=test_ds, auto_split=True)
    return data


def load_fmnist(root=None, transform=None, target_transform=None, download=True):
    root = root or Path("~/.learner/dataset").expanduser()
    train_ds = FashionMNIST(root, train=True, download=download, transform=transform, target_transform=target_transform)
    test_ds = FashionMNIST(root, train=False, download=download, transform=transform, target_transform=target_transform)
    data = Data(train_ds, test_ds=test_ds, auto_split=True)
    return data


def load_cifar10(root=None, transform=None, target_transform=None, download=True):
    root = root or Path("~/.learner/dataset").expanduser()
    train_ds = CIFAR10(root, train=True, download=download, transform=transform, target_transform=target_transform)
    test_ds = CIFAR10(root, train=False, download=download, transform=transform, target_transform=target_transform)
    data = Data(train_ds, test_ds=test_ds, auto_split=True)
    return data


def load_cifar100(root=None, transform=None, target_transform=None, download=True):
    root = root or Path("~/.learner/dataset").expanduser()
    train_ds = CIFAR100(root, train=True, download=download, transform=transform, target_transform=target_transform)
    test_ds = CIFAR100(root, train=False, download=download, transform=transform, target_transform=target_transform)
    data = Data(train_ds, test_ds=test_ds, auto_split=True)
    return data
