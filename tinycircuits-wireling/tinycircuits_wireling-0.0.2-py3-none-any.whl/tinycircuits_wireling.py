# tinycircuits_wireling.py - Last modified 23 Dec 2019
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# 
# Written by Laveréna Wienclaw for TinyCircuits.
# 
# The latest version of this library can be found at https://TinyCircuits.com/

import RPi.GPIO as GPIO
from micropython import const
import pigpio 
import busio
import board
import adafruit_ads1x15.ads1115 as ADS # Included ADC module
from adafruit_ads1x15.analog_in import AnalogIn
i2c = busio.I2C(board.SCL, board.SDA)

_MULTIPLEXER_ADDRESS = const(0x70)

class Wireling: 
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT) # provides power to Wireling Pi Hat
        GPIO.output(22,1)

    def enablePower(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT) 
        GPIO.output(22,1)

    def disablePower(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22,0)

    def selectPort(self, port):
        pi = pigpio.pi()
        h = pi.i2c_open(1, _MULTIPLEXER_ADDRESS)
        pi.i2c_write_byte(h, 0x04 + port)
        pi.i2c_close(h)

    # Get the correct pin number that correlates to the port number
    def getPin(self, pin):
        if pin == 0: return 10
        elif pin == 1: return 12
        elif pin == 2: return 18
        elif pin == 3: return 21
        else: raise ValueError('Pin %s is not valid, please select pin 0-3' % (pin))

    # Get the correct board pin number that correlates to the port number
    def getBoardPin(self, pin):
        if pin == 0: return board.D10
        elif pin == 1: return board.D12
        elif pin == 2: return board.D18
        elif pin == 3: return board.D21
        else: raise ValueError('Pin %s is not valid, please select pin 0-3' % (pin))

    def analogRead(self, port):
        # Create the ADC object using the I2C bus
        ads = ADS.ADS1115(i2c)
        print("{:>5}\t{:>5}".format('raw', 'v'))
        if port == 0:
            chan = AnalogIn(ads, ADS.P0)
            print("port 0: ")
            print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
            print("")
            return chan.value
        elif port == 1: 
            chan1 = AnalogIn(ads, ADS.P1)
            print("port 1: ")
            print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
            print("")
            return chan1.value
        elif port == 2: 
            chan2 = AnalogIn(ads, ADS.P2)
            print("port 2: ")
            print("{:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
            print("")
            return chan2.value
        elif port == 3: 
            chan3 = AnalogIn(ads, ADS.P3)
            print("port 3: ")
            print("{:>5}\t{:>5.3f}".format(chan3.value, chan3.voltage))
            print("")
            return chan3.value
        else: raise ValueError('Port %s is not valid, please select port 0-3' % (pin))

    # Note: PWM is a percentage. Over 0-3.3V, 50% duty cycle would produce an average of 1.65V
    def analogWrite(self, pin, dutyCycle, frequency=1000):
        self.getPin(pin)
        hatPin = self.getPin(pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(hatPin,GPIO.OUT)
        set_pwm=GPIO.PWM(hatPin,frequency)
        set_pwm.start(dutyCycle)

    # Read the digital value on the input pin
    def digitalRead(self, pin):
         GPIO.setmode(GPIO.BCM)
         rasPin = self.getPin(pin=pin)
         GPIO.setup(rasPin , GPIO.IN, pull_up_down=GPIO.PUD_UP)
         input_state = GPIO.input(rasPin)
         print(input_state)

    # Write a high or low value to a digital pin
    def digitalWrite(self, pin, value):
         rasPin  = self.getPin(pin)
         GPIO.setup(rasPin, GPIO.OUT)
         if value== 1:
             GPIO.output(rasPin, GPIO.HIGH)
         if value == 0: 
             GPIO.output(rasPin, GPIO.LOW)

    # Read and print the raw analog value and voltage on a given pin
    def readADC(self):
        # Create the ADC object using the I2C bus
        ads = ADS.ADS1115(i2c)

        chan = AnalogIn(ads, ADS.P0)
        chan1 = AnalogIn(ads, ADS.P1)
        chan2 = AnalogIn(ads, ADS.P2)
        chan3 = AnalogIn(ads, ADS.P3)

        # Print channel value, and voltage
        print("{:>5}\t{:>5}".format('raw', 'v'))
        print("port0: ")
        print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
        print("")
        print("port1: ")
        print("{:>5}\t{:>5.3f}".format(chan1.value, chan1.voltage))
        print("")
        print("port2: ")
        print("{:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
        print("")
        print("port3: ")
        print("{:>5}\t{:>5.3f}".format(chan3.value, chan3.voltage))
        print("====================================")










	
