from enum import Enum, unique
import logging
from etornado.singleton import SingletonMeta

HTTP_OK = 200

@unique
class ErrorCode(Enum):
    NONE = 0
    UNKNOWN = 100
    UNSUPPORTED_URL = 101
    UNSUPPORTED_METHOD = 102
    LACK_OF_FIELD = 103
    UNSUPPORTED_LOGGING_LEVEL = 104


ERROR_INFO_MAP = {
    ErrorCode.NONE: "ok",
    ErrorCode.UNKNOWN: "unknown error",
    ErrorCode.UNSUPPORTED_URL: "unsupported url [{url}]",
    ErrorCode.UNSUPPORTED_METHOD:
    "unsupported method [{method}] for url [{url}]",
    ErrorCode.LACK_OF_FIELD: "lack of field [{field}]",
    ErrorCode.UNSUPPORTED_LOGGING_LEVEL: "unsupported logging level [{level}]",
}


class ErrorCodeManager(object, metaclass=SingletonMeta):
    MIN_USER_DEFINE_ERROR_CODE = 1000

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.error_infos = {}
        self.__register_error_enum(ErrorCode, ERROR_INFO_MAP, False)

    def register_error_enum(self, error_enum, error_info_map):
        self.__register_error_enum(error_enum, error_info_map, True)

    def register_error_code(self, error_code, error_msg):
        self.__register_error_code(error_code, error_msg, True)

    def __register_error_enum(self, error_enum, error_info_map, user_define):
        for name, member in error_enum.__members__.items():
            error_msg = error_info_map.get(member, "")
            if not error_msg:
                self.logger.warning("error msg of [%s] is empty", member)
            self.__register_error_code(member.value, error_msg, user_define)

    def __register_error_code(self, error_code, error_msg, user_define):
        if error_code in self.error_infos:
            raise Exception("error_code [%d] has be registered"
                    " with message[%s]" % (error_code, error_msg))
        if user_define is True and error_code < self.MIN_USER_DEFINE_ERROR_CODE:
            raise Exception("user define error code must be greater than or "
                            "equal to %s" % self.MIN_USER_DEFINE_ERROR_CODE)
        if user_define is False and error_code >= self.MIN_USER_DEFINE_ERROR_CODE:
            raise Exception("buildin error code must be less"
                            " than %s" % self.MIN_USER_DEFINE_ERROR_CODE)
        self.error_infos[error_code] = error_msg

    def format_error_info(self, error_code, **kwargs):
        if error_code is None:
            error_code = ErrorCode.UNKNOWN
        if isinstance(error_code, Enum):
            error_code = error_code.value
        error_message = self.error_infos.get(error_code, "").format(**kwargs)
        return {"err_no": error_code, "err_msg": error_message}


error_code_manager = ErrorCodeManager()
