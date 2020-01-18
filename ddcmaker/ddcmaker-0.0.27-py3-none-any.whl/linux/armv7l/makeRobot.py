# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/13 18:14                      *
# @Author  : Bob He                                |
# @FileName: makeRobot.py                          *
# @Software: PyCharm                               |
# @Project : ddcmaker                              *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
import subprocess
from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.decorator.safety import args_check


class author(object):
    def __init__(self):
        self.name = 'Bob He'
        self.age = 20
        self.projects = "Django_linux、Django-504、selenium_linux、Amazon-crawler、AIserver、Automated-cartography" \
                        "、ddcmaker、JIT、ddcmakerVirtual"
        self.github = "https://github.com/NocoldBob/robot"
        self.email = "fastbiubiu@163.com"

    def info(self):
        print("------------****author's information****-------------\n\nname:", self.name, "\nage:", self.age,
              "\nprojects:", self.projects, "\ngithub:", self.github,
              "\nemail:", self.email, "\n\n------------****author's information****-------------")


if ge.get_eq_type() == 0:
    from ddcmaker.human import robot
    from ddcmaker.public import showlib
    from ddcmaker.human.AI_human import cv_mode as cv

    Rb = robot.robot()
    Sh = showlib.showlib()


    class Robot(object):
        @staticmethod
        def init_head():
            Rb.init_head()

        @staticmethod
        @args_check()
        def left(step=1):
            Rb.left(step)

        @staticmethod
        @args_check()
        def right(step=1):
            Rb.right(step)

        @staticmethod
        @args_check()
        def left_slide(step=1):
            Rb.left_slide(step)

        @staticmethod
        @args_check()
        def right_slide(step=1):
            Rb.right_slide(step)

        @staticmethod
        @args_check()
        def forward(step=1):
            Rb.forward(step)

        @staticmethod
        @args_check()
        def backward(step=1):
            Rb.backward(step)

        @staticmethod
        @args_check(attr_max=1)
        def up(step=1):
            Rb.up(step)

        @staticmethod
        @args_check(attr_max=1)
        def down(step=1):
            Rb.down(step)

        @staticmethod
        @args_check(attr_max=1)
        def check(step=1):
            Rb.check(step)

        @staticmethod
        @args_check()
        def nod(step=1):
            Rb.nod(step)

        @staticmethod
        @args_check()
        def shaking_head(step=1):
            Rb.shaking_head(step)

        '''虚不实真，苦切一除能，咒等等无是，咒上无是，咒明大是'''

        @staticmethod
        def hiphop():
            Sh.hiphop()

        @staticmethod
        def smallapple():
            Sh.smallapple()

        @staticmethod
        def jiangnanstyle():
            Sh.jiangnanstyle()

        @staticmethod
        def lasong():
            Sh.lasong()

        @staticmethod
        def feelgood():
            Sh.feelgood()

        @staticmethod
        def push_up():
            Rb.push_up()

        @staticmethod
        def abdominal_curl():
            Rb.abdominal_curl()

        @staticmethod
        def wave():
            Rb.wave()

        @staticmethod
        def bow():
            Rb.bow()

        @staticmethod
        def spread_wings():
            Rb.spread_wings()

        @staticmethod
        def haha():
            Rb.haha()

        @staticmethod
        def follow(color="green"):
            r = cv()
            r.follow(color)

        @staticmethod
        def find_color():
            r = cv()
            r.identifying()

        @staticmethod
        def find_hand():
            r = cv()
            r.find_hand()

        @staticmethod
        def check_distance(color="green"):
            r = cv()
            r.check_distance(color)

        @staticmethod
        def tracking(color="green"):
            r = cv()
            r.tracking(color)
