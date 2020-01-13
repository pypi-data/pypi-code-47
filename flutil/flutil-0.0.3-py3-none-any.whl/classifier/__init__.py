import pandas as pd
import numpy as np
from typing import Tuple


class Classifier:
    """High-level abstraction of a classifier. The classifier is instantiated
    with a `pd.DataFrame` containing descriptors and labels to train the
    classifier. There are \$m_A\$ training descriptors, each of dimension
    \$n\$. The method `classify` takes in an \$m_B \times n\$ matrix denoting
    \$m_B\$ descriptors of dimension \$n\$ that need to be classified; the
    method returns a `pd.DataFrame` with per descriptor the estimated label
    and the score.
    """

    def __init__(self, train_data: pd.DataFrame, *args, **kwargs):
        """Initialize the classifier with training data.

        :param pd.DataFrame train_data: `pd.DataFrame` with columns
        'descriptor' and 'label'. The 'descriptor' column contains \$m_A\$
        arrays of dimension \$n\$; the 'label' column contains the respective
        labels.
        :param args: args that allow for specific classifier configuration
        :param kwargs: kwargs that allow for specific classifier configuration
        :raises ValueError: if `train_data` does not contain the correct
        columns.
        """
        if ('descriptor' in train_data.columns
                and 'label' in train_data.columns):
            num_labels = len(train_data.groupby('label'))
            if num_labels <= 1:
                raise ValueError('There are not enough labels to classify. '
                                 f'Requires at least 2, got {num_labels}.')
            if any(train_data.descriptor.isna()):
                raise ValueError('DataFrame descriptor column '
                                 'contains NaN values')
            self._train_desc = np.asarray([list(x)
                                           for x in train_data.descriptor])
            self._train_label = train_data.label.values
            self._train_data = train_data
        else:
            raise ValueError('train_data must contain the columns '
                             '"descriptor" and "label"')

    @property
    def train_data(self):
        """The `pd.DataFrame` with which the classifier was initialized."""
        return self._train_data

    def get_score_mat(self,
                      descriptors) -> Tuple[np.array, np.array]:
        """Return a tuple with the score matrix and the labels.

        Each row of the matrix represents a
        descriptor, each column represents a class label. The labels are
        returned as an `np.array` where the index of each label denotes
        its column index in the matrix.

        :param np.array,pd.DataFrame descriptors:
        1. \$m_B\$ by \$n\$ `np.array` containing \$m_B\$ descriptors of
        dimension \$n\$.
        2. `pd.DataFrame` containing a column `descriptor` with \$m_B\$
        rows, each containing a vector of dimension \$n\$.
        :returns: a tuple with the score matrix (shape \$m_B\$ by \$L\$)
        and the labels (shape \$L\$ by 1).
        :rtype: tuple
        """
        if isinstance(descriptors, pd.DataFrame):
            # Check for NaN in descriptors
            if any(descriptors.descriptor.isna()):
                raise ValueError('DataFrame descriptor column '
                                 'contains NaN values')
            desc_mat = np.asarray(list(descriptors
                                       .descriptor
                                       .apply(list)))
        elif isinstance(descriptors, np.ndarray):
            desc_mat = descriptors
        else:
            raise TypeError(f'Unsupported descriptor type {type(descriptors)}')

        # Get the scores and labels
        # This should be implemented by the child class
        score_mat, labels = self._get_score_mat(desc_mat)

        return score_mat, labels

    def _get_score_mat(self,
                       descriptors: np.array) -> Tuple[np.array,
                                                       np.array]:
        """Private implementation for `get_score_mat`.

        This should be implemented by the subclasses.

        :param np.array descriptors: \$m_B\$ by \$n\$ `np.array` containing
        \$m_B\$ descriptors of dimension \$n\$.
        :returns: a tuple with the score matrix and the labels.
        :rtype: tuple
        """
        raise NotImplementedError

    def classify(self, descriptors, show='best',
                 sort_descending=True):
        """Return a `pd.DataFrame` with columns 'descriptor', 'label'
        and 'score'. The 'descriptor' column contains the descriptors passed
        to this method with the `descriptors` argument, the 'label' column
        contains the label closest to the respective descriptor and the
        'score' column contains a score describing how alike the descriptor
        and the label are (higher score means more alike).

        :param np.array,pd.DataFrame descriptors:
        1. \$m_B\$ by \$n\$ `np.array` containing \$m_B\$ descriptors of
        dimension \$n\$.
        2. `pd.DataFrame` containing a column `descriptor` with \$m_B\$
        rows, each containing a vector of dimension \$n\$.
        :param str, int show: which labels and scores to show per descriptor.

        Options are:
        1. 'best': show the label and score for the best match with the
        descriptor;
        2. 'worst': show the label and score for the worst match with the
        descriptor;
        3. 'all': show the labels and scores for all classes, sorted on score
        according to the `sort_descending` argument (note that a class label
        might occur multiple times, depending on the implementation of the
        classifier);
        4. Any positive integer k: show the labels and scores for the best k
        matches with the descriptor, sorted on score according to the
        `sort_descending` argument. If there are less than k matches, the
        labels and scores will have that smaller size as.
        5. Any negative integer k: show the labels and scores for the worst k
        matches with the descriptor, sorted on score according to the
        `sort_descending` argument. If there are less than k matches, the
        labels and scores will have that smaller size as.


        :param bool sort_descending: how to sort the scores and their
        corresponding labels if multiple labels and scores need to be
        shown per descriptor (see `show` argument). If `True`, sort the scores
        from high to low (i.e. from best to worst match); if `False`, sort the
        scores from low to high (i.e. from worst to best match).
        Default: `True`.
        :raises ValueError: if the value of `show` is none of the above
        """
        _scores, _labels = self.get_score_mat(descriptors)
        _idx = np.argsort(_scores, axis=1)

        if show == 'best':
            scores = _scores[np.arange(_scores.shape[0])[:, np.newaxis],
                             _idx[:, -1][:, np.newaxis]]
            labels = _labels[_idx[:, -1][:, np.newaxis]]
        elif show == 'worst':
            scores = _scores[np.arange(_scores.shape[0])[:, np.newaxis],
                             _idx[:, 0][:, np.newaxis]]
            labels = _labels[_idx[:, 0][:, np.newaxis]]
        elif show == 'all':
            scores = _scores[np.arange(_scores.shape[0])[:, np.newaxis],
                             _idx]
            labels = _labels[_idx]
        elif isinstance(show, int) and show > 0:
            scores = _scores[np.arange(_scores.shape[0])[:, np.newaxis],
                             _idx[:, -show:]]
            labels = _labels[_idx[:, -show:]]
        elif isinstance(show, int) and show < 0:
            scores = _scores[np.arange(_scores.shape[0])[:, np.newaxis],
                             _idx[:, :-show]]
            labels = _labels[_idx[:, :-show]]
        else:
            raise ValueError(f'Illegal argument for show: {show}')

        # Scores are sorted from low to high by default (ascending)
        # Flip if user wants descending
        if sort_descending:
            scores = np.fliplr(scores)
            labels = np.fliplr(labels)

        # Show a single score and label if there is only one per query
        # Otherwise, show a list of labels and a list of respective scores
        return pd.DataFrame({'score': [s if len(s) != 1 else s[0]
                                       for s in scores],
                             'label': [l if len(l) != 1 else l[0]
                                       for l in labels]})
