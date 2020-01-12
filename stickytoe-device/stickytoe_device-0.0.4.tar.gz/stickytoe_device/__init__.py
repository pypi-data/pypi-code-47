import collections
from . import constants, devices, inputs

# Aliases
_device = collections.namedtuple("devices", ["I2C", "GPIO"])
DEVICE = _device(GPIO=devices.GPIO, I2C=devices.I2C)

get_device = devices.get_device

_input = collections.namedtuple("input", ["I2C", "GPIO"])
INPUT = _device(GPIO=inputs.GPIO, I2C=inputs.I2C)

get_input = inputs.get_input

reset = devices.reset