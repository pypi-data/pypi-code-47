from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.human_code.human_ssr import serial_human
from ddcmaker.public.basic_mode import ba_mode

if ge.get_eq_type() == 2:
    import time
    from ddcmaker.public import PWMServo
    class robot(ba_mode):
        def __init__(self):
            super().__init__()
            self.name = "机器人"
            self.SSR = serial_human()
            self.sleeptime = 1
            self.nodid = 1
            self.shakingid = 2
            self.Interval_time = 200
            self.homing_angle = 1500
            self.start_angle = 1800
            self.end_angle = 1200

        def init_body(self):
            self.run_action("0")

        def up(self, step):
            self.run_action("0", step, "站立")

        def down(self, step):
            self.run_action("14", step, "蹲下")

        def check(self, step):
            self.run_action("188", step, "自检")

        def forward(self, step):
            self.run_action("1", step, "前进")

        def backward(self, step):
            self.run_action("2", step, "后退")

        def left(self, step):
            self.run_action("3", step, "左转")

        def right(self, step):
            self.run_action("4", step, "右转")

        def left_slide(self, step):
            self.run_action("11", step, "左滑")

        def right_slide(self, step):
            self.run_action("12", step, "右滑")

        def push_up(self, step=1):
            self.run_action("7", step, "俯卧撑")

        def abdominal_curl(self, step=1):
            self.run_action("8", step, "仰卧起坐")

        def wave(self, step):
            self.run_action("9", step, "挥手┏(＾0＾)┛")

        def bow(self, step):
            self.run_action("10", step, "鞠躬╰(￣▽￣)╭")

        def spread_wings(self, step):
            self.run_action("13", step, "大鹏展翅")

        def haha(self, step):
            self.run_action("15", step, "哈哈大笑o(*￣▽￣*)o")

        def straight_boxing(self, step):
            self.run_action("30", step, "直拳连击")

        def lower_hook_combo(self, step):
            self.run_action("31", step, "下勾拳连击")

        def left_hook(self, step):
            self.run_action("32", step, "左勾拳")

        def right_hook(self, step):
            self.run_action("33", step, "右勾拳")

        def punching(self, step):
            self.run_action("34", step, "攻步冲拳")

        def crouching(self, step):
            self.run_action("35", step, "八字蹲拳")

        def yongchun(self, step):
            self.run_action("36", step, "咏春拳")

        def beat_chest(self, step):
            self.run_action("37", step, "捶胸")

        def left_side_kick(self, step):
            self.run_action("50", step, "左侧踢")

        def right_side_kick(self, step):
            self.run_action("51", step, "右侧踢")

        def left_foot_shot(self, step):
            self.run_action("52", step, "左脚射门")

        def right_foot_shot(self, step):
            self.run_action("53", step, "右脚射门")

        def show_poss(self, step):
            self.run_action("60", step, "摆拍poss")

        def inverted_standing(self, step):
            self.run_action("101", step, "前倒站立")

        def rear_stand_up(self, step):
            self.run_action("102", step, "后倒站立")

        # -------------------体操动作-------------------
        def gymnastics_applaud_left_leg(self, step):
            self.run_action("gymnastics_applaud_left_leg", step, "鼓掌时迈左腿")

        def gymnastics_applaud_right_leg(self, step):
            self.run_action("gymnastics_applaud_right_leg", step, "鼓掌时迈右腿")

        def gymnastics_hands_flat(self, step):
            self.run_action("gymnastics_hands_flat", step, "双手平举")

        def gymnastics_hands_flat_left_leg_forward(self, step):
            self.run_action("gymnastics_hands_flat_left_leg_forward", step, "双手平举时左腿向前")

        def gymnastics_hands_flat_left_leg_up(self, step):
            self.run_action("gymnastics_hands_flat_left_leg_up", step, "双手平举时向左踢腿")

        def gymnastics_hands_flat_right_leg_forward(self, step):
            self.run_action("gymnastics_hands_flat_right_leg_forward", step, "双手平举时右腿向前")

        def gymnastics_hands_flat_right_leg_up(self, step):
            self.run_action("gymnastics_hands_flat_right_leg_up", step, "双手平举时向右踢腿")

        def gymnastics_hands_to_left(self, step):
            self.run_action("gymnastics_hands_to_left", step, "双手向左平举")

        def gymnastics_hands_to_right(self, step):
            self.run_action("gymnastics_hands_to_right", step, "双手向右平举")

        def gymnastics_hand_up(self, step):
            self.run_action("gymnastics_hand_up", step, "双手高举")

        def gymnastics_hand_up_left_leg_backward(self, step):
            self.run_action("gymnastics_hand_up_left_leg_backward", step, "双手平举时左腿向后")

        def gymnastics_hand_up_right_leg_backward(self, step):
            self.run_action("gymnastics_hand_up_right_leg_backward", step, "双手平举时右腿向后")

        def gymnastics_keep_down(self, step):
            self.run_action("gymnastics_keep_down", step, "蹲下")

        def gymnastics_left_hand_up(self, step):
            self.run_action("gymnastics_left_hand_up", step, "举左手")

        def gymnastics_right_hand_up(self, step):
            self.run_action("gymnastics_right_hand_up", step, "举右手")

        def gymnastics_stand_up(self, step):
            self.run_action("gymnastics_stand_up", step, "立正")

        def gymnastics_up_left_leg(self, step):
            self.run_action("gymnastics_up_left_leg", step, "迈左腿")

        def gymnastics_up_right_leg(self, step):
            self.run_action("gymnastics_up_right_leg", step, "迈右腿")

        def gymnastics_akimbo(self, step):
            self.run_action("gymnastics_akimbo", step, "叉腰")

        def gymnastics_nod_down(self, step):
            self.Interval_time = 2000
            for i in range(step):
                PWMServo.setServo(self.nodid, self.start_angle, self.Interval_time)
                time.sleep(self.Interval_time / 1000)
                self.describe("体操点头")

        def gymnastics_nod_up(self, step):
            self.Interval_time = 2000
            for i in range(step):
                PWMServo.setServo(self.nodid, self.end_angle, self.Interval_time)
                time.sleep(self.Interval_time / 1000)
                self.describe("体操抬头")

        def gymnastics_shaking_head_left(self, step):
            self.Interval_time = 2000
            for i in range(step):
                PWMServo.setServo(self.shakingid, self.start_angle, self.Interval_time)
                time.sleep(self.Interval_time / 1000)
                self.describe("左摇头")

        def gymnastics_shaking_head_right(self, step):
            self.Interval_time = 2000
            for i in range(step):
                PWMServo.setServo(self.shakingid, self.end_angle, self.Interval_time)
                time.sleep(self.Interval_time / 1000)
                self.describe("右摇头")

        def gymnastics_init_head(self):
            self.init_head()
            self.describe("头部归位")
        # -------------------体操动作-------------------

'''
我喜欢吃蒸鲈鱼，虾鲍鳝，蝴蝶翅
'''
