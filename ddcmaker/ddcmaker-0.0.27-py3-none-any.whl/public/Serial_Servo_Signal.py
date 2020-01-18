#!/usr/bin/env python3
# encoding: utf-8
from ddcmaker.public.EP626 import *
import time
import os
import sqlite3 as sql
import threading

# from hwax import HWAX
"""基类"""
runningAction = False
stopRunning = False
online_action_num = None
online_action_times = -1
update_ok = False
action_group_finish = True


class serial_signal(object):
    def __init__(self):
        self.Xpath = ""

    def serial_setServo(self, s_id, pos, s_time):
        if pos > 1000:
            pos = 1000
        elif pos < 0:
            pos = 0
        else:
            pass
        if s_time > 30000:
            s_time = 30000
        elif s_time < 10:
            s_time = 10
        ssc.serial_serro_wirte_cmd(s_id, ssc.LOBOT_SERVO_MOVE_TIME_WRITE, pos, s_time)

    def setDeviation(self, servoId, d):
        global runningAction
        if servoId < 0 or servoId > 19:
            return
        if d < -200 or d > 200:
            return
        if runningAction is False:
            config_serial_servo.serial_servo_set_deviation(servoId, d)

    def stop_servo(self):
        for i in range(18):
            config_serial_servo.serial_servo_stop(i + 1)

    def stop_action_group(self):
        global stopRunning, online_action_num, online_action_times, update_ok
        update_ok = False
        stopRunning = True
        online_action_num = None
        online_action_times = -1
        time.sleep(0.1)

    def action_finish(self):
        global action_group_finish
        return action_group_finish

    def runAction(self, actNum):
        global runningAction
        global stopRunning
        global online_action_times
        if actNum is None:
            return
        hwaxNum = self.Xpath + actNum + ".hwax"
        actNum = self.Xpath + actNum + ".d6a"

        if os.path.exists(hwaxNum) is True:
            if runningAction is False:
                runningAction = True
                ssc.portWrite()
                hwax = HWAX(hwaxNum, ssc.serialHandle)
                hwax.reset()
                while True:
                    if stopRunning is True:
                        stopRunning = False
                        print('stop')
                        break
                    ret = hwax.next()
                    if ret is None:
                        hwax.reset()
                        break
                hwax.close()
                runningAction = False

        elif os.path.exists(actNum) is True:
            if runningAction is False:
                runningAction = True
                ag = sql.connect(actNum)
                cu = ag.cursor()
                cu.execute("select * from ActionGroup")
                while True:
                    act = cu.fetchone()
                    if stopRunning is True:
                        stopRunning = False
                        print('stop')
                        break
                    if act is not None:
                        for i in range(0, len(act) - 2, 1):
                            self.serial_setServo(i + 1, act[2 + i], act[1])
                        time.sleep(float(act[1]) / 1000.0)
                    else:
                        break
                runningAction = False

                cu.close()
                ag.close()
        else:
            runningAction = False
            print("未能找到动作组文件")

    def run_ActionGroup(self, actNum, times):
        global runningAction
        global stopRunning
        global action_group_finish

        d6aNum = self.Xpath + actNum + ".d6a"
        hwaxNum = self.Xpath + actNum + ".hwax"

        stopRunning = False
        if action_group_finish:
            if times == 0:
                times = 1
                state = False
            else:
                times = abs(times)
                state = True
            if os.path.exists(hwaxNum) is True:
                ssc.portWrite()
                hwax = HWAX(hwaxNum, ssc.serialHandle)
                hwax.reset()
                while times:
                    if state:
                        times -= 1
                    if runningAction is False:
                        runningAction = True
                        while True:
                            if stopRunning is True:
                                runningAction = False
                                break
                            ret = hwax.next()
                            if ret is None:
                                runningAction = False
                                hwax.reset()
                                break
                    else:
                        break

            elif os.path.exists(d6aNum) is True:
                while times:
                    if state:
                        times -= 1
                    ag = sql.connect(d6aNum)
                    cu = ag.cursor()
                    cu.execute("select * from ActionGroup")
                    if runningAction is False:
                        runningAction = True
                        while True:
                            if stopRunning is True:
                                runningAction = False
                                cu.close()
                                ag.close()
                                break
                            act = cu.fetchone()
                            if act is not None:
                                for i in range(0, len(act) - 2, 1):
                                    self.serial_setServo(i + 1, act[2 + i], act[1])
                                time.sleep(float(act[1]) / 1000.0)
                            else:
                                runningAction = False
                                cu.close()
                                ag.close()
                                break
                    else:
                        break
            else:
                runningAction = False
                print("未能找到动作组文件")

    def online_thread_run_acting(self):
        global online_action_times, online_action_num, update_ok, action_group_finish
        while True:
            if update_ok:
                if online_action_times == 0:

                    self.runAction(online_action_num)
                    action_group_finish = False
                elif online_action_times > 0:

                    self.runAction(online_action_num)
                    online_action_times -= 1
                    action_group_finish = False
                    if online_action_times == 0:
                        online_action_times = -1
                else:

                    action_group_finish = True
                    time.sleep(0.01)
            else:
                action_group_finish = True
                time.sleep(0.01)

    def start_action_thread(self):
        th1 = threading.Thread(target=self.online_thread_run_acting)
        th1.setDaemon(True)
        th1.start()

    def change_action_value(self, actNum, actTimes):
        global online_action_times, online_action_num, update_ok, stopRunning

        online_action_times = actTimes
        online_action_num = actNum
        stopRunning = False
        update_ok = True


