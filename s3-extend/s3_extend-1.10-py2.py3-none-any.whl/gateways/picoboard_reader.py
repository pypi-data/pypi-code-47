"""
 Copyright (c) 2019 Alan Yorinks All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import serial
from serial.tools import list_ports
import sys
import threading
import time

class PicoBoardReader(threading.Thread):

    """
    Picoboard data reader
    """

    def __init__(self, com_port=None):
        self.baud_rate = 38400

        self.channels = {0: "D", 1: "C",
                           2: "B", 3: "btn", 4: "A",
                           5: "lt", 6: "snd", 7: "slide", 15: "id"}

        self.data_packet = None
        if com_port:
            self.picoboard = serial.Serial(com_port, self.baud_rate,
                                     timeout=1, writeTimeout=0)
        else:
            self.find_the_picoboard()
            print('picoboard found on:', self.picoboard.port)

        threading.Thread.__init__(self)
        self.daemon = True
        self.stop_event = threading.Event()
        self.start()
        time.sleep(.2)
        self.count = 0
        x= b'\x01'

        while True:
            try:
                time.sleep(.001)
                self.picoboard.write(x)
            except KeyboardInterrupt:
                self.picoboard.close()
                sys.exit(0)

    def find_the_picoboard(self):
        # go through the ports looking for an active board
        serial_ports = []

        the_ports_list = list_ports.comports()
        for port in the_ports_list:
            if port.pid is None:
                continue
            else:
                print('Looking for picoboard on: ', port.device)
                self.picoboard = serial.Serial(port.device, self.baud_rate,
                                               timeout=1, writeTimeout=0)
                num_bytes = None
                for send in range(10):
                    self.picoboard.write(b'\x01')
                    time.sleep(.2)
                    num_bytes = self.picoboard.inWaiting()
                    if num_bytes == 18:
                        self.picoboard.reset_input_buffer()
                        self.picoboard.reset_output_buffer()

                        return
                    else:
                        continue
            continue
        print('Could not find a picoboard')
        sys.exit(0)


    def analog_scaling(self, value):
        """
        scale the normal analog input range of 0-1023 to 0-100
        :param value:
        :return:
        """
        assert 0 <= value <= 1023, 'analog input must be in range of 0-1023'
        return int(round ((100 * value) / 1023))

    def light_scaling(self, value):
        if value < 25:
            return 100 - value
        else:
            return int(round((1023 - value) * (75 / 998)))

    def sound_scaling(self, value):
        value = max(0, value - 18)
        if (value < 50):
            return int(value / 2)
        else:
            return int(25 + min(75, round((value - 50) * (75 / 580))))

    def run(self):
        """
        This method continually runs. If an incoming character is available on the serial port
        it is read and placed on the _command_deque
        @return: Never Returns
        """
        # time.sleep(.5)
        # while not self.is_stopped():
        while True:
            # we can get an OSError: [Errno9] Bad file descriptor when shutting down
            # just ignore it
            # try:
            self.data_packet = None
            if self.picoboard.inWaiting():
                self.count += 1
                self.data_packet = self.picoboard.read(18)

                sresult = ''
                for i in range(9):
                    cooked = 0
                    sb_channel = self.channels[(int(self.data_packet[2 * i]) - 128) >> 3]
                    sb_value = ((int(self.data_packet[2 * i]) & 7) << 7) + int(self.data_packet[2 * i + 1])
                    if i in [0, 1, 2, 4, 7]:
                        # scale for standard analog:
                        cooked = self.analog_scaling(sb_value)
                        sresult = sresult + sb_channel + '=' + str(cooked) + ' '
                    elif i == 5: # light
                        cooked = self.light_scaling(sb_value)
                        sresult = sresult + sb_channel + '=' + str(cooked)+ ' '

                    elif i == 6: # sound
                        cooked = self.sound_scaling(sb_value)
                        sresult = sresult + sb_channel + '=' + str(cooked)+ ' '

                    elif i == 3: # invert digital input
                        cooked = not sb_value
                        sresult = sresult + sb_channel + '=' + str(cooked)+ ' '

                    elif i == 8:
                        cooked = sb_value
                        sresult = sresult + sb_channel + '=' + str(cooked)+ ' '

                print('\r' + sresult, end=' ' )

            else:
                try:
                    time.sleep(.001)
                except KeyboardInterrupt:
                    sys.exit(0)

PicoBoardReader()
