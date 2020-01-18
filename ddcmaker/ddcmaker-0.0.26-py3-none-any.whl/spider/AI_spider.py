from ddcmaker.public.advanced_mode import ad_mode
from ddcmaker.linux.armv7l.pro_name_list import spider
import sys


class cv_color(ad_mode):
    def __init__(self):
        super().__init__()
        self.Xpath = "python3 /home/pi/hexapod/"
        self.list = spider
        self.cap = " no_display "
        self.color = ["red", "green", "blue"]

    def identifying(self):
        print("识别颜色(红色点头，蓝绿摇头)")
        self.name = self.list[0] + self.cap
        super().run()

    def tracking(self, color="red"):
        if color in self.color:
            print("云台追踪")  # 可行
            self.name = self.list[1] + self.cap+color
            super().run()
        else:
            raise Exception("函数 %s" % sys._getframe().f_code.co_name + "参数的颜色超出范围，请在"+str(self.color)+"中选择，不传参默认" + color)

    def follow(self, color="red"):
        print("机体跟随")  # 可行
        self.name = self.list[2] + self.cap+color
        super().run()

    def linefollow(self):
        print("自动巡线")
        self.name = self.list[3] + self.cap
        super().run()

    def balance(self):
        print("自动平衡")
        self.name = self.list[4]
        super().run()

    def sonar(self):
        print("自动避障")
        self.name = self.list[5]
        super().run()
