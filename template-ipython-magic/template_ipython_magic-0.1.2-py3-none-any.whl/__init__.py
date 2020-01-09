__version__ = '0.1.2'

import importlib.util

def load_ipython_extension(ipython):
    # pylint: disable=import-outside-toplevel

    if importlib.util.find_spec('jinja2') is not None:
        from .jinja import JinjaMagics
        ipython.register_magics(JinjaMagics)

    if importlib.util.find_spec('mako') is not None:
        from .mako import MakoMagics
        ipython.register_magics(MakoMagics)
