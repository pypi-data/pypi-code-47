from dvk_archive.tests.processing.test_html_processing import test_all as ht_p
from dvk_archive.tests.processing.test_list_processing import test_all as ls_p
from dvk_archive.tests.processing.test_printing import test_all as ts_p
from dvk_archive.tests.processing.test_string_compare import test_all as sc_p
from dvk_archive.tests.processing.test_string_processing import test_all as sp


def test_processing():
    """
    Runs all processing tests.
    """
    ht_p()
    ls_p()
    ts_p()
    sc_p()
    sp()
