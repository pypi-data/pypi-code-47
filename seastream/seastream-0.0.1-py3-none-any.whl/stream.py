"""

This provides a wrapper stream that takes types and their instances as arguments.


"""

class Stream:
    """
    Wraps other binary streams, allows reading and writing of types registered.
    """

    def __init__(self, base, mode=None, registry=None):
        """

        :param base: a path-like value or a stream-like object
        :param mode: None or a valid read mode for a stream
        :param registry: a seastream.Registry object
        """
        if registry is None:
            raise ValueError("must be passed")

        if type(mode) == str:
            base = open(base, mode=mode)

        self.base = base
        self.registry = registry

    def write(self, obj):# todo : codec kwargs?
        """

        :param obj: bytes-like object or a type
        :return:
        """

        #pass through if it's bytes
        if type(obj) is bytes:
            self.base.write(obj)
            return

        codec = self.registry[type(obj)]
        self.base.write(codec.pack(obj))

    def read(self, arg=None):
        """

        :param arg: an integer or a type
        :return:
        """

        if arg is None:
            arg=-1

        if isinstance(arg, int):
            return self.base.read(arg)

        elif not isinstance(arg, type):
            raise TypeError("Argument to read must be a type or an integer")

        codec = self.registry[arg]

        return codec.unpack(self.base.read(codec.size))
