from abc import ABCMeta, abstractmethod
import pathlib
import subprocess
import importlib
import logging

# local imports
from . import constants


def get_device(pip: pathlib.Path, config: dict, package: dict):
    logger = logging.getLogger(__name__)

    if config["package"] not in package.keys():
        logger.error("Package not validated".format(config["package"]))
        raise ValueError

    try:
        mod = importlib.import_module(config["package"])
    except ModuleNotFoundError:
        logger.warning(
            "{} not installed. Trying to pip install the module".format(config["package"]))
        subprocess.run(["bash", constants.BINPATH.joinpath(
            "pip"), str(pip), config["package"], config["version"]], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

        try:
            mod = importlib.import_module(config["package"])
        except ModuleNotFoundError:
            logger.error("cannot import {}=={}".format(
                config["package"], config["version"]))
            raise ValueError

    logger.info("{} found. Creating an object".format(mod))

    try:
        device = mod.get_device({**config["config"], constants.NAME_KEY: config[constants.NAME_KEY]})
    except NotImplementedError:
        logger.error("get_device was not found in {}".format(mod))
        raise ValueError

    if not isinstance(device, _Device):
        logger.error("{} does not inherit from _Device".format(device))
        raise ValueError
    return device

def reset():
    """ resets the registers which enforces device/input uniqueness.
    """
    for v in constants.REGISTERS:
        v = []

def init_helper(config: dict, diff_key: str, keys: list, register: list)->bool:
    logger = logging.getLogger(__name__)

    if all(k in config for k in keys):
        diff_val = config[diff_key]

        if diff_val in register:
            logger.error(
                "{}: {} already has been allocated".format(diff_key, addr))
            return False

        register.append(diff_val)
    else:
        logger.error("Missing key in {}".format(config))
        return False
    return True

class _Device(metaclass=ABCMeta):
    """the private base class that requires certain function signatures for general usage.

        Implement an execute(self, payload:str) function to finish this abstract class.

        Return None if nothing should be published.

        Otherwise return a payload string which will be published accordingly.

        DO NOT INHERIT DIRECTLY FROM _DEVICE.
    """
    @abstractmethod
    def __init__(self, config: dict):
        self._logger = logging.getLogger(__name__)
        if constants.NAME_KEY not in config:
            print("test1")
            raise ValueError

        self.name = config[constants.NAME_KEY]

    @abstractmethod
    def execute(self, payload: str):
        pass


class I2C(_Device):
    """an abstract class that extends the functionality of the private, skeleton class _Device.

        raises ValueError if two or more devices allocate the same address.
    """

    def __init__(self, config: dict):
        super().__init__(config)
        
        if not init_helper(config, constants.ADDRESS_KEY, constants.I2C_KEYS, constants.I2C_REGISTER):
            print("test")
            raise ValueError

        self.bus = config[constants.BUS_KEY]
        self.addr = config[constants.ADDRESS_KEY]
        

class GPIO(_Device):
    """an abstract class that extends the functionality of the private, skeleton class _Device.

    raises ValueError if two or more devices allocate the same pin.
    """

    def __init__(self):
        super().__init__(config)

        if not init_helper(config, constants.GPIO_KEY, constants.GPIO_KEYS, constants.GPIO_REGISTER):
            raise ValueError

        self.gpio = config[constants.GPIO_KEY]
        self.mode = config[constants.MODE_KEY]
