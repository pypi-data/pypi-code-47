from typing import Callable, Union
import os
import toml

from panaetius.library import export
from panaetius.header import __header__
from panaetius.db import Mask

# __all__ = ['Config']


@export
class Config:

    """Handles the config options for the module and stores config variables
    to be shared.

    Attributes
    ----------
    config_file : dict
        Contains the config options. See
        :meth:`~panaetius.config.Config.read_config`
        for the data structure.
    deferred_messages : list
        A list containing the messages to be logged once the logger has been
        instantiated.
    Mask : panaetius.db.Mask
        Class to mask values in a config file.
    module_name : str
        A string representing the module name. This is added in front of all
        envrionment variables and is the title of the `config.toml`.
    path : str
        Path to config file

    Parameters
    ----------
    path : str
        Path to config file
    """

    def __init__(self, path: str) -> None:
        """
        See :class:`~panaetius.config.Config` for parameters.
        """
        self.path = os.path.expanduser(path)
        self.deferred_messages = []
        self.config_file = self.read_config(path)
        self.module_name = __header__.lower()
        self.Mask = Mask

    def read_config(self, path: str, write: bool = False) -> Union[dict, None]:
        """Reads the toml config file from `path` if it exists.

        Parameters
        ----------
        path : str
            Path to config file. Should not contain `config.toml`

            Example: ``path = '~/.config/panaetius'``

        Returns
        -------
        Union[dict, None]
            Returns a dict if the file is found else returns nothing.

            The dict contains a key for each header. Each key corresponds to a
            dictionary containing a key, value pair for each config under
            that header.

            Example::

                [panaetius]

                [panaetius.foo]
                foo = bar

            Returns a dict:

                ``{'panaetius' : {foo: {'foo': 'bar'}}}``
        """

        path += 'config.toml' if path[-1] == '/' else '/config.toml'
        path = os.path.expanduser(path)
        if not write:
            try:
                with open(path, 'r+') as config_file:
                    config_file = toml.load(config_file)
                self.defer_log(f'Config file found at {path}')
                return config_file
            except FileNotFoundError:
                self.defer_log(f'Config file not found at {path}')
                pass
        else:
            try:
                with open(path, 'w+') as config_file:
                    config_file = toml.load(config_file)
                self.defer_log(f'Config file found at {path}')
                return config_file
            except FileNotFoundError:
                self.defer_log(f'Config file not found at {path}')
                pass

    def get(
        self,
        key: str,
        default: str = None,
        cast: Callable = None,
        mask: bool = False,
    ) -> Union[str, None]:
        """Retrives the config variable from either the `config.toml` or an
        environment variable. Will default to the default value if nothing
        is found

        Parameters
        ----------
        key : str
            Key to the configuration variable. Should be in the form
            `panaetius.variable` or `panaetius.header.variable`.
            When loaded, it will be accessable at
            `Config.panaetius_variable` or
            `Config.panaetius_header_variable`.
        default : str, optional
            The default value if nothing is found. Defaults to `None`.
        cast : Callable, optional
            The type of the variable. E.g `int` or `float`. Should reference
            the type object and not as string. Defaults to `None`.

        Returns
        -------
        Any
            Will return the config variable if found, or the default.
        """
        env_key = f"{__header__.upper()}_{key.upper().replace('.', '_')}"

        try:
            # look in the config.toml
            if len(key.split('.')) == 2:
                # look for subsections
                # print(mask)
                if mask:
                    # print('mask', key)
                    value = self.Mask(
                        self.path, self.config_file, key
                    ).get_value()
                else:
                    # print('no-mask')
                    section, name = key.lower().split('.')
                    value = self.config_file[self.module_name][section][name]
                    self.defer_log(f'{env_key} found in config.toml')
            else:
                # print('valueerror')
                # look under top level module __header__
                # key = f'{self.module_name}.key'
                if mask:
                    # key = f'{__header__}.{key}'
                    # print(f'mask key={key}')
                    value = self.Mask(
                        self.path, self.config_file, key
                    ).get_value()
                else:
                    name = key.lower()
                    value = self.config_file[self.module_name][name]
                    self.defer_log(f'{env_key} found in config.toml')
            # finally:
            try:
                # return if found in config.toml
                return cast(value) if cast else value
            except UnboundLocalError:
                # pass if nothing was found
                # print('unbound error')
                pass
        except KeyError:
            # print('key error')
            self.defer_log(f'{env_key} not found in config.toml')
        except TypeError:
            # print('type error')
            self.defer_log(f'{env_key} not found in config.toml')

        # look for an environment variable
        value = os.environ.get(env_key)

        if value is not None:
            self.defer_log(f'{env_key} found in an environment variable')
        else:
            # fall back to default
            self.defer_log(f'{env_key} not found in an environment variable.')
            value = default
            self.defer_log(f'{env_key} set to default {default}')
        return cast(value) if cast else value

    def defer_log(self, msg: str) -> None:
        """Populates a list `Config.deferred_messages` with all the events to
        be passed to the logger later if required.

        Parameters
        ----------
        msg : str
            The message to be logged.
        """
        self.deferred_messages.append(msg)

    def reset_log(self) -> None:
        """Empties the list `Config.deferred_messages`.
        """
        del self.deferred_messages
        self.deferred_messages = []
