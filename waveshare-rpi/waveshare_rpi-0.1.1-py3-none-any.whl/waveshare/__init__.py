import serial
import pynmea2
import threading

ser = None
lock = threading.Lock()
thread = None

gga = None
gsa = None
gsv = None
rmc = None


def get_gga():
    with lock:
        return gga


def __set_gga(val):
    global gga
    gga = val


def get_gsa():
    with lock:
        return gsa


def __set_gsa(val):
    global gsa
    gsa = val


def get_gsv():
    with lock:
        return gsv


def __set_gsv(val):
    global gsv
    gsv = val


def get_rmc():
    with lock:
        return rmc


def __set_rmc(val):
    global rmc
    rmc = val


def start(device):
    global ser
    global thread

    ser = serial.Serial(device, 19200, timeout=1)
    ser.write(str.encode("AT+CGNSPWR=1\n"))  # turn on the power for GPS

    # TODO: figure out if/why this is needed
    ser.write(str.encode("AT+CGNSSEQ=\"RMC\"\n"))  # define the last NMEA sentence that parsed

    ser.write(str.encode("AT+CGNSTST=1\n"))  # start gps streaming to serial

    def read_data():

        while True:
            line = ser.read_until(str.encode("\n")).decode()

            headers = {
                "$GNGGA": __set_gga,
                "$GPGSA": __set_gsa,
                "$GPGSV": __set_gsv,
                "$GNRMC": __set_rmc,
            }

            if line[:6] in headers.keys():
                with lock:
                    headers[line[:6]](pynmea2.parse(line))

    thread = threading.Thread(target=read_data)
    thread.daemon = True
    thread.start()


def stop():
    with lock:
        if ser is not None:
            ser.write(str.encode("AT+CGNSTST=0\n"))
        if thread is not None:
            thread.stop()
