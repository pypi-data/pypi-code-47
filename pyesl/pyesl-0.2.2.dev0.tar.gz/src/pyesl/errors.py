# -*- coding: utf-8 -*-


class BaseError(Exception):
    """
    Raised when a error occur.
    """

    SUBCODE = 10501
    STATUS = u'PyESL Error'

    def __init__(self, message="", subcode=SUBCODE, status=STATUS, *args, **kwargs):
        self.status = status or self.STATUS
        self.subcode = subcode or self.SUBCODE
        self.error = kwargs.get("error", {})
        self.info = kwargs.get("info", {})
        Exception.__init__(self, message, *args)


class ParamError(BaseError):
    """
    **调用创建QueryBody接口的参数异常**
    """
    SUBCODE = 10422
    STATUS = u'PyESL Invalid Parameter Error'


class DuplicateKeyError(BaseError):
    """
    **暂无用**
    """
    SUBCODE = 11061
    STATUS = u'PyESL Duplicate Key Error'


class SearchFailedError(BaseError):
    """
    **查询条件异常**
    """
    SUBCODE = 10400
    STATUS = u'PyESL Elasticsearch Search Error'


class QueryBodyError(BaseError):
    """
    **调用创建QueryBody接口异常**
    """
    STATUS = u'PyESL Elasticsearch Query Body Error'
