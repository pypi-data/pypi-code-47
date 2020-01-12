import os
pkg_dir=os.path.dirname(__file__)
pkg_data_dir=pkg_dir+'/data'

def is_linux():
    import sys
    pf=sys.platform
    if pf=='linux':
        return True
    return False

def is_windows():
    import sys
    pf=sys.platform
    if pf=='win32':
        return True
    return False

