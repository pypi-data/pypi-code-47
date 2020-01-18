# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/13 18:17                      *
# @Author  : Bob He                                |
# @FileName: makeCar.py                            *
# @Software: PyCharm                               |
# @Project : ddcmaker                              *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.decorator.safety import args_check
if ge.get_eq_type() == 1:
    from ddcmaker.car import car

    Ca = car.car()


    class Car(object):

        @staticmethod
        @args_check(attr_type=(float, int))
        def left(step=1, speed=50):
            Ca.left(step, speed)

        @staticmethod
        @args_check(attr_type=(float, int))
        def right(step=1, speed=50):
            Ca.right(step, speed)

        @staticmethod
        @args_check(attr_type=(float, int))
        def forward(step=1, speed=50):
            Ca.forward(step, speed)

        @staticmethod
        @args_check(attr_type=(float, int))
        def backward(step=1, speed=50):
            Ca.backward(step, speed)

        @staticmethod
        def stop():
            Ca.stop(0)


