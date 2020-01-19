class JstageError(Exception):
    """Abstract class for errors caused by J-STAGE API"""
    pass


class JstageWarning(Warning):
    """Abstract class for warnings caused by J-STAGE API"""
    pass


class NoResultsError(JstageError):
    """ERR_001"""
    pass


class TooManyResultsError(JstageWarning):
    """WARN_001"""
    pass


class TooManyRequestsError(JstageError):
    """ERR_003"""
    pass


class InvalidQueryError(JstageError):
    """ERR_004"""
    pass


class EmptyRequiredFieldError(JstageError):
    """ERR_005"""
    pass


class InvalidYearValueError(JstageError):
    """ERR_006"""
    pass


class InvalidCountsError(JstageError):
    """ERR_007"""
    pass


class InvalidIssnError(JstageError):
    """ERR_008"""
    pass


class SystemFatalError(JstageError):
    """SYS_ERR_009"""
    pass


class InvalidUrlError(JstageError):
    """ERR_010"""
    pass


class ListNoQueryError(JstageError):
    """ERR_011"""
    pass


class SearchNoQueryError(JstageError):
    """ERR_012"""
    pass


class ListUnspecifiedError(JstageError):
    """ERR_013"""
    pass


class SearchUnsortableError(JstageError):
    """ERR_014"""
    pass
