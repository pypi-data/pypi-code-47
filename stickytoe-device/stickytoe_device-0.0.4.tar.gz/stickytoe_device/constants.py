import pathlib


"""This python module contains constants utilized in device initialization and general use.
These strings are mainly utilized as the JSON keys for the MQTT payload
"""

# Pathlib Constants
BINPATH = pathlib.Path(__file__).parent / "bin"

# Registers

GPIO_REGISTER = []
I2C_REGISTER = []

REGISTERS = [
    GPIO_REGISTER,
    I2C_REGISTER,
]



# General Keys

NAME_KEY = "name"

# I2C Keys

ADDRESS_KEY = "addr"
BUS_KEY = "bus"

# List of I2C Keys to check for in config
I2C_KEYS = [
    ADDRESS_KEY,
    BUS_KEY,
]

# GPIO Keys

GPIO_KEY = "gpio"
MODE_KEY = "mode"

GPIO_KEYS = [
    GPIO_KEY,
    MODE_KEY,
]

# Input GPIO Keys

BOUNCETIME_KEY = "bouncetime"
RISING_KEY = "rising"
FALLING_KEY = "falling"