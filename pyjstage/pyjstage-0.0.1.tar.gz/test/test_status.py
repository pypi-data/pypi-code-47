from status import Status
import errors
from unittest import TestCase


class TestStatus(TestCase):
    def test_ok(self):
        try:
            Status.divide(Status.OK.value, None)
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_no_results(self):
        try:
            Status.divide(Status.NO_RESULTS.value, '')
            self.assertTrue(False)
        except errors.NoResultsError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_too_many_results(self):
        try:
            Status.divide(Status.TOO_MANY_RESULTS.value, '')
            self.assertTrue(False)
        except errors.TooManyResultsError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_too_many_requests(self):
        try:
            Status.divide(Status.TOO_MANY_REQUESTS.value, '')
            self.assertTrue(False)
        except errors.TooManyRequestsError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_invalid_query(self):
        try:
            Status.divide(Status.INVALID_QUERY.value, '')
            self.assertTrue(False)
        except errors.InvalidQueryError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_empty_required_field(self):
        try:
            Status.divide(Status.EMPTY_REQUIRED_FIELD.value, None)
            self.assertTrue(False)
        except errors.EmptyRequiredFieldError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_invalid_year_value(self):
        try:
            Status.divide(Status.INVALID_YEAR_VALUE.value, '')
            self.assertTrue(False)
        except errors.InvalidYearValueError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_invalid_counts(self):
        try:
            Status.divide(Status.INVALID_COUNTS.value, '')
            self.assertTrue(False)
        except errors.InvalidCountsError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_invalid_issn(self):
        try:
            Status.divide(Status.INVALID_ISSN.value, '')
            self.assertTrue(False)
        except errors.InvalidIssnError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_system_fatal(self):
        try:
            Status.divide(Status.SYSTEM_FATAL.value, '')
            self.assertTrue(False)
        except errors.SystemFatalError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_invalid_url(self):
        try:
            Status.divide(Status.INVALID_URL.value, '')
            self.assertTrue(False)
        except errors.InvalidUrlError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_list_no_query(self):
        try:
            Status.divide(Status.LIST_NO_QUERY.value, '')
            self.assertTrue(False)
        except errors.ListNoQueryError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_search_no_query(self):
        try:
            Status.divide(Status.SEARCH_NO_QUERY.value, '')
            self.assertTrue(False)
        except errors.SearchNoQueryError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_list_unspecified(self):
        try:
            Status.divide(Status.LIST_UNSPECIFIED.value, '')
            self.assertTrue(False)
        except errors.ListUnspecifiedError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)

    def test_search_unsortable(self):
        try:
            Status.divide(Status.SEARCH_UNSORTABLE.value, '')
            self.assertTrue(False)
        except errors.SearchUnsortableError:
            self.assertTrue(True)
        except errors.JstageError:
            self.assertTrue(False)
