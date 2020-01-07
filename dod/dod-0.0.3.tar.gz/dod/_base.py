import os
import wget
import logging
import pathlib
import sklearn
import sklearn.datasets

import numpy as np
import pandas as pd
import pickle as pkl


MODULE_PATH = pathlib.Path(__file__).parent

logger = logging.getLogger(__name__)
logging.basicConfig(filename=str(MODULE_PATH / "tmp.log"),
                    filemode='w',
                    format="%(levelname)s:%(asctime)s:%(name)s: %(message)s \n",
                    level=logging.DEBUG)

FILES = {
    'waveform': 'http://archive.ics.uci.edu/ml/machine-learning-databases/waveform/waveform-+noise.data.Z',
    # from page https://datarepository.wolframcloud.com/resources/Sample-Data-Crab-Measures:
    'crabs': 'https://www.wolframcloud.com/objects/17953846-517e-4a70-b656-a1a0ab34d48e',
    'wdbc': 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data',
    'isolet': 'https://archive.ics.uci.edu/ml/machine-learning-databases/isolet/isolet1+2+3+4.data.Z',
    'wine': 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
    'glass': 'https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
}


DATA_DIR = MODULE_PATH / 'data/'
if not DATA_DIR.is_dir():
    logger.info("data directory doesn't exist, creating it")
    os.system("mkdir {}".format(DATA_DIR))


def is_present(file, folder=MODULE_PATH / "data/"):
    return pathlib.Path(folder, file).exists()


def load_iris() -> pd.DataFrame:
    """

    Returns: pandas.Dataframe
        First four columns are the features of the iris dataset:
        - sepal length
        - sepal width
        - petal length
        - petal width
        The labels are in the fifth column

    """

    logger.info("Loading iris dataset")

    # load dataset using sklearn
    feat, labels = sklearn.datasets.load_iris(return_X_y=True)

    # concatenate features and labels in one dataframe
    cols = ["sepal length", "sepal width", "petal length", "petal width", "label"]
    df = pd.DataFrame(np.concatenate((feat, labels.reshape(-1, 1)),
                                     axis=1),
                      columns=cols)
    # labels type: float -> int
    df.label = df.label.astype(int)

    return df


def load_waveform() -> pd.DataFrame:
    logger.info("Loading waveform dataset")

    if is_present("waveform_noise.pkl"):
        logger.info("Found waveform in the data/ directory")
        with open(str(MODULE_PATH / "data/waveform_noise.pkl"), "rb") as f:
            waveform = pkl.load(f)
        return waveform

    logger.info("Did not find waveform in the data/ directory. Downloading dataset.")

    zfilename = wget.download(FILES['waveform'], str(DATA_DIR))

    logger.debug("zfilename = {}".format(zfilename))
    logger.info("unzipping file")

    os.system('gunzip -d {}'.format(zfilename))

    filename = pathlib.Path(zfilename).with_suffix('')
    logger.debug("filename = {}".format(filename))

    waveform = pd.read_csv(filename, header=None, names=[str(i) for i in range(40)] + ['label'])

    with open(str(MODULE_PATH / "data/waveform_noise.pkl"), "wb") as f:
        pkl.dump(waveform, f)

    return waveform
