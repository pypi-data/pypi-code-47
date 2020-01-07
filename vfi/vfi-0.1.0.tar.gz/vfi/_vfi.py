import numbers

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder, KBinsDiscretizer, normalize
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted


class VFI(BaseEstimator, ClassifierMixin):
    """ Classification by voting feature intervals.

    Intervals are constucted around each class for each attribute
    (basically discretization). Class counts are recorded for each
    interval on each attribute. Classification is by voting.

    Parameters
    ----------
    n_bins : int or array-like, shape (n_features,) (default="auto")
        The number of bins to produce. When is set to 'auto' the n_bins
        equals to the double of the number of classes. Raises ValueError
        if n_bins < 2.

    strategy : {'uniform', 'quantile', 'kmeans'}, (default='quantile')
        Strategy used to define the widths of the bins.

        uniform
            All bins in each feature have identical widths.
        quantile
            All bins in each feature have the same number of points.
        kmeans
            Values in each bin have the same nearest center of a 1D k-means
            cluster.


    Attributes
    ----------
    classes_ : array, shape (n_classes,)
        The classes.

    classes_distribution_ : array, shape (n_classes,)
        The distribution of the classes.

    interval_class_counts_ : array, shape (n_features, n_bins, n_classes,)
        Contains the raw class counts per feature and per bin.

    n_bins_ : int or array-like, shape (n_features,).
        The number of bins used during fit.

    n_classes_ : int
        The number of classes.


    References
    ----------
    .. [1] G. Demiroz, A. Guvenir: Classification by voting feature intervals.
           In: 9th European Conference on Machine Learning, 85-92, 1997.01.

    """

    def __init__(self, n_bins="auto", strategy="uniform"):
        self.n_bins = n_bins
        self.strategy = strategy

    def fit(self, X, y):
        """ Fit VFI according to X, y.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The training input samples.
        y : array-like, shape (n_samples,)
            The target values. An array of int.

        Returns
        -------
        self : object
               Returns self.
        """

        self._validate_params()
        X, y = check_X_y(X, y)
        check_classification_targets(y)

        self._label_encoder = LabelEncoder()
        y_transformed = self._label_encoder.fit_transform(y)
        self.classes_ = self._label_encoder.classes_
        self.n_classes_ = len(self.classes_)
        n_features = X.shape[1]
        self.class_distribution_ = np.bincount(y_transformed, minlength=self.n_classes_)

        self.n_bins_ = self.n_classes_ * 2 if self.n_bins == "auto" else self.n_bins

        discretizer = KBinsDiscretizer(
            n_bins=self.n_bins_, encode="ordinal", strategy=self.strategy
        )
        X_discretized = discretizer.fit_transform(X).astype(np.int32)
        self.interval_class_counts_ = np.zeros(
            (n_features, self.n_bins_, self.n_classes_)
        )

        for i, col in enumerate(X_discretized.T):
            for bin in range(discretizer.n_bins_[i]):
                class_counts = np.bincount(
                    y_transformed[col == bin], minlength=self.n_classes_
                )
                self.interval_class_counts_[i, bin] = class_counts

        self._discretizer = discretizer

        return self

    def predict(self, X):
        """ Perform classification on an array of test vectors X.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y : ndarray, shape (n_samples,)
            The label for each sample is the label of the closest sample
            seen during fit.
        """

        check_is_fitted(self, ["classes_"])
        X = check_array(X)

        predicted_probabilitiy = self.predict_proba(X)
        return self.classes_.take((np.argmax(predicted_probabilitiy, axis=1)), axis=0)

    def predict_proba(self, X):
        """ Return probability estimates for the test vector X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)

        Returns
        -------
        probas : array-like of shape (n_samples, n_classes)
                 Returns the probability of the samples for each class in
                 the model. The columns correspond to the classes in sorted
                 order, as they appear in the attribute :term:`classes_`.
        """

        check_is_fitted(self, ["classes_"])
        X = check_array(X)

        X_discretized = self._discretizer.transform(X).astype(int)
        class_votes = np.zeros((X.shape[0], self.n_classes_))

        for i, col in enumerate(X_discretized.T):
            feature_votes = (
                self.interval_class_counts_[i][col] / self.class_distribution_
            )
            class_votes += normalize(feature_votes, axis=1, norm="l1")

        probas = normalize(class_votes, axis=1, norm="l1")

        return probas

    def _validate_params(self):
        if isinstance(self.n_bins, numbers.Integral) and self.n_bins < 2:
            msg = (
                "{} received an invalid value for parameter 'n_bins'. "
                "Valid values are 'auto' or any integer > 1."
            )
            msg = msg.format(self.__class__.__name__)
            raise ValueError(msg)
