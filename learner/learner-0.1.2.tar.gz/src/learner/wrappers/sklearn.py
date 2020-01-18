"""Just a wrapper for Scikit-Learn to reduce the clutter
"""
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

from sklearn import __version__

from sklearn import preprocessing
from sklearn import impute
from sklearn import feature_extraction
from sklearn import feature_selection
from sklearn import model_selection
from sklearn import linear_model
from sklearn import svm
from sklearn import tree
from sklearn import ensemble
from sklearn import gaussian_process
from sklearn import cluster
from sklearn import decomposition
from sklearn import manifold
from sklearn import kernel_approximation
from sklearn import kernel_ridge
from sklearn import neural_network
from sklearn import pipeline
from sklearn import metrics
from sklearn import experimental


from sklearn.preprocessing import *
from sklearn.impute import *
from sklearn.feature_extraction import *
from sklearn.feature_selection import *
from sklearn.model_selection import *
from sklearn.linear_model import *
from sklearn.svm import *
from sklearn.tree import *
from sklearn.ensemble import *
from sklearn.gaussian_process import *
from sklearn.neural_network import *
from sklearn.pipeline import *
from sklearn.metrics.classification import *
from sklearn.metrics.pairwise import *
from sklearn.metrics.ranking import *
from sklearn.metrics.regression import *



