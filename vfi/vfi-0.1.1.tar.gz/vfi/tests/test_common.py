import pytest

from sklearn.datasets import load_iris
from sklearn.utils.estimator_checks import check_estimator

from vfi import VFI


def test_esimator():
    return check_estimator(VFI)


@pytest.mark.parametrize("n_bins", [1, 3.3, {"foo": 1}, "foo"])
def test_invalid_n_bins(n_bins):
    X, y = load_iris(return_X_y=True)
    model = VFI(n_bins=n_bins)
    error_message = "Valid values are 'auto' or any integer > 1."
    with pytest.raises(ValueError, match=error_message):
        model.fit(X, y)
