# -*- coding: utf8 -*-
# python 3
# (C) Fabrice Sincère

"""This pure python module provides a raspberry pi i2c interface for \
Maxim-Dallas DS1621 DS1631 DS1631A DS1721 DS1731 high-precision digital \
thermometer and thermostat.

DS1621, DS1631, DS1631A : thermometer accuracy is ±0.5°C
DS1721, DS1731 : thermometer accuracy is ±1°C

DS1631A begin performing temperature conversion immediately at power-up.

DS1621, DS1631, DS1721 and DS1731 begins continuous conversions after \
a Start Convert command.

Datasheet
=========

https://datasheets.maximintegrated.com/en/ds/DS1621.pdf
https://datasheets.maximintegrated.com/en/ds/DS1721.pdf
https://datasheets.maximintegrated.com/en/ds/DS1631-DS1731.pdf

2-wire serial data bus
======================

DS1631s are connected to Raspberry pi i2c GPIO (8 devices max) with 4 wires :

- SDA i2c bus (GPIO2)
- SCL i2c bus (GPIO3)
- Power (3.3 V or 5 V)
- Ground

Installation
============

pip install DS1631

Basic usage
===========

Raspberry pi : OS Raspbian

First, you need python 3 smbus module :
sudo apt install python3-smbus

DS1631 device simple example
----------------------------

import DS1631
import time

i2c_address = 0x48
ic1 = DS1631.DS1631(1, i2c_address)
# thermostat config
ic1.set_tout_polarity("active-low")
ic1.set_thigh(22.5)
ic1.set_tlow(20.5)
# thermometer config
ic1.set_conversion_mode("continuous")
ic1.set_resolution(12)
ic1.start_convert()
# read temperature
while True:
    time.sleep(0.75)
    temperature = ic1.get_temperature()
    print("Temperature  : {} °C".format(temperature))

Virtual device simple example
-----------------------------

DS1631 module provides a DS1631virtualdevice class for development without \
raspberry pi or DS1631s devices.

On–Off controller (hysteresis controller) simulation is performed :

- if temperature > thigh then electric radiator OFF
- if temperature < tlow then electric radiator ON

Of course, you don't need python 3 smbus module, so you can work with a \
Windows OS computer or Android OS device (pydroid3).

import DS1631
import time

# virtual device
room = DS1631.DS1631virtualdevice(initial_temperature=18,
                                  thigh=20, tlow=19,
                                  P=1000, R=0.02,
                                  tau=360,
                                  Text_max=15,Text_min=10,
                                  period=24*3600)
while True:
    time.sleep(0.75)
    temperature = room.get_temperature()
    print("Temperature  : {} °C".format(temperature))


Author
======

Fabrice Sincère <fabrice.sincere@wanadoo.fr>
https://pypi.org/project/DS1631
"""

try:
    import smbus
except:
    print("""smbus module not found.
You can only use DS1631virtualdevice class""")

import sys
import math
import random
import time
import threading

__version__ = (0, 3, 6)
__author__ = "Fabrice Sincère <fabrice.sincere@wanadoo.fr>"

if sys.version_info[0] < 3:
    print('You need to run this with Python 3')
    exit(1)


