#!/usr/bin/python
# encoding: utf-8

from ddcmaker.linux.armv7l import get_equipment_type as ge

if ge.get_eq_type() == 3 or ge.get_eq_type() == 2:
    import serial
    import pigpio
    import time
    import ctypes

    LOBOT_SERVO_FRAME_HEADER = 0x55
    LOBOT_SERVO_MOVE_TIME_WRITE = 1
    LOBOT_SERVO_MOVE_TIME_READ = 2
    LOBOT_SERVO_MOVE_TIME_WAIT_WRITE = 7
    LOBOT_SERVO_MOVE_TIME_WAIT_READ = 8
    LOBOT_SERVO_MOVE_START = 11
    LOBOT_SERVO_MOVE_STOP = 12
    LOBOT_SERVO_ID_WRITE = 13
    LOBOT_SERVO_ID_READ = 14
    LOBOT_SERVO_ANGLE_OFFSET_ADJUST = 17
    LOBOT_SERVO_ANGLE_OFFSET_WRITE = 18
    LOBOT_SERVO_ANGLE_OFFSET_READ = 19
    LOBOT_SERVO_ANGLE_LIMIT_WRITE = 20
    LOBOT_SERVO_ANGLE_LIMIT_READ = 21
    LOBOT_SERVO_VIN_LIMIT_WRITE = 22
    LOBOT_SERVO_VIN_LIMIT_READ = 23
    LOBOT_SERVO_TEMP_MAX_LIMIT_WRITE = 24
    LOBOT_SERVO_TEMP_MAX_LIMIT_READ = 25
    LOBOT_SERVO_TEMP_READ = 26
    LOBOT_SERVO_VIN_READ = 27
    LOBOT_SERVO_POS_READ = 28
    LOBOT_SERVO_OR_MOTOR_MODE_WRITE = 29
    LOBOT_SERVO_OR_MOTOR_MODE_READ = 30
    LOBOT_SERVO_LOAD_OR_UNLOAD_WRITE = 31
    LOBOT_SERVO_LOAD_OR_UNLOAD_READ = 32
    LOBOT_SERVO_LED_CTRL_WRITE = 33
    LOBOT_SERVO_LED_CTRL_READ = 34
    LOBOT_SERVO_LED_ERROR_WRITE = 35
    LOBOT_SERVO_LED_ERROR_READ = 36

    pi = pigpio.pi()
    serialHandle = serial.Serial("/dev/ttyAMA0", 115200)


    def portInit():
        pi.set_mode(17, pigpio.OUTPUT)
        pi.write(17, 0)
        pi.set_mode(27, pigpio.OUTPUT)
        pi.write(27, 1)


    portInit()


    def portWrite():
        pi.write(27, 1)
        pi.write(17, 0)


    def portRead():
        pi.write(17, 1)
        pi.write(27, 0)


    def portRest():
        time.sleep(0.1)
        serialHandle.close()
        pi.write(17, 1)
        pi.write(27, 1)
        serialHandle.open()
        time.sleep(0.1)


    def checksum(buf):

        sum = 0x00
        for b in buf:
            sum += b
        sum = sum - 0x55 - 0x55
        sum = ~sum
        return sum & 0xff


    def serial_serro_wirte_cmd(id=None, w_cmd=None, dat1=None, dat2=None):

        portWrite()
        buf = bytearray(b'\x55\x55')
        buf.append(id)

        if dat1 is None and dat2 is None:
            buf.append(3)
        elif dat1 is not None and dat2 is None:
            buf.append(4)
        elif dat1 is not None and dat2 is not None:
            buf.append(7)

        buf.append(w_cmd)

        if dat1 is None and dat2 is None:
            pass
        elif dat1 is not None and dat2 is None:
            buf.append(dat1 & 0xff)
        elif dat1 is not None and dat2 is not None:
            buf.extend([(0xff & dat1), (0xff & (dat1 >> 8))])
            buf.extend([(0xff & dat2), (0xff & (dat2 >> 8))])

        buf.append(checksum(buf))

        serialHandle.write(buf)


    def serial_servo_read_cmd(id=None, r_cmd=None):
        portWrite()
        buf = bytearray(b'\x55\x55')
        buf.append(id)
        buf.append(3)
        buf.append(r_cmd)
        buf.append(checksum(buf))
        serialHandle.write(buf)
        time.sleep(0.00034)


    def serial_servo_get_rmsg(cmd):
        serialHandle.flushInput()
        portRead()
        time.sleep(0.005)
        count = serialHandle.inWaiting()
        if count != 0:
            recv_data = serialHandle.read(count)

            if recv_data[0] == 0x55 and recv_data[1] == 0x55 and recv_data[4] == cmd:
                # print 'ok'
                dat_len = recv_data[3]
                serialHandle.flushInput()
                if dat_len == 4:
                    return recv_data[5]
                elif dat_len == 5:
                    pos = 0xffff & (recv_data[5] | (0xff00 & ((recv_data[6]) << 8)))
                    return ctypes.c_int16(pos).value
                elif dat_len == 7:
                    pos1 = 0xffff & (recv_data[5] | (0xff00 & ((recv_data[6]) << 8)))
                    pos2 = 0xffff & (recv_data[7] | (0xff00 & ((recv_data[8]) << 8)))
                    return ctypes.c_int16(pos1).value, ctypes.c_int16(pos2).value
            else:
                return None
        else:
            serialHandle.flushInput()

            return None
