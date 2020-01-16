from sklearn.cluster import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster
from sklearn.linear_model import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model
from sklearn.naive_bayes import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.naive_bayes
from sklearn.svm import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm
from sklearn.ensemble import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble
from sklearn.discriminant_analysis import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.discriminant_analysis
from sklearn.tree import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree
from sklearn.ensemble import *  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.ensemble
from sklearn import metrics  # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics
from sklearn import model_selection
import mlflow
import os
import numpy as np


def fit(model, x, y=None, **kwargs):
    return model.fit(x, y, **kwargs)


def predict(model, x, **kwargs):
    return model.predict(x, **kwargs)


def train_test_split(x, y, **kwargs):
    return model_selection.train_test_split(x, y, **kwargs)


def log_metric(value, name):
    mlflow.log_metric(name, value)
    return


def log_artifact(path, rm=True):
    mlflow.log_artifact(path)
    if rm:
        os.remove(path)


# descriptive variables
def gini_index(array):
    # all values are treated equally, arrays must be 1d
    array = np.array(array).flatten().astype(float)
    if np.amin(array) < 0:
        array -= np.amin(array)  # values cannot be negative
    array += np.finfo(float).tiny  # values cannot be 0
    array = np.sort(array)  # values must be sorted
    index = np.arange(1, array.shape[0]+1)  # index per array element
    n = array.shape[0]  # number of array elements
    return ((np.sum((2 * index - n - 1) * array)) / (n * np.sum(array)))  # Gini coefficient


# metrics
def accuracy_score(y_true, y_pred, **kwargs):
    out = metrics.accuracy_score(y_true, y_pred, **kwargs)
    log_metric(out, "accuracy")
    return out


def balanced_accuracy_score(y_true, y_pred, **kwargs):
    out = metrics.balanced_accuracy_score(y_true, y_pred, **kwargs)
    log_metric(out, "balanced_accuracy")
    return out


def f1_score(y_true, y_pred, **kwargs):
    out = metrics.f1_score(y_true, y_pred, **kwargs)
    log_metric(out, "F1")
    return out


def fbeta_score(y_true, y_pred, **kwargs):
    out = metrics.fbeta_score(y_true, y_pred, **kwargs)
    log_metric(out, "Fbeta")
    return out


def hamming_loss(y_true, y_pred, **kwargs):
    out = metrics.hamming_loss(y_true, y_pred, **kwargs)
    log_metric(out, "hamming")
    return out


def jaccard_score(y_true, y_pred, **kwargs):
    out = metrics.jaccard_score(y_true, y_pred, **kwargs)
    log_metric(out, "jaccard")
    return out


def log_loss(y_true, y_pred, **kwargs):
    out = metrics.log_loss(y_true, y_pred, **kwargs)
    log_metric(out, "log_loss")
    return out


def matthews_corrcoef(y_true, y_pred, **kwargs):
    out = metrics.matthews_corrcoef(y_true, y_pred, **kwargs)
    log_metric(out, "matthews_corrcoef")
    return out


def precision_score(y_true, y_pred, **kwargs):
    out = metrics.precision_score(y_true, y_pred, **kwargs)
    log_metric(out, "precision")
    return out


def recall_score(y_true, y_pred, **kwargs):
    out = metrics.recall_score(y_true, y_pred, **kwargs)
    log_metric(out, "recall")
    return out


def zero_one_loss(y_true, y_pred, **kwargs):
    out = metrics.zero_one_loss(y_true, y_pred, **kwargs)
    log_metric(out, "zero_one_loss")
    return out


def explained_variance_score(y_true, y_pred, **kwargs):
    out = metrics.explained_variance_score(y_true, y_pred, **kwargs)
    log_metric(out, "explained_variance")
    return out


def max_error(y_true, y_pred, **kwargs):
    out = metrics.max_error(y_true, y_pred, **kwargs)
    log_metric(out, "max_error")
    return out


def mean_absolute_error(y_true, y_pred, **kwargs):
    out = metrics.mean_absolute_error(y_true, y_pred, **kwargs)
    log_metric(out, "mean_absolute_error")
    return out


def mean_square_error(y_true, y_pred, **kwargs):
    out = metrics.mean_square_error(y_true, y_pred, **kwargs)
    log_metric(out, "mean_square_error")
    return out


def mean_square_log_error(y_true, y_pred, **kwargs):
    out = metrics.mean_square_log_error(y_true, y_pred, **kwargs)
    log_metric(out, "mean_square_log_error")
    return out


def median_absolute_error(y_true, y_pred, **kwargs):
    out = metrics.median_absolute_error(y_true, y_pred, **kwargs)
    log_metric(out, "median_absolute_error")
    return out


def r2_score(y_true, y_pred, **kwargs):
    out = metrics.r2_score(y_true, y_pred, **kwargs)
    log_metric(out, "R2")
    return out


def mean_poisson_deviance(y_true, y_pred, **kwargs):
    out = metrics.mean_poisson_deviance(y_true, y_pred, **kwargs)
    log_metric(out, "mean_poisson_deviance")
    return out


def mean_gamma_deviance(y_true, y_pred, **kwargs):
    out = metrics.mean_gamma_deviance(y_true, y_pred, **kwargs)
    log_metric(out, "mean_gamma_deviance")
    return out


def mean_tweedie_deviance(y_true, y_pred, **kwargs):
    out = metrics.mean_tweedie_deviance(y_true, y_pred, **kwargs)
    log_metric(out, "mean_tweedie_deviance")
    return out


def classification_report(y_true, y_pred, **kwargs):
    out = metrics.classification_report(y_true, y_pred, **kwargs)
    with open(f'/tmp/classification_report.txt', 'w') as outfile:
        outfile.writelines(out)
    log_artifact(f'/tmp/classification_report.txt')
    return
