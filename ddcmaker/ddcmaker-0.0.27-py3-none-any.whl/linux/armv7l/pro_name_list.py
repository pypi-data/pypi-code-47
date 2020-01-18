# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/12 11:12                      *
# @Author  : Bob He                                |
# @FileName: pro_name_list.py                      *
# @Software: PyCharm                               |
# @Project : ddcmaker                              *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
from ddcmaker.linux.armv7l.get_equipment_type import get_eq_type
human = ["cv_find_stream.py", "cv_color_stream.py", "cv_find_hand.py", "cv_distance_stream.py", "cv_track_stream.py"]
human_code = ["cv_find_stream.py", "cv_color_stream.py", "cv_find_hand.py", "cv_line_patrol.py", "cv_track_stream.py"]
car = []
spider = ["cv_color_stream.py", "cv_track_stream.py", "cv_color_tracking.py", "cv_linefollow.py", "balance.py", "sonar.py"]
ddcmaker = {0: human, 1: car, 2: human_code, 3: spider}


def get_pro_list():
    for key in ddcmaker.keys():
        if get_eq_type() == key:
            return ddcmaker[key]
    return []


def kill_ai_pro_list():
    pro_name_list = get_pro_list()
    if pro_name_list:
        from ddcmaker.public import killprocess
        for proname in pro_name_list:
            killprocess.kill_process(proname)


