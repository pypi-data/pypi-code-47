import re


def camel2kebab(string):
    """
    Transforms CamelCase to kebab-case

    Adapted from http://stackoverflow.com/questions/1796180/ddg#1796247

    :type string: basestring
    :rtype: basestring
    """
    _string = re.sub("(.)([A-Z][a-z]+)", r"\1-\2", string)
    return re.sub("([a-z0-9])([A-Z])", r"\1-\2", _string).lower()
