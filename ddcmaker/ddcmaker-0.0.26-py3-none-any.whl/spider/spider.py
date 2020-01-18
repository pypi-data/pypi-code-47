# -*- utf-8 -*-
"""蜘蛛侠来了"""
from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.spider.SSR import serial_spider
from ddcmaker.public.basic_mode import ba_mode

if ge.get_eq_type() == 3:

    class spider(ba_mode):
        def __init__(self):
            super().__init__()
            self.sleeptime = 1
            self.name = "蜘蛛"
            self.SSR = serial_spider()
#----------------------------------------------------------------

        def init_body(self):
            self.run_action("25")

        def creeping(self, step):
            self.run_action('0', step, "匍匐")

        def creeping_forward(self, step):
            self.run_action('1', step, "匍匐前进")

        def creeping_backward(self, step):
            self.run_action('2', step, "匍匐后退")

        def creeping_left(self, step):
            self.run_action('3', step, "匍匐左转")

        def creeping_right(self, step):
            self.run_action('4', step, "匍匐右转")
#-----------------------------------------------------------------

        def stand(self, step):
            self.run_action('25', step, "站立")

        def forward(self, step):
            self.run_action('26', step, "前进")

        def backward(self, step):
            self.run_action('27', step, "后退")

        def left(self, step):
            self.run_action('28', step, "左转")

        def right(self, step):
            self.run_action('29', step, "右转")
# -----------------------------------------------------------------

        def towering(self, step):
            self.run_action('34', step, "耸立")

        def towering_forward(self, step):
            self.run_action('35', step, "耸立前进")

        def towering_backward(self, step):
            self.run_action('36', step, "耸立后退")

        def towering_left(self, step):
            self.run_action('37', step, "耸立左转")

        def towering_right(self, step):
            self.run_action('38', step, "耸立右转")
# -----------------------------------------------------------------

        def forward_flutter(self, step):
            self.run_action('5', step, "前扑")

        def backward_flutter(self, step):
            self.run_action('6', step, "后扑")

        def left_shift(self, step):
            self.run_action('7', step, "左移")

        def right_shift(self, step):
            self.run_action('8', step, "右移")

        def twisting(self, step):
            self.run_action('9', step, "扭身")

        def fighting(self, step):
            self.run_action('10', step, "战斗")

        def break_forward(self, step):
            self.run_action('41', step, "碎步前进")

        def minor_steering(self, step):
            self.run_action('40', step, "小转向(右)")
