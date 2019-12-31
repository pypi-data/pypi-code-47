from sklearn.utils.estimator_checks import check_estimator

from vfi import VFI


def test_esimator():
    return check_estimator(VFI)
