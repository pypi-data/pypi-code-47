# TinyCircuits Light Sensor TSL2572 Wireling Module
# Written by: Corey Miller for TinyCircuits
# Initialized: 6-15-19
# Last updated: 12-12-19

import math
from time import sleep
from micropython import const
try:
    import struct
except ImportError:
    import ustruct as struct
import busio
import board


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/TinyCircuits_CircuitPython_TSL2572.git"

#    I2C ADDRESS/BITS/SETTINGS
#    -----------------------------------------------------------------------

_MULTIPLEXER_ADDRESS = const(0x70)
_TSL2572_ADDRESS = const(0x39)
_TSL2572_CHIPID = const(0x60)

_TSL2572_GAIN_1X = const(0x00)
_TSL2572_GAIN_8X = const(0x01)
_TSL2572_GAIN_16X = const(0x02)
_TSL2572_GAIN_120X = const(0x03)

#_GAIN_VAL = _TSL2572_GAIN_16X

#only use this with 1x and 8x gain settings
_GAIN_DIVIDE_6 = True

#class TinyCircuits_TSL2572():
#    def _read_byte(self, register):
#        """Read a byte register value and return it"""
#        return self._read_register(register, 1)[0]
#
#    def _read_register(self, register, length):
#        raise NotImplementedError()
#
#    def _write_register_byte(self, register, value):
#        raise NotImplementedError()

class TinyCircuits_TSL2572_I2C():
    """Driver for TSL2572 connected over I2C"""
    def __init__(self, gain, i2c=busio.I2C(board.SCL, board.SDA), address=_TSL2572_ADDRESS):
        import adafruit_bus_device.i2c_device as i2c_device
        self._multiplexer = i2c_device.I2CDevice(i2c, _MULTIPLEXER_ADDRESS)
        self._i2c = i2c_device.I2CDevice(i2c, address)

        self._write_register_byte(0x0F, gain)
        self._write_register_byte(0x01, 0xED)
        self._write_register_byte(0x00, 0x03)

        if _GAIN_DIVIDE_6:
            self._write_register_byte(0x0D, 0x04)

        if gain == _TSL2572_GAIN_1X:
            self.gain_val = 1
        elif gain == _TSL2572_GAIN_8X:
            self.gain_val = 8
        elif gain == _TSL2572_GAIN_16X:
            self.gain_val = 16
        elif gain == _TSL2572_GAIN_120X:
            self.gain_val = 120
        else:
            self.gain_val = 16

    def _read_register(self, register, length):
        with self._i2c as i2c:
            i2c.write(bytes([register & 0xFF]))
            result = bytearray(length)
            i2c.readinto(result)
            #print("$%02X => %s" % (register, [hex(i) for i in result]))
            return result

    def _write_register_byte(self, register, value):
        with self._i2c as i2c:
            i2c.write(bytes([register | 0x80, value]))
            #print("$%02X <= 0x%02X" % (register, value))

    def readAmbientLight(self):
        data = self._read_register(0xA0 | 0x14, 4)
        with self._i2c as i2c:
            i2c.write(bytes([0xA0 | 0x14]))
            data = bytearray(4)
            i2c.readinto(data)
        #for i in range(0,4):
         #   print(data[i])
        
        c0 = data[1] << 8 | data[0]
        c1 = data[3] << 8 | data[2]

        #print("c0: {} c1: {}".format(c0,c1))

        cpl = 51.87 * self.gain_val / 60

        #print("cpl: {}".format(cpl))
        if _GAIN_DIVIDE_6:
            cpl /= 6
        
        lux1 = (c0 - (1.87 * c1)) / cpl
        lux2 = ((0.63 * c0) - c1) / cpl

        cpl = max(lux1, lux2)
        return max(cpl, 0)

