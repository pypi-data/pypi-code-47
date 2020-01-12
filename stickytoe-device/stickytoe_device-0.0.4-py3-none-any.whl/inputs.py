import pathlib
import logging
import paho.mqtt.client as paho
import RPi.GPIO as RPiGPIO

from abc import ABCMeta, abstractmethod

from . import devices, constants


def get_input(pip: pathlib.Path, client:paho.Client, config: dict, package: dict):
    logger = logging.getLogger(__name__)

    if config["package"] not in package.keys():
        logger.error("Package {} not validated for installation".format(config["package"]))
        raise ValueError

    if config["version"] != package[config["package"]]:
        logger.error("Package version not validated for installation".format(config["version"]))
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
        input = mod.get_input({**config["config"], constants.NAME_KEY:config[constants.NAME_KEY]}, client)
    except NotImplementedError:
        logger.error("get_input was not found in {}".format(mod))
        raise ValueError

    if not isinstance(device, _Input):
        logger.error("{} does not inherit from _Input".format(device))
        raise ValueError
    return device

class _Input(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, config:dict, client:paho.Client):
        self.config = config
        self.client = client
        self._logger = logging.getLogger(__name__)

class I2C(_Input):
    
    def __init__(self, config: dict, client: paho.Client):
        super().__init__(config, client)

class GPIO(_Input):

    def __init__(self, config: dict, client: paho.Client):
        super().__init__(config, client)

        if not devices.init_helper(config, constants.GPIO_KEY, constants.GPIO_KEYS, constants.GPIO_REGISTER):
            raise ValueError

        self.gpio = self.config[constants.GPIO_KEY]
        mode = self.config[constants.MODE_KEY]

        self.mode = None
        
        if mode == constants.RISING_KEY:
            self.mode = RPiGPIO.RISING
        elif mode == constants.FALLING_KEY:
            self.mode = RPiGPIO.FALLING
        
        if self.mode is None:
            raise ValueError

        self.bouncetime = self.config.get(constants.BOUNCETIME_KEY, 200)

        RPiGPIO.setup(self.gpio, RPiGPIO.IN, pull_up_down=RPiGPIO.PUD_DOWN)
        

    @abstractmethod
    def handler(self, channel: int):
        if channel != self.gpio:
            return None
        
        gpio_value = None
        if self.mode == RPiGPIO.RISING:
            gpio_value = 1
        elif self.mode == RPiGPIO.FALLING:
            gpio_value = 0
        
        if gpio_value is None:
            return None

        if gpio_value != RPiGPIO.input(self.gpio):
            return None
        return True