class DS1631:
    """Raspberry Pi I2c interface for Maxim-Dallas DS1631 DS1631A DS1721 \
DS1731
Needs smbus module"""

    # command set
    ACCESS_CONFIG = 0xAC     # 1 byte, read/write
    READ_TEMPERATURE = 0xAA  # 2 bytes, read only
    ACCESS_TH = 0xA1         # 2 bytes, read/write
    ACCESS_TL = 0xA2         # 2 bytes, read/write

    START_CONVERT = 0x51
    STOP_CONVERT = 0x22
    SOFTWARE_POR = 0x54

    def __init__(self, i2c_bus_id, i2c_addr):
        """i2c_bus_id : 0 or 1 (depend of Raspberry Pi version)
i2c_addr : 7-bit i2c address is (1 0 0 1 A2 A1 A0)

Basic usage
-----------

import DS1631
ic1 = DS1631.DS1631(1, 0x4A)
ic1.print_configuration()
"""

        try:
            import smbus
        except:
            raise ImportError("""smbus module not found.
You must install smbus module on your Raspberry Pi""")

        self.__i2c_bus__id = i2c_bus_id
        self.bus = smbus.SMBus(self.__i2c_bus__id)

        # 7-bit i2c address is (1 0 0 1 A2 A1 A0)
        self.__i2c_addr = i2c_addr

        if self.__i2c_addr not in range(0x48, 0x4F + 1):
            raise ValueError("Invalid i2c address value")

    def stop(self):
        """Do nothing.
Only for DS1631virtualdevice class method compatibility"""
        pass

    def set_conversion_mode(self, mode):
        """Set the conversion mode
mode = "one-shot" or "continuous"
Stored in EEPROM (write cycle time : 10 ms max)

Note : when writing to the configuration register, conversions should first be \
stopped using the Stop Convert command if the device is in continuous \
conversion mode.
"""
        config_register = self.get_config_register()
        # 1SHOT : Configuration Register Bit 0 (LSB)
        # write 1SHOT bit

        if mode == "one-shot":
            # one-shot mode (1SHOT = 1)
            self.set_config_register(config_register | 0x01)
        elif mode == "continuous":
            # continuous mode (1SHOT = 0)
            self.set_config_register(config_register & 0xFE)
        else:
            raise NameError("Invalid conversion mode name")

    def get_conversion_mode(self, config_register=None):
        """Read and return the conversion mode ("continuous" or "one-shot")"""

        if config_register is None:
            # Read config register
            config_register = self.get_config_register()
        # read 1SHOT bit
        if config_register & 0x01 == 0x00:
            # continuous mode (1SHOT = 0)
            return "continuous"
        else:
            # one-shot mode (1SHOT = 1)
            return "one-shot"

    def set_tout_polarity(self, polarity):
        """Set the Tout polarity
polarity = "active-low" or "active-high"
Stored in EEPROM (write cycle time : 10 ms max)

Note : when writing to the configuration register, conversions should first \
be stopped using the Stop Convert command if the device is in \
continuous conversion mode.
"""
        config_register = self.get_config_register()
        # Tout polarity : POL Configuration Register Bit 1
        # write POL bit
        if polarity == "active-high":
            # POL = 1
            self.set_config_register(config_register | 0x02)
        elif polarity == "active-low":
            # POL = 0
            self.set_config_register(config_register & 0xFD)
        else:
            raise NameError("Invalid polarity name")

    def get_tout_polarity(self, config_register=None):
        """Read and return the Tout polarity ("active-low" or "active-high")"""
        if config_register is None:
            # Read config register
            config_register = self.get_config_register()
        # Tout polarity : POL (bit 1)
        if config_register & 0x02 == 0x00:
            # POL = 0
            return "active-low"
        else:
            # POL = 1
            return "active-high"

    def set_resolution(self, resolution):
        """Set the temperature resolution
resolution is 9, 10, 11 or 12 bits

Stored in SRAM (power-up state 12 bits)

Note : when writing to the configuration register, conversions should first be \
stopped using the Stop Convert command if the device is in \
continuous conversion mode.
"""
        config_register = self.get_config_register()
        # write R1 (bit 3) R0 (bit 2)
        if resolution == 9:
            # R1 = 0 R0 = 0
            self.set_config_register(config_register & 0xF3)
        elif resolution == 10:
            # R1 = 0 R0 = 1
            self.set_config_register((config_register & 0xF7) | 0x04)
        elif resolution == 11:
            # R1 = 1 R0 = 0
            self.set_config_register((config_register & 0xFB) | 0x08)
        elif resolution == 12:
            # R1 = 1 R0 = 1
            self.set_config_register(config_register | 0x0C)
        else:
            raise ValueError("Resolution out of range")

    def get_resolution(self, config_register=None):
        """Read resolution and return the tuple \
temperature resolution (bits), temperature resolution (°C), \
conversion time (ms)"""

        if config_register is None:
            # Read config register
            config_register = self.get_config_register()

        # resolution : R1 (bit 3) R0 (bit 2)
        if config_register & 0x0C == 0x00:
            # R1=0  R0=0
            return 9, 0.5, 93.75
        elif config_register & 0x0C == 0x04:
            # R1=0  R0=1
            return 10, 0.25, 187.5
        elif config_register & 0x0C == 0x08:
            # R1=1  R0=0
            return 11, 0.125, 375.0
        elif config_register & 0x0C == 0x0C:
            # R1=1  R0=1
            return 12, 0.0625, 750.0

    def is_eeprom_busy(self, config_register=None):
        """EEPROM status
return True if a write to memory is in progress
return False if memory is not busy

Note : write cycle time : 10 ms max, 4 ms typ.
"""
        if config_register is None:
            # Read the NVB (NV Memory Busy) bit from config register
            config_register = self.get_config_register()

        # Non Volatile Memory Busy : NVB (bit 4)
        if config_register & 0x10 == 0x00:
            # NVB = 0 : memory is not busy
            return False
        else:
            # NVB = 1 : a write to memory is in progress
            return True

    def is_tlow_flag_on(self, config_register=None):
        """Tl thermostat status.
return False if the measured temperature has not been lower than the \
value stored in the Tl register since power-up ;
otherwise return True
"""
        if config_register is None:
            # Read config register
            config_register = self.get_config_register()

        # Temperature Low Flag : TLF (bit 5)
        if config_register & 0x20 == 0x00:
            # TLF = 0 "off"
            return False
        else:
            # TLF = 1 "on"
            return True

    def reset_tlow_flag(self):
        """Tl thermostat status.
Tlow flag is overwritten with a 0
"""
        config_register = self.get_config_register()
        # Temperature Low Flag : TLF (bit 5)
        # reset TLF
        self.set_config_register(config_register & 0xDF)

    def is_thigh_flag_on(self, config_register=None):
        """Th thermostat status.
return False if the measured temperature has not exceeded the value \
stored in the Th register since power-up ;
otherwise return True
"""
        if config_register is None:
            # Read Temperature High Flag bit
            config_register = self.get_config_register()

        # Temperature High Flag : THF (bit 6)
        if config_register & 0x40 == 0x00:
            # THF = 0 "off"
            return False
        else:
            # THF = 1 "on"
            return True

    def reset_thigh_flag(self):
        """Th thermostat status.
Thigh flag is overwritten with a 0
"""
        config_register = self.get_config_register()
        # Temperature High Flag : THF (bit 6)
        # reset THF
        self.set_config_register(config_register & 0xBF)

    def is_temperature_conversion_in_progress(self, config_register=None):
        """Temperature conversion status
return True if a temperature conversion is in progress
return False if the temperature conversion is complete
"""
        if config_register is None:
            # Read the DONE bit from config register
            config_register = self.get_config_register()

        # Temperature Conversion : DONE (bit 7)
        if config_register & 0x80 == 0x00:
            # DONE = 0 'in progress'
            return True
        else:
            # DONE = 1 'complete'
            return False

    def get_temperature(self):
        """Read and return the last converted temperature value (°C) \
from the temperature register.

Note : temperature value stored in SRAM (power-up state -60 °C)
"""
        word = self.bus.read_word_data(self.__i2c_addr, DS1631.READ_TEMPERATURE)
        return convert_word_to_temperature(word)

    def set_thigh(self, temperature):
        """Set the upper thermostat trip point.
temperature range : -55°C to +125°C
Stored in EEPROM (write cycle time : 10 ms max)

Note : when making changes to the Th and Tl registers, conversions should \
first be stopped using the Stop Convert command if the device is in \
continuous conversion mode.
"""

        if not -55.0 <= temperature <= 125.0:
            raise ValueError("Temperature out of range")

        self.bus.write_word_data(self.__i2c_addr, DS1631.ACCESS_TH,
                                 convert_temperature_to_word(temperature))

    def get_thigh(self):
        """Read and return the Th thermostat register (°C)"""
        word = self.bus.read_word_data(self.__i2c_addr, DS1631.ACCESS_TH)
        return convert_word_to_temperature(word)

    def set_tlow(self, temperature):
        """Set the lower thermostat trip point.
temperature range : -55°C to +125°C
Stored in EEPROM (write cycle time : 10 ms max)

Note : when making changes to the Th and Tl registers, conversions should \
first be stopped using the Stop Convert command if the device is in continuous \
conversion mode.
"""
        if not -55.0 <= temperature <= 125.0:
            raise ValueError("Temperature out of range")

        self.bus.write_word_data(self.__i2c_addr, DS1631.ACCESS_TL,
                                 convert_temperature_to_word(temperature))

    def get_tlow(self):
        """Read and return the Tl thermostat register (°C)"""

        word = self.bus.read_word_data(self.__i2c_addr, DS1631.ACCESS_TL)
        return convert_word_to_temperature(word)

    def start_convert(self):
        """Initiates temperature conversions.
If the part is in one-shot mode, only one conversion is performed.
In continuous mode, continuous temperature conversions are performed \
until a Stop Convert command is issued."""
        self.bus.write_byte(self.__i2c_addr, DS1631.START_CONVERT)

    def stop_convert(self):
        """Stops temperature conversions when the device is in
continuous conversion mode"""
        self.bus.write_byte(self.__i2c_addr, DS1631.STOP_CONVERT)

    def software_por(self):
        """ Initiates a software power-on-reset (POR), which stops \
temperature conversions and resets all registers and logic to their \
power-up states.

Power-up state
--------------

temperature register : -60 °C
resolution  : 12 bits
temperature high flag : 0 (off)
temperature low flag : 0 (off)
"""
        try:
            self.bus.write_byte(self.__i2c_addr, DS1631.SOFTWARE_POR)
        except:
            pass

    def get_config_register(self):
        """Read and return the configuration register"""
        config_register = \
            self.bus.read_byte_data(self.__i2c_addr, DS1631.ACCESS_CONFIG)
        return config_register

    def set_config_register(self, config_register):
        """Write to the configuration register

Note : when writing to the configuration register, conversions should first be \
stopped using the Stop Convert command if the device is in \
continuous conversion mode."""
        self.bus.write_byte_data(self.__i2c_addr, DS1631.ACCESS_CONFIG,
                                 config_register)

    def print_configuration(self):
        """Read and print configuration and status information"""

        config_register = self.get_config_register()
        memory = self.is_eeprom_busy(config_register)
        conversion_mode = self.get_conversion_mode(config_register)
        tout_polarity = self.get_tout_polarity(config_register)
        resolution, quantum, conversion_time = \
            self.get_resolution(config_register)
        if memory:
            memory = "a write to memory is in progress"
        else:
            memory = "memory is not busy"
        tlow_flag = self.is_tlow_flag_on(config_register)
        if tlow_flag:
            tlow_flag = "on"
        else:
            tlow_flag = "off"
        thigh_flag = self.is_thigh_flag_on(config_register)
        if thigh_flag:
            thigh_flag = "on"
        else:
            thigh_flag = "off"
        temperature_conversion = \
            self.is_temperature_conversion_in_progress(config_register)
        if temperature_conversion:
            temperature_conversion = "in progress"
        else:
            temperature_conversion = "complete"

        print("""
Configuration
-------------
I2c address            : 0x{:0x}
Configuration register : 0x{:0x}

Conversion mode        : {}
Tout polarity          : {}
Resolution             : {} bits
 --> Resolution        : {} °C
 --> Conversion time   : {} ms (max)

Status information
------------------
EEPROM memory          : {}
Temperature Low Flag   : {}
Temperature High Flag  : {}
Temperature conversion : {}
""".format(self.__i2c_addr, config_register, conversion_mode,
           tout_polarity, resolution, quantum, conversion_time, memory,
           tlow_flag, thigh_flag, temperature_conversion))


