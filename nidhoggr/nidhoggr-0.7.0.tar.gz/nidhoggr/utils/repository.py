from typing import Union, TypeVar

from nidhoggr_core.response import StatusResponse
from werkzeug.exceptions import InternalServerError

T = TypeVar("T")


def handle_status(repository_response: Union[StatusResponse, T]) -> T:
    if isinstance(repository_response, StatusResponse):
        raise InternalServerError(description=repository_response.reason)
    return repository_response
