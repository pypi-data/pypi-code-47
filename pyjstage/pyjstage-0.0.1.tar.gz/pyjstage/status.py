import errors
from typing import Optional
from enum import Enum


class Status(Enum):
    """Enum for Status

    Status.OK: No Error
    Status.NO_RESULTS: No results found
    Status.TOO_MANY_RESULTS: Too many results found
    Status.TOO_MANY_REQUESTS: Too many requests were occurred
    Status.INVALID_QUERY: Query is invalid
    Status.EMPTY_REQUIRED_FIELD: Any of required fields were not filled
    Status.INVALID_YEAR_VALUE: Year value is invalid
    Status.INVALID_COUNTS: Count value is invalid
    Status.INVALID_ISSN: ISSN format is invalid.
    Status.SYSTEM_FATAL: Fatal error has been occurred.
    Status.INVALID_URL: URL is invalid
    Status.LIST_NO_QUERY: Any of required queries were not sent.
    Status.SEARCH_NO_QUERY: Any of required queries were not sent.
    Status.LIST_UNSPECIFIED: Cannot specify result.
    Status.SEARCH_UNSORTABLE: Cannot sort result.
    """
    OK = '0'
    NO_RESULTS = 'ERR_001'
    TOO_MANY_RESULTS = 'WARN_002'
    TOO_MANY_REQUESTS = 'ERR_003'
    INVALID_QUERY = 'ERR_004'
    EMPTY_REQUIRED_FIELD = 'ERR_005'
    INVALID_YEAR_VALUE = 'ERR_006'
    INVALID_COUNTS = 'ERR_007'
    INVALID_ISSN = 'ERR_008'
    SYSTEM_FATAL = 'SYS_ERR_009'
    INVALID_URL = 'ERR_010'
    LIST_NO_QUERY = 'ERR_011'
    SEARCH_NO_QUERY = 'ERR_012'
    LIST_UNSPECIFIED = 'ERR_013'
    SEARCH_UNSORTABLE = 'ERR_014'

    @staticmethod
    def divide(status: str, message: Optional[str]):
        """Divide status and raise Error or Warning if necessary.

        Args:
            status: status code J-STAGE API returned
            message: message J-STAGE API returned
        Raises:
            JstageError: error depending on j-stage api
            JstageWarning: warning depending on j-stage api
        """
        if status == Status.OK.value:
            pass
        elif status == Status.NO_RESULTS.value:
            raise errors.NoResultsError(message)
        elif status == Status.TOO_MANY_RESULTS.value:
            raise errors.TooManyResultsError(message)
        elif status == Status.TOO_MANY_REQUESTS.value:
            raise errors.TooManyRequestsError(message)
        elif status == Status.INVALID_QUERY.value:
            raise errors.InvalidQueryError(f'{message} invalid.')
        elif status == Status.EMPTY_REQUIRED_FIELD.value:
            raise errors.EmptyRequiredFieldError(f'{message} required.')
        elif status == Status.INVALID_YEAR_VALUE.value:
            raise errors.InvalidYearValueError(f'{message} invalid.')
        elif status == Status.INVALID_COUNTS.value:
            raise errors.InvalidCountsError(f'{message} invalid')
        elif status == Status.INVALID_ISSN.value:
            raise errors.InvalidIssnError(f'{message} invalid')
        elif status == Status.SYSTEM_FATAL.value:
            raise errors.SystemFatalError(message)
        elif status == Status.INVALID_URL.value:
            raise errors.InvalidUrlError(message)
        elif status == Status.LIST_NO_QUERY.value:
            raise errors.ListNoQueryError(f'{message} required')
        elif status == Status.SEARCH_NO_QUERY.value:
            raise errors.SearchNoQueryError(f'{message}: any parameter is required')
        elif status == Status.LIST_UNSPECIFIED.value:
            raise errors.ListUnspecifiedError(message)
        elif status == Status.SEARCH_UNSORTABLE.value:
            raise errors.SearchUnsortableError(message)
        else:
            raise Exception(message)
