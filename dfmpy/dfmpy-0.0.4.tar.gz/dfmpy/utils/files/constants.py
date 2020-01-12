# TODO docs

from dfmpy.utils.config import get_config


def suffixes():
    # TODO docs
    # TODO unit test
    # Order of precedence:
    #   file.txt##hostname
    #   file.txt##hostname.system
    #   file.txt##systemname
    #   file.txt
    marker = get_config().marker
    delimiter = get_config().delimiter
    hostname = get_config().hostname
    system_type = get_config().system
    return tuple([
        marker + hostname,
        marker + delimiter.join([hostname, system_type]),
        marker + system_type,
    ])
