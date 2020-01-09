import re
import json
import demjson


def replace_utf8mb4(self, v):
    """Replace 4-byte unicode characters by REPLACEMENT CHARACTER"""
    import re
    INVALID_UTF8_RE = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
    INVALID_UTF8_RE.sub(u'\uFFFD', v)


def loads_jsonp(_jsonp):
    """
        解析jsonp数据格式为json
        :return:
    """
    try:
        return demjson.decode(
            re.match(".*?\(({.*})\).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')
