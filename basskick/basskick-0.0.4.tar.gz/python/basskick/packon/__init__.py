'''

    basskick.packon

'''
import pkg_resources

class PackonRegistry(object):

    PACKON_TYPES = {}
    _SINGLETON = None

    @classmethod
    def THE(cls):
        singleton = cls._SINGLETON
        if singleton is None:
            singleton = cls()
            cls._SINGLETON = singleton
        return singleton

    @classmethod
    def discover_packons(cls):
        print('Packon Discovery in progress')
        entry_name = 'blender_addon'
        for entry_point in pkg_resources.iter_entry_points(
            entry_name
        ):
            print('\tPackon found:', entry_point)
            continue
            PackonType = entry_point.load()
            cls.install(PackonType)

        print('Checking Packon Requirements')
        cls.check_requirements()
        print('Auto Registering Packons')
        cls.register_all(auto_register_only=True)

        print('Packon Discovery in Done')

    @classmethod
    def install(cls, PackonType):
        print('Installing Packon "{}"'.format(PackonType.name()))
        name = PackonType.name()
        try:
            previous = cls.PACKON_TYPES[name]
        except KeyError:
            pass
        else:
            if previous is PackonType:
                return
            raise ValueError(
                'Another {!r} Packon is already installed.'.format(
                    name, 
                )
            )

        cls.PACKON_TYPES[name] = PackonType

        for packon_name in PackonType.packon_requires:
            cls.require(packon_name)

    @classmethod
    def require(cls, packon_name, by_packon_type):
        if not packon_name in cls.PACKON_TYPES:
            raise ValueError(
                'Could not find packon {!r} required by {!r}'.format(
                    packon_name, by_packon_type.name()
                )
            )

    @classmethod
    def check_requirements(cls):
        for name, PackonType in cls.PACKON_TYPES.items():
            for req_name in (PackonType.packon_requires or []):
                cls.require(req_name, PackonType)

    @classmethod
    def register_all(cls, auto_register_only=True):
        cls.check_requirements()
        for name, PackonType in cls.PACKON_TYPES.items():
            if auto_register_only and not PackonType.auto_register:
                continue
            if not PackonType.is_registered():
                PackonType.unregister()
                PackonType.set_registered(True)

    @classmethod
    def unregister_all(cls):
        for name, PackonType in cls.PACKON_TYPES.items():
            if PackonType.is_registered():
                PackonType.unregister()
                PackonType.set_registered(False)

class Packon(object):

    bl_info = dict(
        name=None,
        author='Someone Nice',
        version=(0, 1),
        blender=(2, 80, 0),
        location='View3D > Toolshelf (T)',
        description='Base stuff for all basskick Packons',
        category='3D View',
    )
    packon_requires=[]
    auto_register = True

    def __init__(self, name):
        super(object, self).__init__()

    @classmethod
    def name(cls):
        return cls.bl_info.get('name', cls.__name__)

    @classmethod
    def set_registered(cls, b):
        cls._IS_REGISTERED = b
        
    @classmethod
    def is_registered(cls, b):
        return cls._IS_REGISTERED
        
    @classmethod
    def register(cls):
        pass

    @classmethod
    def unregister(cls):
        pass