"""主要更新白色机器人"""
if ge.get_eq_type() == 2:
    from ddcmaker.human_code import whiterobot
    from ddcmaker.public import showlib
    from ddcmaker.human_code.AI_robot import cv_mode as cm

    Rb = whiterobot.robot()
    Sh = showlib.showlib()


    class Robot(object):

        @staticmethod
        def init_body():
            Rb.init_body()

        @staticmethod
        def init_head():
            Rb.init_head()

        @staticmethod
        @args_check()
        def left(step=1):
            Rb.left(step)

        @staticmethod
        @args_check()
        def right(step=1):
            Rb.right(step)

        @staticmethod
        @args_check()
        def left_slide(step=1):
            Rb.left_slide(step)

        @staticmethod
        @args_check()
        def right_slide(step=1):
            Rb.right_slide(step)

        @staticmethod
        @args_check()
        def forward(step=1):
            Rb.forward(step)

        @staticmethod
        @args_check()
        def backward(step=1):
            Rb.backward(step)

        @staticmethod
        @args_check(attr_max=1)
        def up(step=1):
            Rb.up(step)

        @staticmethod
        @args_check(attr_max=1)
        def down(step=1):
            Rb.down(step)

        @staticmethod
        @args_check(attr_max=1)
        def check(step=1):
            Rb.check(step)

        @staticmethod
        @args_check()
        def nod(step=1):
            Rb.nod(step)

        @staticmethod
        @args_check()
        def shaking_head(step=1):
            Rb.shaking_head(step)

        @staticmethod
        def jiangnanstyle():
            Sh.jiangnanstyle()

        @staticmethod
        def smallapple():
            Sh.smallapple()

        @staticmethod
        def lasong():
            Sh.lasong()

        @staticmethod
        def feelgood():
            Sh.feelgood()

        @staticmethod
        def fantastic_baby():
            Sh.fantastic_baby()

        @staticmethod
        def super_champion():
            Sh.super_champion()

        @staticmethod
        def youth_cultivation():
            Sh.youth_cultivation()

        @staticmethod
        def love_starts():
            Sh.Love_starts()

        @staticmethod
        @args_check(attr_max=5)
        def push_up(step=1):
            Rb.push_up(step)

        @staticmethod
        @args_check(attr_max=5)
        def abdominal_curl(step=1):
            Rb.abdominal_curl(step)

        @staticmethod
        @args_check(attr_max=5)
        def wave(step=1):
            Rb.wave(step)

        @staticmethod
        @args_check(attr_max=5)
        def bow(step=1):
            Rb.bow(step)

        @staticmethod
        @args_check(attr_max=1)
        def spread_wings(step=1):
            Rb.spread_wings(step)

        @staticmethod
        @args_check(attr_max=5)
        def straight_boxing(step=1):
            Rb.straight_boxing(step)

        @staticmethod
        @args_check(attr_max=5)
        def lower_hook_combo(step=1):
            Rb.lower_hook_combo(step)

        @staticmethod
        @args_check(attr_max=5)
        def left_hook(step=1):
            Rb.left_hook(step)

        @staticmethod
        @args_check(attr_max=5)
        def right_hook(step=1):
            Rb.right_hook(step)

        @staticmethod
        @args_check(attr_max=1)
        def punching(step=1):
            Rb.punching(step)

        @staticmethod
        @args_check(attr_max=1)
        def crouching(step=1):
            Rb.crouching(step)

        @staticmethod
        @args_check(attr_max=1)
        def yongchun(step=1):
            Rb.yongchun(step)

        @staticmethod
        @args_check(attr_max=1)
        def beat_chest(step=1):
            Rb.beat_chest(step)

        @staticmethod
        @args_check(attr_max=1)
        def haha(step=1):
            Rb.haha(step)

        @staticmethod
        @args_check(attr_max=1)
        def left_side_kick(step=1):
            Rb.left_side_kick(step)

        @staticmethod
        @args_check(attr_max=1)
        def right_side_kick(step=1):
            Rb.right_side_kick(step)

        @staticmethod
        @args_check(attr_max=1)
        def left_foot_shot(step=1):
            Rb.left_foot_shot(step)

        @staticmethod
        @args_check(attr_max=1)
        def right_foot_shot(step=1):
            Rb.right_foot_shot(step)

        @staticmethod
        @args_check(attr_max=1)
        def show_poss(step=1):
            Rb.show_poss(step)

        @staticmethod
        @args_check(attr_max=1)
        def inverted_standing(step=1):
            Rb.inverted_standing(step)

        @staticmethod
        @args_check(attr_max=1)
        def rear_stand_up(step=1):
            Rb.rear_stand_up(step)

        #-------------------体操动作-------------------
        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_applaud_left_leg(step=1):
            Rb.gymnastics_applaud_left_leg(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_applaud_right_leg(step=1):
            Rb.gymnastics_applaud_right_leg(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_flat(step=1):
            Rb.gymnastics_hands_flat(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_flat_left_leg_forward(step=1):
            Rb.gymnastics_hands_flat_left_leg_forward(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_flat_left_leg_up(step=1):
            Rb.gymnastics_hands_flat_left_leg_up(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_flat_right_leg_forward(step=1):
            Rb.gymnastics_hands_flat_right_leg_forward(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_flat_right_leg_up(step=1):
            Rb.gymnastics_hands_flat_right_leg_up(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_to_left(step=1):
            Rb.gymnastics_hands_to_left(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hands_to_right(step=1):
            Rb.gymnastics_hands_to_right(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hand_up(step=1):
            Rb.gymnastics_hand_up(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hand_up_left_leg_backward(step=1):
            Rb.gymnastics_hand_up_left_leg_backward(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_hand_up_right_leg_backward(step=1):
            Rb.gymnastics_hand_up_right_leg_backward(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_keep_down(step=1):
            Rb.gymnastics_keep_down(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_left_hand_up(step=1):
            Rb.gymnastics_left_hand_up(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_right_hand_up(step=1):
            Rb.gymnastics_right_hand_up(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_stand_up(step=1):
            Rb.gymnastics_stand_up(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_up_left_leg(step=1):
            Rb.gymnastics_up_left_leg(step)

        @staticmethod
        @args_check(attr_max=1)
        def gymnastics_up_right_leg(step=1):
            Rb.gymnastics_up_right_leg(step)

        #-------------------体操动作-------------------
        @staticmethod
        def automatic_shot():
            rc = cm()
            rc.automatic_shot()

        @staticmethod
        def find_color():
            rc = cm()
            rc.identifying()

        @staticmethod
        def find_hand():
            rc = cm()
            rc.find_hand()

        @staticmethod
        def linefollow():
            rc = cm()
            rc.linefollow()

        @staticmethod
        def tracking(color="blue"):
            rc = cm()
            rc.tracking(color)
