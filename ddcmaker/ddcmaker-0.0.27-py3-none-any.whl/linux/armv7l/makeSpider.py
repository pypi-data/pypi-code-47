from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.decorator.safety import args_check

if ge.get_eq_type() == 3:

    from ddcmaker.spider import spider
    Sp = spider.spider()
    from ddcmaker.spider.AI_spider import cv_color as cv

    class Spider(object):

        @staticmethod
        def init_head():
            Sp.init_head()

        @staticmethod
        def init_body():
            Sp.init_body()

        @staticmethod
        @args_check()
        def left(step=1):
            Sp.left(step)

        @staticmethod
        @args_check()
        def right(step=1):
            Sp.right(step)

        @staticmethod
        @args_check()
        def left_shift(step=1):
            Sp.left_shift(step)

        @staticmethod
        @args_check()
        def right_shift(step=1):
            Sp.right_shift(step)

        @staticmethod
        @args_check()
        def forward(step=1):
            Sp.forward(step)

        @staticmethod
        @args_check()
        def backward(step=1):
            Sp.backward(step)

        @staticmethod
        @args_check()
        def nod(step=1):
            Sp.nod(step)

        @staticmethod
        @args_check()
        def shaking_head(step=1):
            Sp.shaking_head(step)

        @staticmethod
        @args_check(attr_max=1)
        def stand(step=1):
            Sp.stand(step)

        @staticmethod
        @args_check(attr_max=1)
        def creeping(step=1):
            Sp.creeping(step)

        @staticmethod
        @args_check()
        def creeping_forward(step=1):
            Sp.creeping_forward(step)

        @staticmethod
        @args_check()
        def creeping_backward(step=1):
            Sp.creeping_backward(step)

        @staticmethod
        @args_check()
        def creeping_left(step=1):
            Sp.creeping_left(step)

        @staticmethod
        @args_check()
        def creeping_right(step=1):
            Sp.creeping_right(step)

        @staticmethod
        @args_check(attr_max=1)
        def towering(step=1):
            Sp.towering(step)

        @staticmethod
        @args_check()
        def towering_forward(step=1):
            Sp.towering_forward(step)

        @staticmethod
        @args_check()
        def towering_backward(step=1):
            Sp.towering_backward(step)

        @staticmethod
        @args_check()
        def towering_left(step=1):
            Sp.towering_left(step)

        @staticmethod
        @args_check()
        def towering_right(step=1):
            Sp.towering_right(step)

        @staticmethod
        @args_check()
        def forward_flutter(step=1):
            Sp.forward_flutter(step)

        @staticmethod
        @args_check()
        def backward_flutter(step=1):
            Sp.backward_flutter(step)

        @staticmethod
        @args_check()
        def break_forward(step=1):
            Sp.break_forward(step)

        @staticmethod
        @args_check()
        def minor_steering(step=1):
            Sp.minor_steering(step)

        @staticmethod
        @args_check(attr_max=1)
        def twisting(step=1):
            Sp.twisting(step)

        @staticmethod
        @args_check(attr_max=1)
        def fighting(step=1):
            Sp.fighting(step)

        @staticmethod
        def sonar():
            c = cv()
            c.sonar()

        @staticmethod
        def tracking(color='red'):
            c = cv()
            c.tracking(color)

        @staticmethod
        def follow(color='red'):
            c = cv()
            c.follow(color)

        @staticmethod
        def find_color():
            c = cv()
            c.identifying()

        @staticmethod
        def linefollow():
            c = cv()
            c.linefollow()

        @staticmethod
        def balance():
            c = cv()
            c.balance()
