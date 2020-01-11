from .constants import HTTP_STATUS_CODE_MAP
from .exceptions import DateProcessingError

__all__ = (
    'validate_response_code',
)


def validate_response_code(code: int):
    """
    Validate a code from a 17track API response
    """
    if code not in [0, 200]:
        raise DateProcessingError(
            message=HTTP_STATUS_CODE_MAP.get(code, f'Unknown error (Code: {code})'),
            code=code
        )
