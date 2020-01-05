from os import getenv
from os import getlogin
from os.path import pathsep
from pathlib import Path


def _get_dirs(var_name, default_value=None):
    """
    Retrieves the specified :code:`$XDG_*_DIRS` type variable, then returns
    a sequence of the directory names.  This is to help make the code more
    Pythonic rather than return a single long string delimited by [semi]colons.

    :param str var_name: The name of the :code:`$XDG_*_DIRS` variable.
    :param str default_value: The default value of the variable is not
            defined in the list of environment variables.

    :rtype: tuple
    :return: A sequence of directory names that represent the values of the
            :code:`$XDG_*_DIRS` variables.
    """
    if not default_value:
        default_value = ''
    return tuple(getenv(var_name, default_value).split(pathsep))


class XDGWindowsPlatform(object):
    """
    A top level XDG object that implements the XDG specification within a
    reasonable approximation for a Windows-based platform.  Essentially, all
    paths will build from :code:`%APPDATA%`.
    """

    def __init__(self):
        """Initializes the base XDG object."""
        self._app_data = getenv('APPDATA')

    @property
    def XDG_DATA_HOME(self):
        """
        There is a single base directory relative to which user-specific data
        files should be written. This directory is defined by the environment
        variable :code:`$XDG_DATA_HOME`.

        :code:`$XDG_DATA_HOME` defines the base directory relative to which user
        specific data files should be stored. If :code:`$XDG_DATA_HOME` is
        either not set or empty, a default equal to :code:`$HOME/.local/share`
        should be used.

        A Windows-platform approximation, the default value differs from the
        true XDG Base Directories Specification and will return:
        :code:`%APPDATA%/local/share`.

        :rtype: str
        :return: A string containing the value of :code:`$XDG_DATA_HOME`.
        """
        return getenv('XDG_DATA_HOME',
                      Path(self._app_data).joinpath('local', 'share')
                                          .as_posix())

    @property
    def XDG_CONFIG_HOME(self):
        """
        There is a single base directory relative to which user-specific
        configuration files should be written. This directory is defined by the
        environment variable :code:`$XDG_CONFIG_HOME`.

        :code:`$XDG_CONFIG_HOME` defines the base directory relative to which
        user specific configuration files should be stored. If
        :code:`$XDG_CONFIG_HOME` is either not set or empty, a default equal to
        :code:`$HOME/.config` should be used.

        A Windows-platform approximation, the default value differs from the
        true XDG Base Directories Specification and will return:
        :code:`%APPDATA%/config`.

        :rtype: str
        :return: A string containing the value of :code:`$XDG_CONFIG_HOME`.
        """
        return getenv('XDG_CONFIG_HOME',
                      Path(self._app_data).joinpath('config').as_posix())

    @property
    def XDG_CACHE_HOME(self):
        """
        There is a single base directory relative to which user-specific
        non-essential (cached) data should be written. This directory is defined
        by the environment variable :code:`$XDG_CACHE_HOME`.

        code:`$XDG_CACHE_HOME` defines the base directory relative to which user
        specific non-essential data files should be stored. If
        :code:`$XDG_CACHE_HOME` is either not set or empty, a default equal to
        :code:`$HOME/.cache` should be used.

        A Windows-platform approximation, the default value differs from the
        true XDG Base Directories Specification and will return:
        :code:`%APPDATA%/cache`.

        :rtype: str
        :return: A string containing the value of :code:`$XDG_CACHE_HOME`.
        """
        return getenv('XDG_CACHE_HOME',
                      Path(self._app_data).joinpath('cache').as_posix())

    @property
    def XDG_RUNTIME_DIR(self):
        """
        There is a single base directory relative to which user-specific runtime
        files and other file objects should be placed. This directory is defined
        by the environment variable :code:`$XDG_RUNTIME_DIR`.

        :code:`$XDG_RUNTIME_DIR` defines the base directory relative to which
        user-specific non-essential runtime files and other file objects (such
        as sockets, named pipes, ...) should be stored. The directory MUST be
        owned by the user, and he MUST be the only one having read and write
        access to it. Its Unix access mode MUST be 0700.

        The lifetime of the directory MUST be bound to the user being logged in.
        It MUST be created when the user first logs in and if the user fully
        logs out the directory MUST be removed. If the user logs in more than
        once he should get pointed to the same directory, and it is mandatory
        that the directory continues to exist from his first login to his last
        logout on the system, and not removed in between. Files in the directory
        MUST not survive reboot or a full logout/login cycle.

        The directory MUST be on a local file system and not shared with any
        other system. The directory MUST by fully-featured by the standards of
        the operating system. More specifically, on Unix-like operating systems
        AF_UNIX sockets, symbolic links, hard links, proper permissions, file
        locking, sparse files, memory mapping, file change notifications, a
        reliable hard link count must be supported, and no restrictions on the
        file name character set should be imposed. Files in this directory MAY
        be subjected to periodic clean-up. To ensure that your files are not
        removed, they should have their access time timestamp modified at least
        once every 6 hours of monotonic time or the 'sticky' bit should be set
        on the file.

        If :code:`$XDG_RUNTIME_DIR` is not set applications should fall back to
        a replacement directory with similar capabilities and print a warning
        message. Applications should use this directory for communication and
        synchronization purposes and should not place larger files in it, since
        it might reside in runtime memory and cannot necessarily be swapped out
        to disk.

        A Windows-platform approximation, the default value differs from the
        true XDG Base Directories Specification and will return:
        :code:`%APPDATA%/run/user/loginname`.

        :rtype: str
        :return: A string containing the value of :code:`$XDG_RUNTIME_DIR`.
        """
        default_value = Path(self._app_data).joinpath('run',
                                                      'user',
                                                      getlogin())\
                                            .as_posix()
        return getenv('XDG_RUNTIME_DIR', default_value)

    @property
    def XDG_DATA_DIRS(self):
        """
        There is a set of preference ordered base directories relative to which
        data files should be searched. This set of directories is defined by the
        environment variable :code:`$XDG_DATA_DIRS`.

        :code:`$XDG_DATA_DIRS` defines the preference-ordered set of base
        directories to search for data files in addition to the
        :code:`$XDG_DATA_HOME` base directory. The directories in
        :code:`$XDG_DATA_DIRS` should be seperated with a colon ':'.

        If :code:`$XDG_DATA_DIRS` is either not set or empty, a value equal to
        :code:`/usr/local/share/:/usr/share/` should be used.

        The order of base directories denotes their importance; the first
        directory listed is the most important. When the same information is
        defined in multiple places the information defined relative to the more
        important base directory takes precedent. The base directory defined by
        :code:`$XDG_DATA_HOME` is considered more important than any of the base
        directories defined by :code:`$XDG_DATA_DIRS`.

        A Windows-platform approximation, the default value differs from the
        true XDG Base Directories Specification and will return:
        :code:`%APPDATA%/usr/local/share;%APPDATA%/usr/share`.

        :rtype: tuple
        :return: A sequence containing the value of :code:`$XDG_DATA_DIRS`.
        """
        data_home = self.XDG_DATA_HOME
        dirs = _get_dirs('XDG_DATA_DIRS',
                         f'{self._app_data}/usr/local/share'
                         f';{self._app_data}/usr/share')
        if not dirs:
            dirs = (data_home,)
        elif dirs[0] != data_home:
            dirs = tuple([data_home] + list(dirs))
        dirs = [d for d in dirs if d]
        return tuple(dirs)

    @property
    def XDG_CONFIG_DIRS(self):
        """
        There is a set of preference ordered base directories relative to which
        configuration files should be searched. This set of directories is
        defined by the environment variable code:`$XDG_CONFIG_DIRS`.

        :code:`$XDG_CONFIG_DIRS` defines the preference-ordered set of base
        directories to search for configuration files in addition to the
        :code:`$XDG_CONFIG_HOME` base directory. The directories in
        :code:`$XDG_CONFIG_DIRS` should be seperated with a colon ':'.

        If :code:`$XDG_CONFIG_DIRS` is either not set or empty, a value equal to
        :code:`/etc/xdg` should be used.

        The order of base directories denotes their importance; the first
        directory listed is the most important. When the same information is
        defined in multiple places the information defined relative to the more
        important base directory takes precedent. The base directory defined by
        :code:`$XDG_CONFIG_HOME` is considered more important than any of the
        base directories defined by :code:`$XDG_CONFIG_DIRS`.

        A Windows-platform approximation, the default value differs from the
        true XDG Base Directories Specification and will return:
        :code:`%APPDATA%/etc/xdg`.

        :rtype: tuple
        :return: A sequence containing the value of :code:`$XDG_CONFIG_DIRS`.
        """
        config_home = self.XDG_CONFIG_HOME
        dirs = _get_dirs('XDG_CONFIG_DIRS', f'{self._app_data}/etc/xdg')
        if not dirs:
            dirs = (config_home,)
        elif dirs[0] != config_home:
            dirs = tuple([config_home] + list(dirs))
        dirs = [d for d in dirs if d]
        return tuple(dirs)