class DS1621:
    """Raspberry Pi I2c interface for Maxim-Dallas DS1621
Needs smbus module"""

    # command set
    ACCESS_CONFIG = 0xAC     # 1 byte, read/write
    READ_TEMPERATURE = 0xAA  # 2 bytes, read only
    READ_COUNTER = 0xA8      # 1 byte, read only
    READ_SLOPE = 0xA9        # 1 byte, read only

    ACCESS_TH = 0xA1         # 2 bytes, read/write
    ACCESS_TL = 0xA2         # 2 bytes, read/write

    START_CONVERT = 0xEE
    STOP_CONVERT = 0x22

    def __init__(self, i2c_bus_id, i2c_addr):
        """i2c_bus_id : 0 or 1 (depend of Raspberry Pi version)
i2c_addr : 7-bit i2c address is (1 0 0 1 A2 A1 A0)

Basic usage
-----------

import DS1631
ic1 = DS1631.DS1621(1, 0x4A)
ic1.print_configuration()
"""

        try:
            import smbus
        except:
            raise ImportError("""smbus module not found.
You must install smbus module on your Raspberry Pi""")

        self.__i2c_bus__id = i2c_bus_id
        self.bus = smbus.SMBus(self.__i2c_bus__id)

        # 7-bit i2c address is (1 0 0 1 A2 A1 A0)
        self.__i2c_addr = i2c_addr

        if self.__i2c_addr not in range(0x48, 0x4F + 1):
            raise ValueError("Invalid i2c address value")

    def stop(self):
        """Do nothing.
Only for DS1631virtualdevice class method compatibility"""
        pass

    def set_conversion_mode(self, mode):
        """Set the conversion mode
mode = "one-shot" or "continuous"
Stored in EEPROM (write cycle time : 10 ms max)

Note : when writing to the configuration register, conversions should first be \
stopped using the Stop Convert command if the device is in continuous \
conversion mode.
"""
        config_register = self.get_config_register()
        # 1SHOT : Configuration Register Bit 0 (LSB)
        # write 1SHOT bit

        if mode == "one-shot":
            # one-shot mode (1SHOT = 1)
            self.set_config_register(config_register | 0x01)
        elif mode == "continuous":
            # continuous mode (1SHOT = 0)
            self.set_config_register(config_register & 0xFE)
        else:
            raise NameError("Invalid conversion mode name")

    def get_conversion_mode(self, config_register=None):
        """Read and return the conversion mode ("continuous" or "one-shot")"""

        if config_register is None:
            # Read config register
            config_register = self.get_config_register()
        # read 1SHOT bit
        if config_register & 0x01 == 0x00:
            # continuous mode (1SHOT = 0)
            return "continuous"
        else:
            # one-shot mode (1SHOT = 1)
            return "one-shot"

    def set_tout_polarity(self, polarity):
        """Set the Tout polarity
polarity = "active-low" or "active-high"
Stored in EEPROM (write cycle time : 10 ms max)

Note : when writing to the configuration register, conversions should first \
be stopped using the Stop Convert command if the device is in \
continuous conversion mode.
"""
        config_register = self.get_config_register()
        # Tout polarity : POL Configuration Register Bit 1
        # write POL bit
        if polarity == "active-high":
            # POL = 1
            self.set_config_register(config_register | 0x02)
        elif polarity == "active-low":
            # POL = 0
            self.set_config_register(config_register & 0xFD)
        else:
            raise NameError("Invalid polarity name")

    def get_tout_polarity(self, config_register=None):
        """Read and return the Tout polarity ("active-low" or "active-high")"""
        if config_register is None:
            # Read config register
            config_register = self.get_config_register()
        # Tout polarity : POL (bit 1)
        if config_register & 0x02 == 0x00:
            # POL = 0
            return "active-low"
        else:
            # POL = 1
            return "active-high"

    def set_resolution(self, resolution):
        """Do nothing.
Only for DS1631 class method compatibility"""
        pass

    def get_resolution(self, config_register=None):
        """Return the tuple (9, 0.5, 750) :
temperature resolution (bits), temperature resolution (°C), \
conversion time (ms)"""
        return 9, 0.5, 750.0

    def is_eeprom_busy(self, config_register=None):
        """EEPROM status
return True if a write to memory is in progress
return False if memory is not busy

Note : write cycle time : 10 ms max, 4 ms typ.
"""
        if config_register is None:
            # Read the NVB (NV Memory Busy) bit from config register
            config_register = self.get_config_register()

        # Non Volatile Memory Busy : NVB (bit 4)
        if config_register & 0x10 == 0x00:
            # NVB = 0 : memory is not busy
            return False
        else:
            # NVB = 1 : a write to memory is in progress
            return True

    def is_tlow_flag_on(self, config_register=None):
        """Tl thermostat status.
return False if the measured temperature has not been lower than the \
value stored in the Tl register since power-up ;
otherwise return True
"""
        if config_register is None:
            # Read config register
            config_register = self.get_config_register()

        # Temperature Low Flag : TLF (bit 5)
        if config_register & 0x20 == 0x00:
            # TLF = 0 "off"
            return False
        else:
            # TLF = 1 "on"
            return True

    def reset_tlow_flag(self):
        """Tl thermostat status.
Tlow flag is overwritten with a 0
"""
        config_register = self.get_config_register()
        # Temperature Low Flag : TLF (bit 5)
        # reset TLF
        self.set_config_register(config_register & 0xDF)

    def is_thigh_flag_on(self, config_register=None):
        """Th thermostat status.
return False if the measured temperature has not exceeded the value \
stored in the Th register since power-up ;
otherwise return True
"""
        if config_register is None:
            # Read Temperature High Flag bit
            config_register = self.get_config_register()

        # Temperature High Flag : THF (bit 6)
        if config_register & 0x40 == 0x00:
            # THF = 0 "off"
            return False
        else:
            # THF = 1 "on"
            return True

    def reset_thigh_flag(self):
        """Th thermostat status.
Thigh flag is overwritten with a 0
"""
        config_register = self.get_config_register()
        # Temperature High Flag : THF (bit 6)
        # reset THF
        self.set_config_register(config_register & 0xBF)

    def is_temperature_conversion_in_progress(self, config_register=None):
        """Temperature conversion status
return True if a temperature conversion is in progress
return False if the temperature conversion is complete
"""
        if config_register is None:
            # Read the DONE bit from config register
            config_register = self.get_config_register()

        # Temperature Conversion : DONE (bit 7)
        if config_register & 0x80 == 0x00:
            # DONE = 0 'in progress'
            return True
        else:
            # DONE = 1 'complete'
            return False

    def get_temperature(self):
        """Read and return the last converted temperature value (°C) \
from the temperature register.
Resolution : 9 bits, 0.5 °C
Conversion time : 750 ms max

Note : temperature value stored in SRAM (power-up state -60 °C)
"""
        word = self.bus.read_word_data(self.__i2c_addr, DS1621.READ_TEMPERATURE)
        return convert_word_to_temperature(word)

    def get_temperature_high_resolution(self):
        """Read and return the last converted temperature value (°C) \
from the Temperature register, Count_Remain register and Count_Per_C register
Resolution : 12 bits, 0.0625 °C
Conversion time : 750 ms max

Note : temperature value stored in SRAM (power-up state -60 °C)
"""
        word = self.bus.read_word_data(self.__i2c_addr, DS1621.READ_TEMPERATURE)
        # 8 bits format
        word = word % 256
        temperature8bits = convert_word_to_temperature(word)

        # 1 to 16
        Count_Remain = self.bus.read_byte_data(self.__i2c_addr,
                                               DS1621.READ_COUNTER)
        # 16
        Count_Per_C = self.bus.read_byte_data(self.__i2c_addr,
                                              DS1621.READ_SLOPE)
        # datasheet's formula is wrong ?
        # the right formula ?
        temperature12bits = temperature8bits + (Count_Per_C - Count_Remain)/Count_Per_C

        return temperature12bits

    def set_thigh(self, temperature):
        """Set the upper thermostat trip point.
temperature range : -55°C to +125°C
Resolution : 9 bits, 0.5 °C
Stored in EEPROM (write cycle time : 10 ms max)

Note : when making changes to the Th and Tl registers, conversions should \
first be stopped using the Stop Convert command if the device is in \
continuous conversion mode.
"""

        if not -55.0 <= temperature <= 125.0:
            raise ValueError("Temperature out of range")

        self.bus.write_word_data(self.__i2c_addr, DS1621.ACCESS_TH,
                                 convert_temperature_to_word(temperature))

    def get_thigh(self):
        """Read and return the Th thermostat register (°C)
Resolution : 9 bits, 0.5 °C """
        word = self.bus.read_word_data(self.__i2c_addr, DS1621.ACCESS_TH)
        return convert_word_to_temperature(word)

    def set_tlow(self, temperature):
        """Set the lower thermostat trip point.
temperature range : -55°C to +125°C
Resolution : 9 bits, 0.5 °C
Stored in EEPROM (write cycle time : 10 ms max)

Note : when making changes to the Th and Tl registers, conversions should \
first be stopped using the Stop Convert command if the device is in continuous \
conversion mode.
"""
        if not -55.0 <= temperature <= 125.0:
            raise ValueError("Temperature out of range")

        self.bus.write_word_data(self.__i2c_addr, DS1621.ACCESS_TL,
                                 convert_temperature_to_word(temperature))

    def get_tlow(self):
        """Read and return the Tl thermostat register (°C)
Resolution : 9 bits, 0.5 °C """

        word = self.bus.read_word_data(self.__i2c_addr, DS1621.ACCESS_TL)
        return convert_word_to_temperature(word)

    def start_convert(self):
        """Initiates temperature conversions.
If the part is in one-shot mode, only one conversion is performed.
In continuous mode, continuous temperature conversions are performed \
until a Stop Convert command is issued."""
        self.bus.write_byte(self.__i2c_addr, DS1621.START_CONVERT)

    def stop_convert(self):
        """Stops temperature conversions when the device is in
continuous conversion mode"""
        self.bus.write_byte(self.__i2c_addr, DS1621.STOP_CONVERT)

    def get_config_register(self):
        """Read and return the configuration register"""
        config_register = \
            self.bus.read_byte_data(self.__i2c_addr, DS1621.ACCESS_CONFIG)
        return config_register

    def set_config_register(self, config_register):
        """Write to the configuration register

Note : when writing to the configuration register, conversions should first be \
stopped using the Stop Convert command if the device is in \
continuous conversion mode."""
        self.bus.write_byte_data(self.__i2c_addr, DS1621.ACCESS_CONFIG,
                                 config_register)

    def print_configuration(self):
        """Read and print configuration and status information"""

        config_register = self.get_config_register()
        memory = self.is_eeprom_busy(config_register)
        conversion_mode = self.get_conversion_mode(config_register)
        tout_polarity = self.get_tout_polarity(config_register)
        resolution, quantum, conversion_time = \
            self.get_resolution(config_register)
        if memory:
            memory = "a write to memory is in progress"
        else:
            memory = "memory is not busy"
        tlow_flag = self.is_tlow_flag_on(config_register)
        if tlow_flag:
            tlow_flag = "on"
        else:
            tlow_flag = "off"
        thigh_flag = self.is_thigh_flag_on(config_register)
        if thigh_flag:
            thigh_flag = "on"
        else:
            thigh_flag = "off"
        temperature_conversion = \
            self.is_temperature_conversion_in_progress(config_register)
        if temperature_conversion:
            temperature_conversion = "in progress"
        else:
            temperature_conversion = "complete"

        print("""
Configuration
-------------
I2c address            : 0x{:0x}
Configuration register : 0x{:0x}

Conversion mode        : {}
Tout polarity          : {}
Resolution             : {} bits
 --> Resolution        : {} °C
 --> Conversion time   : {} ms (max)

Status information
------------------
EEPROM memory          : {}
Temperature Low Flag   : {}
Temperature High Flag  : {}
Temperature conversion : {}
""".format(self.__i2c_addr, config_register, conversion_mode,
           tout_polarity, resolution, quantum, conversion_time, memory,
           tlow_flag, thigh_flag, temperature_conversion))


