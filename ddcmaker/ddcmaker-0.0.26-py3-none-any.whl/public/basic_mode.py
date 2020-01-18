"""
基础模板
"""
import ddcmaker
import time
from ddcmaker.public.Serial_Servo_Signal import serial_signal
from ddcmaker.public import PWMServo


class ba_mode(object):
    def __int__(self):
        self.__version__ = ddcmaker.__version__
        self.sleeptime = 0
        self.name = ""
        self.nodid = 1
        self.shakingid = 2
        self.Interval_time = 200
        self.start_angle = 1200
        self.homing_angle = 1500
        self.end_angle = 1700
        self.SSR = serial_signal()

    def run_action(self, actnum, step=1, msg_txt=""):
        for i in range(step):
            self.SSR.run_ActionGroup(actnum, 1)
            time.sleep(self.sleeptime)
            self.describe(msg_txt)

    def describe(self, msg_txt):
        print(self.name+msg_txt)

    def shaking_head(self, step=1):
        for i in range(step):
            PWMServo.setServo(self.shakingid, self.start_angle, self.Interval_time)
            time.sleep(self.Interval_time/1000)
            PWMServo.setServo(self.shakingid, self.end_angle, self.Interval_time)
            time.sleep(self.Interval_time/1000)
            PWMServo.setServo(self.shakingid, self.homing_angle, self.Interval_time/2)
            time.sleep(self.Interval_time / 200)
            self.describe("摇头")

    def nod(self, step=1):
        for i in range(step):
            PWMServo.setServo(self.nodid, self.start_angle, self.Interval_time)
            time.sleep(self.Interval_time/1000)
            PWMServo.setServo(self.nodid, self.end_angle, self.Interval_time)
            time.sleep(self.Interval_time/1000)
            PWMServo.setServo(self.nodid, self.homing_angle, self.Interval_time/2)
            time.sleep(self.Interval_time / 200)
            self.describe("点头")

    def init_head(self):
        PWMServo.setServo(self.nodid, self.homing_angle, self.Interval_time / 2)
        time.sleep(self.Interval_time / 200)
        PWMServo.setServo(self.shakingid, self.homing_angle, self.Interval_time)
        time.sleep(self.Interval_time / 1000)
