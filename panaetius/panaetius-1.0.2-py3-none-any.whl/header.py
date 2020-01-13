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
    try:
        venv = os.environ.get('VIRTUAL_ENV').split('/')[-1]
        __header__ = venv
    except AttributeError:
        print(
            f'Cannot find a __header__.py file in {os.getcwd()} containing the'
            ' __header__ value of your project name and you are not working'
            ' from a virtual environment. Either make sure this file '
            'exists and the value is set or create and work from a virtual '
            'environment and try again. \n The __header__ value has been '
            'set to the default of panaetius.'
        )
        __header__ = 'panaetius'