class DS1631virtualdevice(threading.Thread):
    """Virtual device I2c interface for Maxim-Dallas DS1621 DS1631 \
DS1631A DS1721 DS1731

on–off controller (hysteresis controller) simulation :
if temperature > thigh then electric radiator OFF
if temperature < tlow then electric radiator ON

Default configuration :
- mode continuous
- 12 bits resolution (0.0625 °C) conversion time 750 ms
- Tout polarity : active low
- begin performing temperature conversion immediately at power-up.
"""

    def __init__(self, initial_temperature=20,
                 thigh=21, tlow=19,
                 P=1000, R=0.02, tau=1*3600, Text_max=25, Text_min=10,
                 period=24*3600, delay=14*3600):
        """

initial_temperature : range -55°C to +125°C
thigh thermostat : range -55°C to +125°C
tlow thermostat : range -55°C to +125°C

P : electric radiator power (W)
R : thermal resistance (°C/W)
tau : thermal time constant (s)  (>> 0.75 s)

Text_max  : max external temperature (°C)
Text_min  : min external temperature (°C)
period : in seconds
delay : in seconds (Text_max time)

Basic usage
-----------

import DS1631
room = DS1631.DS1631virtualdevice()
temperature = room.get_temperature()

# inside temperature sensor (no electric radiator connected)
garage = DS1631.DS1631virtualdevice(P=0)
temperature = garage.get_temperature()

# outside temperature sensor
outside = DS1631.DS1631virtualdevice(P=0, R=0, tau=0)
temperature = outside.get_temperature()
"""

        # threading.Thread.__init__(self)
        super().__init__()

        self.__thigh_flag = "off"
        self.__tlow_flag = "off"

        # warm up values
        # range : -55°C to +125°C
        # resolution 12 bits
        self.__initial_temperature = int(initial_temperature*16)/16

        self.__temperature = self.__initial_temperature
        self.__real_temperature = self.__temperature

        self.__thigh = int(thigh*16)/16  # resolution 12 bits
        self.__tlow = int(tlow*16)/16  # resolution 12 bits
        self.__tout_polarity = "active-low"

        self.__heater = 0  # 0 = electric radiator off
        # 1 = electric radiator on

        self.__P = P  # electric radiator power (W)
        self.__R = R  # thermal resistance (°C/W)
        self.__tau = tau  # time constant (second)

        # external temperature ; cosine law
        self.__Text_max = Text_max  # max external temperature in °C
        self.__Text_min = Text_min  # min external temperature in °C
        self.__period = period  # in seconds
        self.__delay = delay  # in seconds (Text_max time)

        self.__stop_thread = False  # flag
        self.start()  # start the thread’s activity (run() method)

    # getter
    @property
    def P(self):
        """ Electric radiator power (W)"""
        return self.__P

    @P.setter
    def P(self, power):
        self.__P = float(power)

    def set_resolution(self, resolution):
        """Do nothing.
Only for DS1631 class method compatibility"""
        pass

    def get_resolution(self, config_register=None):
        """Read resolution and return the tuple \
temperature resolution (bits), temperature resolution (°C), \
conversion time (ms)"""
        return 12, 0.0625, 750.0

    def set_conversion_mode(self, mode):
        """Do nothing.
Only for DS1631 class method compatibility"""
        pass

    def start_convert(self):
        """Do nothing.
Only for DS1631 class method compatibility"""
        pass

    def set_tout_polarity(self, polarity):
        """Set the Tout polarity
polarity = "active-low" or "active-high"
"""
        if polarity == "active-high":
            self.__tout_polarity = "active-high"
        elif polarity == "active-low":
            self.__tout_polarity = "active-low"
        else:
            raise NameError("Invalid polarity name")

    def get_tout_polarity(self, config_register=None):
        """Read and return the Tout polarity ("active-low" or "active-high")"""
        return self.__tout_polarity

    def print_configuration(self):
        """Read and print configuration and status information"""

        tout_polarity = self.get_tout_polarity()
        resolution, quantum, conversion_time = self.get_resolution()
        tlow_flag = self.is_tlow_flag_on()
        if tlow_flag:
            tlow_flag = "on"
        else:
            tlow_flag = "off"
        thigh_flag = self.is_thigh_flag_on()
        if thigh_flag:
            thigh_flag = "on"
        else:
            thigh_flag = "off"

        print("""
Configuration
-------------
I2c address            : virtual device {}

Conversion mode        : continuous
Tout polarity          : {}
Resolution             : {} bits
 --> Resolution        : {} °C
 --> Conversion time   : {} ms (max)

Status information
------------------
Temperature Low Flag   : {}
Temperature High Flag  : {}
""".format(self.getName(), tout_polarity,
           resolution, quantum, conversion_time, tlow_flag,
           thigh_flag))

    def is_tlow_flag_on(self):
        """Tl thermostat status.
return False if the measured temperature has not been lower than the \
value stored in the Tl register since power-up ;
otherwise return True
"""
        if self.__tlow_flag == "off":
            return False
        if self.__tlow_flag == "on":
            return True

    def reset_tlow_flag(self):
        """Tl thermostat status.
Tlow flag is overwritten with a 0
"""
        self.__tlow_flag = "off"

    def is_thigh_flag_on(self):
        """Th thermostat status.
return False if the measured temperature has not exceeded the value \
stored in the Th register since power-up ;
otherwise return True
"""
        if self.__thigh_flag == "off":
            return False
        if self.__thigh_flag == "on":
            return True

    def reset_thigh_flag(self):
        """Th thermostat status.
Thigh flag is overwritten with a 0
"""
        self.__thigh_flag = "off"

    def get_temperature(self):
        """Read and return the last converted temperature value (°C) \
from the temperature register."""
        return self.__temperature

    def set_thigh(self, temperature):
        """Set the upper thermostat trip point.
temperature range : -55°C to +125°C
"""
        if not -55.0 <= temperature <= 125.0:
            raise ValueError("Temperature out of range")
        self.__thigh = int(temperature*16)/16

    def get_thigh(self):
        """Read and return the Th thermostat register (°C)"""
        return self.__thigh

    def set_tlow(self, temperature):
        """Set the lower thermostat trip point.
temperature range : -55°C to +125°C
"""
        if not -55.0 <= temperature <= 125.0:
            raise ValueError("Temperature out of range")
        self.__tlow = int(temperature*16)/16

    def get_tlow(self):
        """Read and return the Tl thermostat register (°C)"""
        return self.__tlow

    def get_external_temperature(self, time):
        """Return a virtual external temperature (°C)
cosine law

time (second) : timestamp

depend on :
Text_max (°C)
Text_min (°C)
period (second)
delay (second)"""

        temperature = 0.5*(self.__Text_max+self.__Text_min)\
            + 0.5*(self.__Text_max-self.__Text_min)\
            * math.cos(2*math.pi/self.__period*(time-self.__delay))
        return temperature

    def stop(self):
        """ Stop thread’s activity """
        self.__stop_thread = True

    def run(self):
        """ Temperature engine
House heater simulation with hysteresis controller
This method runs every 750 ms

This method representing the thread’s activity
"""
        previous_time = time.time()  # timestamp

        while self.__stop_thread is False:
            time.sleep(0.75)  # conversion time
            actual_time = time.time()  # timestamp
            h = actual_time - previous_time  # step (second)
            previous_time = actual_time

            if self.__tau == 0 or self.__R == 0:
                # outside temperature sensor
                self.__real_temperature = self.get_external_temperature(actual_time)

            else:
                # inside temperature sensor
                # Euler's numerical method
                # to solve first order differential equation
                Tprime = (self.__R*self.__P*self.__heater - (self.__real_temperature - self.get_external_temperature(actual_time)))/self.__tau
                self.__real_temperature += h*Tprime

            # noise + resolution
            self.__temperature = self.__real_temperature \
                + random.uniform(-1, 1)/32
            self.__temperature = int(self.__temperature*16)/16

            # on–off controller (hysteresis controller)
            if self.__temperature > self.__thigh:
                self.__heater = 0  # electric radiator off
                self.__thigh_flag = "on"
            elif self.__temperature < self.__tlow:
                self.__heater = 1  # electric radiator on
                self.__tlow_flag = "on"

        # stop thread


def convert_temperature_to_word(temperature):
    """temperature (float) : -55°C to +125°C range
Return a word (2 bytes) in little endian format
For example :
convert_temperature_to_word(-15.5) return 0x80f0
"""
    # 16 bits format
    word = int(temperature*256.0)
    # 16 bits two’s complement format
    if word < 0:
        word += 65536
    # litte endian
    return swap_bytes(word)


def convert_word_to_temperature(word):
    """word (2 bytes) in little endian format
Return temperature in °C (float)
For example :
convert_word_to_temperature(0x80f0) return -15.5
"""
    # big endian
    word = swap_bytes(word)  # 16 bits two’s complement format

    if word > 32767:
        word -= 65536
    temperature = word/256  # float
    return temperature


def swap_bytes(word):
    """ word : 2 bytes (16 bits)
Swap less significant byte and most significant byte
For example  : swap_bytes(0xF586) return 0x86F5
"""
    msbyte = word//256
    lsbyte = word % 256
    return lsbyte*256 + msbyte


if __name__ == "__main__":
    import DS1631
    help(DS1631)
