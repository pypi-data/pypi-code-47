from ddcmaker.linux.armv7l import get_equipment_type as ge

if ge.get_eq_type() == 2:
    from ddcmaker.human_code.config_vin_temp import *


    class read_state(object):
        def read_vin(self, id=1):
            if id > 16:
                print("你输入的参数有误，请保证参数在1-16之间")
                return False
            else:
                voltage = (css.serial_servo_read_vin(id) / 1000.00)
                return voltage

        def read_temp(self, id=1):
            if id > 16:
                print("你输入的参数有误，请保证参数在1-16之间")
                return False
            else:
                temperature = (css.serial_servo_read_temp(id))
                return temperature

        def set_danger_vin(self, id=1, underv=10.0):
            if id > 16:
                print("你输入的参数有误，请保证参数在1-16之间")
                return False
            else:
                if self.read_vin(id) < underv:
                    print("电压过低请及时充电！")

        def set_danger_temp(self, id=1, undertem=85.0):
            if id > 16:
                print("你输入的参数有误，请保证参数在1-16之间")
                return False
            else:
                if self.read_temp(id) > undertem:
                    print("温度过高，请及时停止运行舵机！")

        def set_warnning(self, musicpath="/home/pi/Music/jiuzhangji.mp3"):
            print("宝宝饿了，快给我点吃的吧")
            import os
            os.system("sudo mplayer  " + musicpath)

        def set_action(self):
            print("没力气了")
            from ddcmaker import Robot
            rb = Robot()
            rb.down()
