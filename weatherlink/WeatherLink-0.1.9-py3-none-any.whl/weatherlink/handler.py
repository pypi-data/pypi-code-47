#!/usr/bin/env python
"""
    The class for communication with
    Vantage Pro and Vantage Pro 2 Weather Stations
"""
import socket
import struct
from datetime import datetime


class WeatherLink:
    """
        This class operates weather stations in accordance with
        https://www.davisinstruments.com/support/weather/download/VantageSerialProtocolDocs_v261.pdf
    """

    ACK = b'\x06'
    NAK = b'\x21'
    ESC = b'\x1B'

    SEQUENCE_NUMBER = 1
    RECORD_SIZE = 52
    RECORDS_PER_PAGE = 5
    UNUSED_PAGE_BYTES = 4
    CRC_BYTES = 2

    VANTAGE_PRO_ID = 16
    VANTAGE_VUE_ID = 17
    FIRMWARE_VERSION = '3.57'
    FIRMWARE_DATE = 'Aug 24 2016'

    STATION_VERSION_SIZE_IN_BYTES = 2
    PAGES_INFO_SIZE_IN_BYTES = 6
    LOOP2_PACKET_SIZE_IN_BYTES = 99
    ACK_SIZE = len(ACK)

    EEPROM_TIME_ZONE_ADDRESS = 17
    EEPROM_MANUAL_OR_AUTO_ADDRESS = 18
    EEPROM_DAYLIGHT_SAVINGS_ADDRESS = 19
    EEPROM_GMT_OR_ZONE_ADDRESS = 22

    TZ_ENIWETOK = 0
    TZ_KWAJALEIN = 0
    TZ_MIDWAY_ISLAND = 1
    TZ_SAMOA = 1
    TZ_HAWAII = 2
    TZ_ALASKA = 3
    TZ_PACIFIC_TIME = 4
    TZ_TIJUANA = 4
    TZ_MOUNTAIN_TIME = 5
    TZ_CENTRAL_TIME = 6
    TZ_MEXICO_CITY = 7
    TZ_CENTRAL_AMERICA = 8
    TZ_BOGOTA = 9
    TZ_LIMA = 9
    TZ_QUITO = 9
    TZ_EASTERN_TIME = 10
    TZ_ATLANTIC_TIME = 11
    TZ_CARACAS = 12
    TZ_LA_PAZ = 12
    TZ_SANTIAGO = 12
    TZ_NEWFOUNDLAND = 13
    TZ_BRASILIA = 14
    TZ_BUENOS_AIRES = 15
    TZ_GEORGETOWN = 15
    TZ_GREENLAND = 15
    TZ_MID_ATLANTIC = 16
    TZ_AZORES = 17
    TZ_CAPE_VERDE_ISLAND = 17
    TZ_GMT = 18
    TZ_DUBLIN = 18
    TZ_EDINBURGH = 18
    TZ_LISBON = 18
    TZ_LONDON = 18
    TZ_MONROVIA = 19
    TZ_CASABLANCA = 19
    TZ_BERLIN = 20
    TZ_ROME = 20
    TZ_AMSTERDAM = 20
    TZ_BERN = 20
    TZ_STOCKHOLM = 20
    TZ_VIENNA = 20
    TZ_PARIS = 21
    TZ_MADRID = 21
    TZ_BRUSSELS = 21
    TZ_COPENHAGEN = 21
    TZ_WEST_CENTRAL_AFRICA = 21
    TZ_PRAGUE = 22
    TZ_BELGRADE = 22
    TZ_BRATISLAVA = 22
    TZ_BUDAPEST = 22
    TZ_LJUBLJANA = 22
    TZ_ATHENS = 23
    TZ_HELSINKI = 23
    TZ_ISTANBUL = 23
    TZ_MINSK = 23
    TZ_RIGA = 23
    TZ_TALLINN = 23
    TZ_CAIRO = 24
    TZ_EASTERN_EUROPE = 25
    TZ_BUCHAREST = 25
    TZ_HARARE = 26
    TZ_PRETORIA = 26
    TZ_ISRAEL = 27
    TZ_JERUSALEM = 27
    TZ_BAGHDAD = 28
    TZ_KUWAIT = 28
    TZ_NAIROBI = 28
    TZ_RIYADH = 28
    TZ_MOSCOW = 29
    TZ_ST_PETERSBURG = 29
    TZ_VOLGOGRAD = 29
    TZ_TEHRAN = 30
    TZ_ABU_DHABI = 31
    TZ_MUSCAT = 31
    TZ_BAKU = 31
    TZ_TBILISI = 31
    TZ_YEREVAN = 31
    TZ_KAZAN = 31
    TZ_KABUL = 32
    TZ_ISLAMABAD = 33
    TZ_KARACHI = 33
    TZ_EKATERINBURG = 33
    TZ_TASHKENT = 33
    TZ_BOMBAY = 34
    TZ_CALCUTTA = 34
    TZ_MADRAS = 34
    TZ_NEW_DELHI = 34
    TZ_CHENNAI = 34
    TZ_ALMATY = 35
    TZ_DHAKA = 35
    TZ_COLOMBO = 35
    TZ_NOVOSIBIRSK = 35
    TZ_ASTANA = 35
    TZ_BANGKOK = 36
    TZ_JAKARTA = 36
    TZ_HANOI = 36
    TZ_KRASNOYARSK = 36
    TZ_BEIJING = 37
    TZ_CHONGQING = 37
    TZ_URUMQI = 37
    TZ_IRKUTSK = 37
    TZ_ULAAN_BATAAR = 37
    TZ_HONG_KONG = 38
    TZ_PERTH = 38
    TZ_SINGAPORE = 38
    TZ_TAIPEI = 38
    TZ_KUALA_LUMPUR = 38
    TZ_TOKYO = 39
    TZ_OSAKA = 39
    TZ_SAPPORO = 39
    TZ_SEOUL = 39
    TZ_YAKUTSK = 39
    TZ_ADELAIDE = 40
    TZ_DARWIN = 41
    TZ_BRISBANE = 42
    TZ_MELBOURNE = 42
    TZ_SYDNEY = 42
    TZ_CANBERRA = 42
    TZ_HOBART = 43
    TZ_GUAM = 43
    TZ_PORT_MORESBY = 43
    TZ_VLADIVOSTOK = 43
    TZ_MAGADAN = 44
    TZ_SOLOMON_ISLANDS = 44
    TZ_NEW_CALEDONIA = 44
    TZ_FIJI = 45
    TZ_KAMCHATKA = 45
    TZ_MARSHALL_ISLANDS = 45
    TZ_WELLINGTON = 46
    TZ_AUCKLAND = 46

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.station_type = ''
        self.firmware_version = ''
        self.firmware_date = ''
        self.connection = None
        self.connected = self.connect()

    def connect(self):
        """ Connects to WeatherLink meteostation"""
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.settimeout(300)
        try:
            self.connection.connect((self.host, self.port))

            if (
                 not self.test_call() or
                 not self.firmware_version_supported() or
                 not self.firmware_date_supported()
               ):
                raise Exception('Station is not supported')
        except socket.gaierror:
            return False
        except socket.timeout:
            return False
        return True

    def disconnect(self):
        """ Disconnect from WeatherLink meteostation"""
        self.connection.close()

    def _call_and_get_fixed_size_response(self, command, response_size):
        """ Call to WeatherLink """
        self.connection.sendall(command.encode())
        response = self.connection.recv(response_size)

        if len(response) != 0:
            return response
        else:
            return False

    def _call_and_get_response_in_lines(self, command, line_count):
        """ Call to WeatherLink """
        self.connection.sendall(command.encode())
        crs = 0
        received = ""
        while crs < line_count:
            char = self.connection.recv(1)
            received += char.decode()

            if char == b'\r':
                crs += 1

        lines = received.split('\n\r')

        if lines[-1] == "":
            del lines[-1]

        if len(lines) == line_count:
            return lines
        else:
            return [None] * line_count

    def set_speed(self, new_speed):
        """
           Set WeatherLink communication speed
        Args:
           new_speed: new serial communication speed rate
           Valid values are 1200, 2400, 4800, 9600, 14400 and 19200
        """
        if new_speed in [1200, 2400, 4800, 9600, 14400, 19200]:
            lines = self._call_and_get_response_in_lines(
                    "BAUD " + str(new_speed) + "\n", 2)
            response = lines[1]
            return response == "OK"
        else:
            return False

    def set_archive_interval(self, interval):
        """
           Set the console archive interval
        Args:
           interval: data collection period in minutes
           Valid values are 1, 5, 10, 15, 30, 60 and 120
        """
        if interval in [1, 5, 10, 15, 30, 60, 120]:
            lines = self._call_and_get_response_in_lines(
                    "SETPER " + str(interval) + "\n", 2)
            response = lines[1]
            return response == "OK"
        else:
            return False

    def get_station_type(self):
        """ Get station type """
        command = "WRD\x12\x4d\n"
        response = self._call_and_get_fixed_size_response(
                   command, self.STATION_VERSION_SIZE_IN_BYTES)
        if response is False:
            return False
        else:
            self.station_type = response[1]
            return self.station_type

    def station_type_supported(self):
        station_type = self.get_station_type()
        return (
                station_type == self.VANTAGE_PRO_ID or
                station_type == self.VANTAGE_VUE_ID
               )

    def get_firmware_version(self):
        """ Get firmware version """
        if self.station_type_supported() is True:
            lines = self._call_and_get_response_in_lines("NVER" + "\n", 3)
            self.firmware_version = lines[2]
        return self.firmware_version

    def firmware_version_supported(self):
        return self.get_firmware_version() == self.FIRMWARE_VERSION

    def get_firmware_date(self):
        """ Get firmware date """
        lines = self._call_and_get_response_in_lines("VER" + "\n", 3)
        self.firmware_date = lines[2]
        return self.firmware_date

    def firmware_date_supported(self):
        return self.get_firmware_date() == self.FIRMWARE_DATE

    def test_call(self):
        """ Test command connection """
        lines = self._call_and_get_response_in_lines("TEST" + "\n", 2)

        return lines[1] == "TEST"

    def set_time(self, year, month, day, hour, minute, second):
        """ Set date/time on weather station """
        response = self._call_and_get_fixed_size_response(
                   "SETTIME" + "\n", self.ACK_SIZE)
        if response == self.ACK:
            datetime = (
                        struct.pack('B', second) +
                        struct.pack('B', minute) +
                        struct.pack('B', hour) +
                        struct.pack('B', day) +
                        struct.pack('B', month) +
                        struct.pack('B', year - 1900)
                       )
            crc = struct.pack('H', self._calculate_crc(datetime))
            all_data = datetime + bytes(reversed(crc))
            self.connection.sendall(all_data)
            response = self.connection.recv(self.ACK_SIZE)
            return response == self.ACK
        else:
            return False

    def set_time_zone(self, zone):
        """ Set time zone on weather station """
        if self._eewr(self.EEPROM_TIME_ZONE_ADDRESS, zone):
            return self._eewr(self.EEPROM_GMT_OR_ZONE_ADDRESS, 0)
        else:
            return False

    def disable_daylight_savings(self):
        """ Disable daylight savings on weather station """
        if self._eewr(self.EEPROM_DAYLIGHT_SAVINGS_ADDRESS, 0):
            return self._eewr(self.EEPROM_MANUAL_OR_AUTO_ADDRESS, 1)
        else:
            return False

    def _eewr(self, address, data):
        """ Write byte to EEPROM """
        lines = self._call_and_get_response_in_lines(
                (
                 "EEWR " + format(address, "X") + " " +
                 format(data, "X") + "\n"
                ), 2)
        response = lines[1]
        return 'OK' == response

    def current_data(self):
        """ Get current data """
        response = self._call_and_get_fixed_size_response(
                   "LPS 2 1" + "\n", self.ACK_SIZE)
        if response == self.ACK:
            loop2_packet = self.connection.recv(
                           self.LOOP2_PACKET_SIZE_IN_BYTES)
            data = self.parse_loop2(loop2_packet)
            return data
        else:
            return False

    @staticmethod
    def _calculate_crc(data):
        """
            Calculate CRC according to CRC-CCITT standard.
        """
        crc = 0
        crc_table = [
            0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50a5, 0x60c6, 0x70e7,
            0x8108, 0x9129, 0xa14a, 0xb16b, 0xc18c, 0xd1ad, 0xe1ce, 0xf1ef,
            0x1231, 0x0210, 0x3273, 0x2252, 0x52b5, 0x4294, 0x72f7, 0x62d6,
            0x9339, 0x8318, 0xb37b, 0xa35a, 0xd3bd, 0xc39c, 0xf3ff, 0xe3de,
            0x2462, 0x3443, 0x0420, 0x1401, 0x64e6, 0x74c7, 0x44a4, 0x5485,
            0xa56a, 0xb54b, 0x8528, 0x9509, 0xe5ee, 0xf5cf, 0xc5ac, 0xd58d,
            0x3653, 0x2672, 0x1611, 0x0630, 0x76d7, 0x66f6, 0x5695, 0x46b4,
            0xb75b, 0xa77a, 0x9719, 0x8738, 0xf7df, 0xe7fe, 0xd79d, 0xc7bc,
            0x48c4, 0x58e5, 0x6886, 0x78a7, 0x0840, 0x1861, 0x2802, 0x3823,
            0xc9cc, 0xd9ed, 0xe98e, 0xf9af, 0x8948, 0x9969, 0xa90a, 0xb92b,
            0x5af5, 0x4ad4, 0x7ab7, 0x6a96, 0x1a71, 0x0a50, 0x3a33, 0x2a12,
            0xdbfd, 0xcbdc, 0xfbbf, 0xeb9e, 0x9b79, 0x8b58, 0xbb3b, 0xab1a,
            0x6ca6, 0x7c87, 0x4ce4, 0x5cc5, 0x2c22, 0x3c03, 0x0c60, 0x1c41,
            0xedae, 0xfd8f, 0xcdec, 0xddcd, 0xad2a, 0xbd0b, 0x8d68, 0x9d49,
            0x7e97, 0x6eb6, 0x5ed5, 0x4ef4, 0x3e13, 0x2e32, 0x1e51, 0x0e70,
            0xff9f, 0xefbe, 0xdfdd, 0xcffc, 0xbf1b, 0xaf3a, 0x9f59, 0x8f78,
            0x9188, 0x81a9, 0xb1ca, 0xa1eb, 0xd10c, 0xc12d, 0xf14e, 0xe16f,
            0x1080, 0x00a1, 0x30c2, 0x20e3, 0x5004, 0x4025, 0x7046, 0x6067,
            0x83b9, 0x9398, 0xa3fb, 0xb3da, 0xc33d, 0xd31c, 0xe37f, 0xf35e,
            0x02b1, 0x1290, 0x22f3, 0x32d2, 0x4235, 0x5214, 0x6277, 0x7256,
            0xb5ea, 0xa5cb, 0x95a8, 0x8589, 0xf56e, 0xe54f, 0xd52c, 0xc50d,
            0x34e2, 0x24c3, 0x14a0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
            0xa7db, 0xb7fa, 0x8799, 0x97b8, 0xe75f, 0xf77e, 0xc71d, 0xd73c,
            0x26d3, 0x36f2, 0x0691, 0x16b0, 0x6657, 0x7676, 0x4615, 0x5634,
            0xd94c, 0xc96d, 0xf90e, 0xe92f, 0x99c8, 0x89e9, 0xb98a, 0xa9ab,
            0x5844, 0x4865, 0x7806, 0x6827, 0x18c0, 0x08e1, 0x3882, 0x28a3,
            0xcb7d, 0xdb5c, 0xeb3f, 0xfb1e, 0x8bf9, 0x9bd8, 0xabbb, 0xbb9a,
            0x4a75, 0x5a54, 0x6a37, 0x7a16, 0x0af1, 0x1ad0, 0x2ab3, 0x3a92,
            0xfd2e, 0xed0f, 0xdd6c, 0xcd4d, 0xbdaa, 0xad8b, 0x9de8, 0x8dc9,
            0x7c26, 0x6c07, 0x5c64, 0x4c45, 0x3ca2, 0x2c83, 0x1ce0, 0x0cc1,
            0xef1f, 0xff3e, 0xcf5d, 0xdf7c, 0xaf9b, 0xbfba, 0x8fd9, 0x9ff8,
            0x6e17, 0x7e36, 0x4e55, 0x5e74, 0x2e93, 0x3eb2, 0x0ed1, 0x1ef0,
        ]
        list_bytes = list(bytearray(data))
        for i, byte in enumerate(list_bytes):
            key = ((crc >> 8) ^ byte)
            crc = crc_table[key] ^ ((crc << 8) % 65536)
        return crc

    @staticmethod
    def _datetime_to_bytes(year, month, day, hour, minute):
        """
            Represent date/time as bytes
        """
        date_stamp = day + month * 32 + (year - 2000) * 512
        time_stamp = (100 * hour) + minute
        return struct.pack('H', date_stamp) + struct.pack('H', time_stamp)

    @staticmethod
    def _bytes_to_datetime(bytes):
        """
            Convert bytes into date/time
        """
        date = int(struct.unpack('H', bytes[0:2])[0])
        time = int(struct.unpack('H', bytes[2:4])[0])
        year = int((date / 512) + 2000)
        month = int(date % 512 / 32)
        day = int(date % 32)
        hour = int(time / 100)
        minute = int(time % 100)
        return datetime(year, month, day, hour, minute)

    def dmpaft(self, year, month, day, hour, minute):
        """
            Request archive dump after the date/time
        """
        response = self._call_and_get_fixed_size_response(
                   "DMPAFT" + "\n", self.ACK_SIZE)
        if response == self.ACK:
            datetime = self._datetime_to_bytes(year, month, day, hour, minute)
            crc = struct.pack('H', self._calculate_crc(datetime))
            all_data = datetime + bytes(reversed(crc))
            self.connection.sendall(all_data)
            response = self.connection.recv(self.ACK_SIZE)
            return response == self.ACK
        else:
            return False

    def pages_info(self):
        """
            Returns total number of pages to follow
            and position of first record
        """
        pages_info = self.connection.recv(self.PAGES_INFO_SIZE_IN_BYTES)
        crc = self._calculate_crc(pages_info)
        if crc == 0:
            pages = struct.unpack('h', pages_info[0:2])[0]
            record_number = struct.unpack('h', pages_info[2:4])[0]
            pages_info = [pages, record_number]
            self.connection.sendall(self.ACK)
            return pages_info
        else:
            self.connection.sendall(self.ESC)
            return False

    def read_page(self, page_number, data_page, pages_info):
        """
            Read single data page received from the station
        """
        records = []
        previous_record_time = None
        crc = self._calculate_crc(data_page)
        if crc == 0:
            if page_number == 0:
                record_position = pages_info[1] * self.RECORD_SIZE + 1
            else:
                record_position = 1
            last = page_number == pages_info[0] - 1
            stop = self.RECORD_SIZE * self.RECORDS_PER_PAGE
            for i in range(record_position, stop, self.RECORD_SIZE):
                record = data_page[i:i + self.RECORD_SIZE]
                if not set(record) == {255}:
                    try:
                        parsed_record = self.parse_dmp(record)
                        if last:
                            if (
                                previous_record_time is None or
                                previous_record_time < parsed_record["datetime"]
                               ):
                                records.append(parsed_record)
                                previous_record_time = parsed_record["datetime"]
                        else:
                            records.append(parsed_record)
                            previous_record_time = parsed_record["datetime"]
                    except ValueError:
                        pass
            command = self.ACK
        else:
            command = self.NAK
        self.connection.sendall(command)
        return records

    def data_since(self, year, month, day, hour, minute):
        """
            Downloads the data records after particular date and time
        """
        dmpaft = self.dmpaft(year, month, day, hour, minute)
        if dmpaft is True:
            pages_info = self.pages_info()
            if pages_info is False:
                return False
            total_pages = pages_info[0] - 1
            data = []
            page_number = 0
            while page_number <= total_pages:
                page_size = (
                             self.SEQUENCE_NUMBER +
                             self.RECORD_SIZE * self.RECORDS_PER_PAGE +
                             self.UNUSED_PAGE_BYTES +
                             self.CRC_BYTES
                            )
                data_page = self.connection.recv(page_size)
                records = self.read_page(page_number, data_page, pages_info)
                if len(records) > 0:
                    data.extend(records)
                    page_number += 1
            return data
        else:
            return False

    def all_data(self):
        """
            Download the entire archive memory
        """
        year = 2003
        day = 6
        month = 6
        hour = 9
        minute = 30
        return self.data_since(year, month, day, hour, minute)

    @staticmethod
    def parse(data, name, format, position, length, divider, dashvalue, array,
              offset=0, xlat=None):
        """
            Parse a single value according to a format
        """
        value = struct.unpack(format, data[position:position + length])[0]

        if value != dashvalue:
            if divider != 1:
                value = value / divider
            if offset != 0:
                value = value + offset
            if xlat is None:
                array.update({name: value})
            else:
                if value in xlat:
                    array.update({name: xlat[value]})

    def parse_dmp(self, record):
        """
            Parse DMP record received from the station
        """
        array = {
            'datetime': self._bytes_to_datetime(record[0:4])
        }
        self.parse(record, 'outside_temperature',        'h',  4, 2,   10,
                   32767, array)
        self.parse(record, 'high_out_temperature',       'h',  6, 2,   10,
                   -32768, array)
        self.parse(record, 'low_out_temperature',        'h',  8, 2,   10,
                   32767, array)
        self.parse(record, 'rainfall',                   'H', 10, 2,    1,
                   0, array)
        self.parse(record, 'high_rain_rate',             'H', 12, 2,    1,
                   0, array)
        self.parse(record, 'barometer',                  'H', 14, 2, 1000,
                   0, array)
        self.parse(record, 'solar_radiation',            'H', 16, 2,    1,
                   32767, array)
        self.parse(record, 'number_of_wind_samples',     'H', 18, 2,    1,
                   0, array)
        self.parse(record, 'inside_temperature',         'h', 20, 2,   10,
                   32767, array)
        self.parse(record, 'inside_humidity',            'B', 22, 1,    1,
                   255, array)
        self.parse(record, 'outside_humidity',           'B', 23, 1,    1,
                   255, array)
        self.parse(record, 'average_wind_speed',         'B', 24, 1,    1,
                   255, array)
        self.parse(record, 'high_wind_speed',            'B', 25, 1,    1,
                   0, array)
        self.parse(record, 'direction_of_hi_wind_speed', 'B', 26, 1,    1,
                   32767, array, 0,
                   {
                    0: 'N',
                    1: 'NNE',
                    2: 'NE',
                    3: 'NEE',
                    4: 'E',
                    5: 'SEE',
                    6: 'SE',
                    7: 'SSE',
                    8: 'S',
                    9: 'SSW',
                    10: 'SW',
                    11: 'SWW',
                    12: 'W',
                    13: 'NWW',
                    14: 'NW',
                    15: 'NNW'
                   })
        self.parse(record, 'prevailing_wind_direction',  'B', 27, 1,    1,
                   32767, array, 0,
                   {
                    0: 'N',
                    1: 'NNE',
                    2: 'NE',
                    3: 'NEE',
                    4: 'E',
                    5: 'SEE',
                    6: 'SE',
                    7: 'SSE',
                    8: 'S',
                    9: 'SSW',
                    10: 'SW',
                    11: 'SWW',
                    12: 'W',
                    13: 'NWW',
                    14: 'NW',
                    15: 'NNW'
                   })
        self.parse(record, 'average_uv',                 'B', 28, 1,   10,
                   255, array)
        self.parse(record, 'et',                         'B', 29, 1, 1000,
                   0, array)
        self.parse(record, 'high_solar_radiation',       'H', 30, 2,    1,
                   0, array)
        self.parse(record, 'high_uv',                    'B', 32, 1,    1,
                   32767, array)
        self.parse(record, 'forecast_rule',              'B', 33, 1,    1,
                   193, array)
        self.parse(record, 'leaf_temperature1',          'b', 34, 1,    1,
                   -1, array, 90)
        self.parse(record, 'leaf_temperature2',          'b', 35, 1,    1,
                   -1, array, 90)
        self.parse(record, 'leaf_wetnesses1',            'B', 36, 1,    1,
                   255, array)
        self.parse(record, 'leaf_wetnesses2',            'B', 37, 1,    1,
                   255, array)
        self.parse(record, 'soil_temperatures1',         'b', 38, 1,    1,
                   -1, array, 90)
        self.parse(record, 'soil_temperatures2',         'b', 39, 1,    1,
                   -1, array, 90)
        self.parse(record, 'soil_temperatures3',         'b', 40, 1,    1,
                   -1, array, 90)
        self.parse(record, 'soil_temperatures4',         'b', 41, 1,    1,
                   -1, array, 90)
        self.parse(record, 'extra_humidity1',            'B', 43, 1,    1,
                   255, array)
        self.parse(record, 'extra_humidity2',            'B', 44, 1,    1,
                   255, array)
        self.parse(record, 'extra_temperature1',         'b', 45, 1,    1,
                   -1, array, 90)
        self.parse(record, 'extra_temperature2',         'b', 46, 1,    1,
                   -1, array, 90)
        self.parse(record, 'extra_temperature3',         'b', 47, 1,    1,
                   -1, array, 90)
        self.parse(record, 'soil_moisture1',             'B', 48, 1,    1,
                   255, array)
        self.parse(record, 'soil_moisture2',             'B', 49, 1,    1,
                   255, array)
        self.parse(record, 'soil_moisture3',             'B', 50, 1,    1,
                   255, array)
        self.parse(record, 'soil_moisture4',             'B', 51, 1,    1,
                   255, array)
        return array

    def parse_loop2(self, packet):
        """
            Parse LOOP2 packet received from the station
        """
        array = {}
        self.parse(packet, 'bar_trend',              'b',  3, 1,    1,    -1,
                   array, 0,
                   {
                    -60: 'Falling Rapidly',
                    -20: 'Falling Slowly',
                    0: 'Steady',
                    20: 'Rising Slowly',
                    60: 'Rising Rapidly'
                   })
        self.parse(packet, 'barometer',              'H',  7, 2, 1000,     0,
                   array)
        self.parse(packet, 'inside_temperature',     'h',  9, 2,   10,     0,
                   array)
        self.parse(packet, 'inside_humidity',        'B', 11, 1,    1,   255,
                   array)
        self.parse(packet, 'outside_temperature',    'h', 12, 2,   10, 32767,
                   array)
        self.parse(packet, 'wind_speed',             'B', 14, 1,    1,   255,
                   array)
        self.parse(packet, 'wind_direction',         'H', 16, 2,    1,     0,
                   array)
        self.parse(packet, 'ten_min_avg_wind_speed', 'H', 18, 2,    1, 32767,
                   array)
        self.parse(packet, 'two_min_avg_wind_speed', 'H', 20, 2,    1, 32767,
                   array)
        self.parse(packet, 'ten_min_wind_gust',      'H', 22, 2,    1, 32767,
                   array)
        self.parse(packet, 'wind_direction_gust',    'H', 24, 2,    1, 32767,
                   array)
        self.parse(packet, 'dew_point',              'h', 30, 2,    1,   255,
                   array)
        self.parse(packet, 'outside_humidity',       'B', 33, 1,    1,   255,
                   array)
        self.parse(packet, 'heat_index',             'h', 35, 2,    1,   255,
                   array)
        self.parse(packet, 'wind_chill',             'h', 37, 2,    1,   255,
                   array)
        self.parse(packet, 'thsw_index',             'h', 39, 2,    1,   255,
                   array)
        self.parse(packet, 'rain_rate',              'H', 41, 2,    1, 32767,
                   array)
        self.parse(packet, 'uv',                     'B', 43, 1,    1,   255,
                   array)
        self.parse(packet, 'solar_radiation',        'H', 44, 2,    1, 32767,
                   array)
        self.parse(packet, 'storm_rain',             'H', 46, 2,    1, 32767,
                   array)
        self.parse(packet, 'daily_rain',             'H', 50, 2,    1, 32767,
                   array)
        self.parse(packet, 'last_fifteen_min_rain',  'H', 52, 2,    1, 32767,
                   array)
        self.parse(packet, 'last_hour_rain',         'H', 54, 2,    1, 32767,
                   array)
        self.parse(packet, 'daily_et',               'H', 56, 2, 1000,     0,
                   array)
        self.parse(packet, 'last_24_hour_rain',      'H', 58, 2,    1, 32767,
                   array)
        return array

    def __del__(self):
        self.disconnect()
