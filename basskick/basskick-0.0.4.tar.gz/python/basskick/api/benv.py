'''




'''


import logging
logger = logging.getLogger(__name__)

def create(name, location):
    try:
        import ensurepip
    except ImportError:
        raise Exception(
            'You cannot use this python to create a benv: ensurepip not found.'
        )

    logger.info('Creating benv {} in {}'.format(name, location))

    #FIXME: this should take a blender version (the benv is created by blender)

    # 1) find the blender version (download if needed)
    # 2) run it with args: -b --python-expr "import pip.__main__ as m; import sys; sys.argv=['install', 'venv']; exec(open(m.__file__).read())"
    #   => actually, try and use runpy.run_module() instead.