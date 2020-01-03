# -*- coding: utf-8 -*- 
# @Time     : 2020-01-02 16:44
# @Author   : binger

import attr


@attr.s(frozen=True, slots=True)
class CodeEnum(object):
    code = attr.ib()
    message = attr.ib()

    @property
    def value(self):
        return self.code, self.message


class TypeExtend(type):
    def __init__(self, class_name, class_parents, class_attr):
        if class_name != "StatusCode":
            self.__code__ = class_attr["__code__"]
        super(TypeExtend, self).__init__(class_name, class_parents, class_attr)

    def __getattribute__(self, item):
        value = type.__getattribute__(self, item)
        if item != "__code__":
            return CodeEnum(self.__code__ + value[0], value[1])
        else:
            return value


class StatusCode(metaclass=TypeExtend):
    OK = (0, 'ok')
    UNKNOWN = (998, 'unknown')
    INVALID_ARGUMENT = (997, 'invalid argument')
    NOT_FOUND = (996, 'not found')
    ALREADY_EXISTS = (995, 'already exists')
    PERMISSION_DENIED = (994,
                         'permission denied')
    ABORTED = (993, 'aborted')
    OUT_OF_RANGE = (992, 'out of range')
    UNAVAILABLE = (991, 'unavailable')
    DATA_LOSS = (990, 'data loss')
    UNAUTHENTICATED = (899, 'unauthenticated')
    TIMEOUT = (898, 'timeout')
    INTERNAL_ERROR = (500, 'internal error')


class BaseError(Exception):
    def __init__(self, code, message=""):
        super(BaseError, self).__init__(code, message)

    def __len__(self):
        return len(self.args)


class VisitorCode(StatusCode):
    __code__ = 10000


class VisitorError(BaseError): pass


class ServerCode(StatusCode):
    __code__ = 0


class ServerError(BaseError): pass
