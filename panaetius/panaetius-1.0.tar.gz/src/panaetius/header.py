import os
from importlib import util

__path = os.getcwd()

try:
    __spec = util.spec_from_file_location(
        '__header__', f'{os.getcwd()}/__header__.py'
    )
    __header__ = util.module_from_spec(__spec)
    __spec.loader.exec_module(__header__)
    __header__ = __header__.__header__
except FileNotFoundError:
    venv = os.environ.get('VIRTUAL_ENV').split('/')[-1]
    if venv is not None:
        __header__ = venv
    else:
        raise FileNotFoundError(
            f'Cannot find a __header__.py file in {os.getcwd()} containing the'
            ' __header__ value of your project name and you are not working'
            ' from a virtual environment. Either make sure this file '
            'exists and the value is set or create and work from a virtual '
            'environment and try again.'
        )
