__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import logging
logging.basicConfig(
    format='[%(name)s::%(levelname)s] %(message)s',
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)
logger.info('Let the BASS Kick !')


def blender_startup():
    from .packon import PackonRegistry
    PackonRegistry.THE().discover_packons()


try:
    import bpy
except (ImportError, ModuleNotFoundError):
    pass
else:
    blender_startup()

blender_startup()