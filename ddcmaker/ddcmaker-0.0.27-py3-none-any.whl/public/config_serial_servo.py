#!/usr/bin/python
# encoding: utf-8
from ddcmaker.public.__init__ import *
if ge.get_eq_type() == 3 or ge.get_eq_type() == 2:
    from ddcmaker.public.SerialServoCmd import *


    def serial_servo_set_id(oldid, newid):
        serial_serro_wirte_cmd(oldid, LOBOT_SERVO_ID_WRITE, newid)


    def serial_servo_read_id(id=None):
        while True:
            if id is None:
                serial_servo_read_cmd(0xfe, LOBOT_SERVO_ID_READ)
            else:
                serial_servo_read_cmd(id, LOBOT_SERVO_ID_READ)

            msg = serial_servo_get_rmsg(LOBOT_SERVO_ID_READ)
            if msg is not None:
                return msg


    def serial_servo_stop(id=None):

        serial_serro_wirte_cmd(id, LOBOT_SERVO_MOVE_STOP)


    def serial_servo_set_deviation(id, d=0):

        serial_serro_wirte_cmd(id, LOBOT_SERVO_ANGLE_OFFSET_ADJUST, d)
        serial_serro_wirte_cmd(id, LOBOT_SERVO_ANGLE_OFFSET_WRITE)


    def serial_servo_read_deviation(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_ANGLE_OFFSET_READ)

            msg = serial_servo_get_rmsg(LOBOT_SERVO_ANGLE_OFFSET_READ)
            if msg is not None:
                return msg


    def serial_servo_set_angle_limit(id, low, high):
        serial_serro_wirte_cmd(id, LOBOT_SERVO_ANGLE_LIMIT_WRITE, low, high)


    def serial_servo_read_angle_limit(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_ANGLE_LIMIT_READ)
            msg = serial_servo_get_rmsg(LOBOT_SERVO_ANGLE_LIMIT_READ)
            if msg is not None:
                return msg


    def serial_servo_set_vin_limit(id, low, high):
        serial_serro_wirte_cmd(id, LOBOT_SERVO_VIN_LIMIT_WRITE, low, high)


    def serial_servo_read_vin_limit(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_VIN_LIMIT_READ)
            msg = serial_servo_get_rmsg(LOBOT_SERVO_VIN_LIMIT_READ)
            if msg is not None:
                return msg


    def serial_servo_set_max_temp(id, m_temp):
        serial_serro_wirte_cmd(id, LOBOT_SERVO_TEMP_MAX_LIMIT_WRITE, m_temp)


    def serial_servo_read_temp_limit(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_TEMP_MAX_LIMIT_READ)
            msg = serial_servo_get_rmsg(LOBOT_SERVO_TEMP_MAX_LIMIT_READ)
            if msg is not None:
                return msg


    def serial_servo_read_pos(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_POS_READ)
            msg = serial_servo_get_rmsg(LOBOT_SERVO_POS_READ)
            if msg is not None:
                return msg


    def serial_servo_read_temp(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_TEMP_READ)
            msg = serial_servo_get_rmsg(LOBOT_SERVO_TEMP_READ)
            if msg is not None:
                return msg


    def serial_servo_read_vin(id):
        while True:
            serial_servo_read_cmd(id, LOBOT_SERVO_VIN_READ)
            msg = serial_servo_get_rmsg(LOBOT_SERVO_VIN_READ)
            if msg is not None:
                return msg


    def serial_servo_rest_pos(oldid):

        serial_servo_set_deviation(oldid, 0)
        time.sleep(0.1)
        serial_serro_wirte_cmd(oldid, LOBOT_SERVO_MOVE_TIME_WRITE, 500, 100)


    def serial_servo_set_pos(oldid, pos, time):
        serial_serro_wirte_cmd(oldid, LOBOT_SERVO_MOVE_TIME_WRITE, pos, time)


    def serial_servo_set_speed(oldid, speed):
        serial_serro_wirte_cmd(oldid, LOBOT_SERVO_OR_MOTOR_MODE_WRITE, 1, speed)


    def serial_servo_set_servo_mode(oldid, mode):
        serial_serro_wirte_cmd(oldid, LOBOT_SERVO_OR_MOTOR_MODE_WRITE, mode, 0)


    def serial_servo_set_servo_load(oldid, mode):
        serial_serro_wirte_cmd(oldid, LOBOT_SERVO_LOAD_OR_UNLOAD_WRITE, mode)


    def show_servo_state():

        oldid = serial_servo_read_id()
        portRest()
        if oldid is not None:
            print('当前的舵机ID是：%d' % oldid)
            pos = serial_servo_read_pos(oldid)
            print('当前的舵机角度：%d' % pos)
            portRest()

            now_temp = serial_servo_read_temp(oldid)
            print('当前的舵机温度：%d°' % now_temp)
            portRest()

            now_vin = serial_servo_read_vin(oldid)
            print('当前的舵机电压：%dmv' % now_vin)
            portRest()

            d = serial_servo_read_deviation(oldid)
            print('当前的舵机偏差：%d' % ctypes.c_int8(d).value)
            portRest()

            limit = serial_servo_read_angle_limit(oldid)
            print('当前的舵机可控角度为%d-%d' % (limit[0], limit[1]))
            portRest()

            vin = serial_servo_read_vin_limit(oldid)
            print('当前的舵机报警电压为%dmv-%dmv' % (vin[0], vin[1]))
            portRest()

            temp = serial_servo_read_temp_limit(oldid)
            print('当前的舵机报警温度为50°-%d°' % temp)
            portRest()
        return oldid


    if __name__ == '__main__':
        serial_servo_set_deviation(1, 100)


