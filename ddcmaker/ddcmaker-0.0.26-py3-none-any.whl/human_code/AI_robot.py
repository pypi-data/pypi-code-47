from ddcmaker.public.advanced_mode import ad_mode
from ddcmaker.linux.armv7l.pro_name_list import human_code
import sys


class cv_mode(ad_mode):
    def __init__(self):
        super().__init__()
        self.Xpath = "python3 /home/pi/human_code/"
        self.list = human_code
        self.cap = " no_display "
        self.color = ["red", "green", "blue"]

    def automatic_shot(self):
        print("自动射门")
        self.name = self.list[0]+self.cap
        super().run()

    def identifying(self):
        print("颜色识别(红色点头，蓝绿摇头)")
        self.name = self.list[1]+self.cap
        super().run()

    def find_hand(self):
        print("手势识别")
        self.name = self.list[2]+self.cap
        super().run()

    def linefollow(self):
        print("自动巡线")
        self.name = self.list[3]+self.cap
        super().run()

    def tracking(self, color):
        if color in self.color:
            print("云台追踪")
            self.name = self.list[4]+self.cap+color
            super().run()
        else:
            raise Exception("函数 %s" % sys._getframe().f_code.co_name + "参数的颜色超出范围，请在"+str(self.color)+"中选择，不传参默认"+color)

