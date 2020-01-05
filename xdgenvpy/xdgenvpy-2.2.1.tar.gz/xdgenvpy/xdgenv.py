from os import makedirs
from pathlib import Path

from platform import system

if system() == 'Linux' or system() == 'Darwin':
    from xdgenvpy._xdg_posix import XDGPosixPlatform as XDG

elif system() == 'Windows':
    from xdgenvpy._xdg_windows import XDGWindowsPlatform as XDG

else:
    raise RuntimeError('Unknown platform: {}'.format(system()))


class XDGPackage(XDG):
    """
    An instance of this class helps build package specific directories according
    to the XDG specification.  In the case of:

        -   :code:`$XDG_DATA_DIR`
        -   :code:`$XDG_CONFIG_DIR`
        -   :code:`$XDG_CACHE_DIR`

    variables, this is accomplished by simply appending the package name to the
    directory locations.  All other variables essentially remain unchanged,
    unless they require the DATA/CONFIG/CACHE package directories.
    """

    def __init__(self, package_name):
        """
        Initializes the object with the specified package name.

        :param str package_name: The name of the package.
        """
        super(XDGPackage, self).__init__()
        if package_name:
            package_name = package_name.strip()
        assert package_name, 'Package name must be specified.'
        self._package_name = package_name

    @property
    def XDG_DATA_HOME(self):
        """:return: A package directory relative to the XDG data directory."""
        base = super(XDGPackage, self).XDG_DATA_HOME
        return Path().joinpath(base, self._package_name)

    @property
    def XDG_CONFIG_HOME(self):
        """:return: A package directory relative to the XDG config directory."""
        base = super(XDGPackage, self).XDG_CONFIG_HOME
        return Path().joinpath(base, self._package_name)

    @property
    def XDG_CACHE_HOME(self):
        """:return: A package directory relative to the XDG cache directory."""
        base = super(XDGPackage, self).XDG_CACHE_HOME
        return Path().joinpath(base, self._package_name)

    @property
    def XDG_RUNTIME_DIR(self):
        """
        :return: A package directory relative to the XDG runtime directory.
        """
        base = super(XDGPackage, self).XDG_RUNTIME_DIR
        return Path().joinpath(base, self._package_name)


class XDGPedanticPackage(XDGPackage):
    """
    An instance of this class goes one step further than the :class:`XDGPackage`
    in that it ensures package-specific directories exist in the file system.
    If one of the

        -   :code:`$XDG_DATA_DIR`
        -   :code:`$XDG_CONFIG_DIR`
        -   :code:`$XDG_CACHE_DIR`

    does not exist, the getter method will ensure the directory (and all parent
    directories) exist.  This same logic is not applied to non-package specific
    directories as they can often contain system level directories.  And thus
    may not be writable by the current user.
    """

    def __init__(self, package_name):
        """
        Initializes the pedantic object with the specified package name.

        :param str package_name: The name of the package.
        """
        super(XDGPedanticPackage, self).__init__(package_name)

    @staticmethod
    def _safe_path(path):
        """
        Ensures the supplied path exists.  If the path does not exist then the
        directory and all parent directories will be created.

        :param str path: The path to ensure exists.

        :rtype: str
        :return: The supplied string, but ensures the path exists.
        """
        if not Path(path).exists():
            makedirs(path)
        return path

    @property
    def XDG_DATA_HOME(self):
        """
        :return: A package directory relative to the XDG data directory with the
                guarantee that the directory exists.
        """
        base = super(XDGPedanticPackage, self).XDG_DATA_HOME
        return XDGPedanticPackage._safe_path(base)

    @property
    def XDG_CONFIG_HOME(self):
        """
        :return: A package directory relative to the XDG config directory with
                the guarantee that the directory exists.
        """
        base = super(XDGPedanticPackage, self).XDG_CONFIG_HOME
        return XDGPedanticPackage._safe_path(base)

    @property
    def XDG_CACHE_HOME(self):
        """
        :return: A package directory relative to the XDG cache directory with
                the guarantee that the directory exists.
        """
        base = super(XDGPedanticPackage, self).XDG_CACHE_HOME
        return XDGPedanticPackage._safe_path(base)

    @property
    def XDG_RUNTIME_DIR(self):
        """
        :return: A package directory relative to the XDG runtime directory with
                the guarantee that the directory exists.
        """
        base = super(XDGPedanticPackage, self).XDG_RUNTIME_DIR
        return XDGPedanticPackage._safe_path(base)
