import typing

from j2db.models import EventModel

# default empty value in response
# you can change it to "null" or None, or something good for your workflow
EMPTY_VALUE = ""


def safe_error(func):
    def wrapper(origin_request: EventModel, *args, **kwargs):
        origin_request.drop_secret()
        return func(origin_request, *args, **kwargs)
    return wrapper


@safe_error
def auth_invalid_error(origin_request: EventModel) -> typing.Dict[str, str]:
    return {
        "error": "auth_invalid",
        "msg": "auth failed, check your secret",
        "request": origin_request.to_dict(),
        "stack": EMPTY_VALUE,
    }


@safe_error
def json_invalid_error(origin_request: EventModel) -> typing.Dict[str, str]:
    return {
        "error": "json_invalid",
        "msg": "content in your request is not a valid json format",
        "request": origin_request.to_dict(),
        "stack": EMPTY_VALUE,
    }


@safe_error
def table_invalid_error(origin_request: EventModel) -> typing.Dict[str, str]:
    return {
        "error": "table_invalid",
        "msg": "should match the table name",
        "request": origin_request.to_dict(),
        "stack": EMPTY_VALUE,
    }


@safe_error
def db_operator_error(origin_request: EventModel, error: str) -> typing.Dict[str, str]:
    return {
        "error": "db_operator",
        "msg": "operate failed",
        "request": origin_request.to_dict(),
        "stack": error,
    }


@safe_error
def null_error(origin_request: EventModel) -> typing.Dict[str, typing.Any]:
    return {
        "error": EMPTY_VALUE,
        "msg": EMPTY_VALUE,
        "request": origin_request,
        "stack": EMPTY_VALUE,
    }


AuthInvalidError = auth_invalid_error
JsonInvalidError = json_invalid_error
TableInvalidError = table_invalid_error
DBOperatorError = db_operator_error
NullError = null_error


# info
def info_flag_not_found_error(error: str) -> typing.Dict[str, str]:
    return {
        "error": "info_flag_not_found_error",
        "msg": "info flag invalid",
        "request": EMPTY_VALUE,
        "stack": error,
    }


InfoFlagNotFoundError = info_flag_not_found_error
