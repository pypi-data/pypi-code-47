"""
circleci.version
~~~~~~~~~~~~~~~~
"""
VERSION = "0.9.5"
"""Current version of circleci.py."""

def get_short_version():
    """
    Format "short" version in the form of X.Y
    :returns: short version
    """
    ver = VERSION.split(".")
    short_version = "{0}.{1}".format(ver[0], ver[1])
    return short_version
