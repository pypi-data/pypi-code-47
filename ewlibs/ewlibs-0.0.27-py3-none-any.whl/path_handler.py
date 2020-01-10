from os import path as os_path
def relative_path(file, path):
    return os_path.join(os_path.abspath(os_path.dirname(file)), path)