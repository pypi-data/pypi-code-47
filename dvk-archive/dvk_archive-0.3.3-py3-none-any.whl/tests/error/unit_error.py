from dvk_archive.tests.error.test_missing_media import TestMissingMedia
from dvk_archive.tests.error.test_same_ids import TestSameIDs
from dvk_archive.tests.error.test_unlinked import TestUnlinkedMedia


def test_error():
    """
    Runs all error tests.
    """
    same_ids = TestSameIDs()
    unlinked = TestUnlinkedMedia()
    missing_media = TestMissingMedia()
    same_ids.test_all()
    unlinked.test_all()
    missing_media.test_all()
