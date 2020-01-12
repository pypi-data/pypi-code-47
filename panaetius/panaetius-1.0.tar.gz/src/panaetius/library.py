from __future__ import annotations
import sys
from typing import Any, TypeVar, Type, TYPE_CHECKING, Union, List
import ast


if TYPE_CHECKING:
    import logging


config_inst_t = TypeVar('config_inst_t', bound='panaetius.config.Config')


def export(fn: callable) -> callable:
    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn


def set_config(
    config_inst: Type[config_inst_t],
    key: str,
    default: str = None,
    cast: Any = None,
    check: Union[None, List] = None,
    mask: bool = False,
) -> None:
    """Sets the config variable on the instance of a class.

    Parameters
    ----------
    config_inst : Type[config_inst_t]
        Instance of the :class:`~panaetius.config.Config` class.
    key : str
        The key referencing the config variable.
    default : str, optional
        The default value.
    mask : bool, optional
        Boolean to indiciate if a value in the `config.toml` should be masked.
        If this is set to True then the first time the variable is read from
        the config file the value will be replaced with a hash. Any time that
        value is then read the hash will be compared to the one stored and if
        they match the true value will be returned. This is stored in a sqlite
        `.db` next to the config file and is hidden by default. If the hash
        provided doesn't match the default behaviour is to update the `.db`
        with the new value and hash the value again. If you delete the
        database file then you will need to set the value again in the
        `config.toml`.
    cast : Any, optional
        The type of the variable.
    check : Union[None, List], optional
        Type of object to check against. This is useful if you want to use TOML
        to define a list, but want to make sure that a string representation
        of a list will be loaded properly if it set as an environment variable.

        Example:

        `config.toml` has the following attribute set:
        ```
            [package.users]
            auth = ['user1', 'user2']
        ```

        If set as an environment variable you can pass this list as a string
        and set check=list:

        Environment variable:
        PACKAGE_USERS_AUTH = "['user1', 'user2']"

        Usage in code:
        ```python
        set_config(CONFIG, 'users.auth', check=list)
        ```
    """
    config_var = key.lower().replace('.', '_')
    if check is None:
        setattr(
            config_inst, config_var, config_inst.get(key, default, cast, mask)
        )
    else:
        if type(config_inst.get(key, default, cast, mask)) is not check:
            if check is list:
                var = ast.literal_eval(
                    config_inst.get(key, default, cast, mask)
                )
                setattr(config_inst, config_var, var)
        else:
            setattr(
                config_inst,
                config_var,
                config_inst.get(key, default, cast, mask),
            )


# Create function to print cached logged messages and reset
def process_cached_logs(
    config_inst: Type[config_inst_t], logger: logging.Logger
):
    """Prints the cached messages from :class:`~panaetius.config.Config`
    and resets the cache.

    Parameters
    ----------
    config_inst : Type[config_inst_t]
        Instance of :class:`~panaetius.config.Config`.
    logger : logging.Logger
        Instance of the logger.
    """
    for msg in config_inst.deferred_messages:
        logger.info(msg)
    config_inst.reset_log()
