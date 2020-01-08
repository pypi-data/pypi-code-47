import logging
import pathlib

import numpy as np

from itertools import product
from ..utils import dataset, distances


filename = str(pathlib.Path(__file__ + '/../../tmp.log').resolve())

print("log file: {}".format(filename))
logging.basicConfig(filename=filename,
                    filemode='w',
                    format="%(levelname)s:%(asctime)s:%(name)s: %(message)s \n",
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DB(dataset.DataSet):
    def __init__(self, X, y):
        logger.info("creating DB instance")
        super().__init__(X, y)
        logger.debug("self.X.shape = {} and self.labels.shape = {}".format(self.X.shape, self.labels.shape))

        self.unique_labels = sorted(np.unique(self.labels))
        logger.debug("self.unique_labels = {}".format(self.unique_labels))

        self.K = len(self.unique_labels)
        logger.debug("self.K = {}".format(self.K))

        self.kmu, self.ksigma = self.compute_kmu_ksigma()
        logger.debug("self.kmu = {} \nself.ksigma = {}".format(self.kmu, self.ksigma))

        self.db = None

        self.fit()

    def fit(self):
        logging.info("Starting computation of DB index")

        S = [
            distances.mean_mahalanobis(self.X[self.labels == k],
                                       self.kmu[k],
                                       self.ksigma[k])
            for k in self.unique_labels
        ]
        logging.debug("S = {}".format(S))

        M = np.zeros((self.K, self.K))
        for i, j in product(range(self.K), range(self.K)):
            print("Calling mean mahalanobis with data:\n{}\n".format(self.kmu[j]))
            M[i, j] = (i != j) and distances.mean_mahalanobis(self.kmu[j], self.kmu[i], self.ksigma[i])
        logging.debug("M = {}".format(M))

        R = np.zeros((self.K, self.K))
        for i, j in product(range(self.K), range(self.K)):
            R[i, j] = (i != j) and (S[i] + S[j]) / M[i, j]

        self.db = (1/self.K) * R.max(axis=1, initial=0).sum()

    def compute_kmu_ksigma(self):
        mu = [np.mean(self.X[self.labels == k], axis=0) for k in self.unique_labels]
        sigma = [np.cov(self.X[self.labels == k], rowvar=False) for k in self.unique_labels]

        return mu, sigma
