# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
# -*- coding: utf-8 -*-                            |
# @Time    : 2019/12/12 14:35                      *
# @Author  : Bob He                                |
# @FileName: makeros.py                            *
# @Software: PyCharm                               |
# @Project : ddcmaker                              *
# @Csdn    ：https://blog.csdn.net/bobwww123       |
# @Github  ：https://www.github.com/NocoldBob      *
# --*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*-+
from ddcmaker.server.__init__ import *  # line:1


def linux_maker(OOO000OOOO00OOO0O, settime=settime):  # line:4
    O0OO0O00000O000O0 = {"msg": "", "code": 1, "data": {}}  # line:5
    OOO000OOOO00OOO0O = str(OOO000OOOO00OOO0O, encoding="u8").replace('    ', '')  # line:11
    if not OOO000OOOO00OOO0O:  # line:13
        O0OO0O00000O000O0.update(err="代码不能为空，请输入代码。")  # line:14
        return json.dumps(O0OO0O00000O000O0)  # line:15
    try:  # line:16
        O0O0OOOOOO00000OO = eval(OOO000OOOO00OOO0O)["code"]  # line:17
        O0O0OOOOOO00000OO = base64.b64decode(O0O0OOOOOO00000OO)  # line:18
        O0O0OOOOOO00000OO = str(O0O0OOOOOO00000OO, encoding="u8")  # line:19
    except Exception as OOOO0OO0O00OO0OOO:  # line:21
        O0OO0O00000O000O0.update(err=OOOO0OO0O00OO0OOO)  # line:23
        return json.dumps(O0OO0O00000O000O0)  # line:25
    if O0O0OOOOOO00000OO == "":  # line:26
        O0OO0O00000O000O0.update(err="代码不能为空，请输入代码。")  # line:27
        return json.dumps(O0OO0O00000O000O0)  # line:29
    O00O0O000OO0OO0O0 = str(time.time())[-6:] + ".py"  # line:31
    O000OOOO0O00O0O00 = "resave//" + O00O0O000OO0OO0O0  # line:32
    from ddcmaker.code_check.code_safety import check_mode  # line:33
    OO0O0O00O0000OO0O = check_mode(O0O0OOOOOO00000OO[:50])  # line:34
    with open(O000OOOO0O00O0O00, "w+", encoding="u8")as O00O0O0OO0OO0O000:  # line:35
        O00O0O0OO0OO0O000.write(O0O0OOOOOO00000OO)  # line:37
        O00O0O0OO0OO0O000.close()  # line:38
    O0O00O00O0O0O0OOO = "python3  " + O000OOOO0O00O0O00  # line:40
    if not OO0O0O00O0000OO0O:  # line:41
        from ddcmaker.code_check.code_safety import check_package  # line:42
        O0OO0O00000O000O0 = check_package(O0OO0O00000O000O0, O000OOOO0O00O0O00)  # line:43
        if O0OO0O00000O000O0["code"] == 555:  # line:44
            return json.dumps(O0OO0O00000O000O0)  # line:45
        try:  # line:46
            OOO0OO000OO0OO000 = subprocess.Popen(O0O00O00O0O0O0OOO, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                 shell=True)  # line:47
        except Exception as OOOO0OO0O00OO0OOO:  # line:48
            O0OO0O00000O000O0.update(err=OOOO0OO0O00OO0OOO)  # line:49
            return json.dumps(O0OO0O00000O000O0)  # line:50
        try:  # line:51
            OO000000OO0O0O0OO, OOOO00O0O0OOOO0OO = OOO0OO000OO0OO000.communicate(timeout=settime)  # line:52
        except Exception as OOOO0OO0O00OO0OOO:  # line:53
            print("捕捉错误", OOOO0OO0O00OO0OOO)  # line:54
            OOO0OO000OO0OO000.kill()  # line:55
            from ddcmaker.linux.armv7l.get_equipment_type import get_maker_name  # line:56
            from ddcmaker.linux.armv7l.pro_name_list import kill_ai_pro_list  # line:57
            O000OOO0OOOOOO000 = get_maker_name()  # line:58
            kill_ai_pro_list()  # line:59
            O0OO0O00000O000O0.update(code=233, msg="超时主动中断",
                                     err="运行超时，中断" + O000OOO0OOOOOO000 + "操作，" + O000OOO0OOOOOO000 + "一次最长允许运行动作" + str(
                                         settime) + "秒")  # line:63
        else:  # line:64
            if OOOO00O0O0OOOO0OO:  # line:65
                O0OO0O00000O000O0.update(err=OOOO00O0O0OOOO0OO.decode("u8"))  # line:66
            else:  # line:67
                O0OO0O00000O000O0.update(code=0, msg="执行成功", data={"moduleData": [OO000000OO0O0O0OO.decode("u8")],
                                                                   "printData": OO000000OO0O0O0OO.decode(
                                                                       "u8"), })  # line:71
        finally:  # line:72
            os.remove(O000OOOO0O00O0O00)  # line:73
        print(O0OO0O00000O000O0)  # line:74
        return json.dumps(O0OO0O00000O000O0)  # line:75
    else:  # line:76
        print("当前设备脱机运行，不再受到平台约束！")  # line:77
        O0OO0O00000O000O0.update(code=777, msg="高级模式脱机运行",
                                 err="警告：当前模式为高级模式，设备将执行脱机命令，设备将不会超时中断动作！\n请谨慎使用，仅限工程师调试使用！！\n若要停止，请等待设备运行结束或者关闭设备电源")  # line:79

        def O0O0OOO00OO0OOOO0():  # line:81
            try:  # line:82
                OO0OOO00O0000000O = subprocess.Popen(O0O00O00O0O0O0OOO, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                     shell=True)  # line:83
                OO0OOO00O0000000O.communicate(timeout=1000)  # line:84
            except Exception as OOO0O000OOO0O000O:  # line:85
                print(OOO0O000OOO0O000O)  # line:86
            finally:  # line:87
                os.remove(O000OOOO0O00O0O00)  # line:88

        import threading  # line:89
        O00000000O0O00OO0 = threading.Thread(target=O0O0OOO00OO0OOOO0)  # line:90
        O00000000O0O00OO0.setDaemon(True)  # line:91
        O00000000O0O00OO0.start()  # line:92
        return json.dumps(O0OO0O00000O000O0)  # line:93


def windows_maker(OO00O000OOOO000OO):  # line:96
    OOOOOOOO000OOOOO0 = {"msg": "", "code": 1, "data": {}}  # line:97
    OO00O000OOOO000OO = str(OO00O000OOOO000OO, encoding="u8").replace('    ', '')  # line:102
    print(OO00O000OOOO000OO)  # line:103
    try:  # line:104
        O0000OO0OO0OOO0O0 = eval(OO00O000OOOO000OO)["code"]  # line:105
        O0000OO0OO0OOO0O0 = base64.b64decode(O0000OO0OO0OOO0O0)  # line:106
        O0000OO0OO0OOO0O0 = str(O0000OO0OO0OOO0O0, encoding="u8")  # line:107
        print("取出传入的值", O0000OO0OO0OOO0O0)  # line:108
    except Exception as O0O00OOO0OOO0O000:  # line:109
        print(O0O00OOO0OOO0O000)  # line:110
        OOOOOOOO000OOOOO0.update(err=O0O00OOO0OOO0O000)  # line:111
        return json.dumps(OOOOOOOO000OOOOO0)  # line:113
    if O0000OO0OO0OOO0O0 == "":  # line:114
        OOOOOOOO000OOOOO0.update(err="代码不能为空，请输入代码。")  # line:115
        return json.dumps(OOOOOOOO000OOOOO0)  # line:117
    if O0000OO0OO0OOO0O0 != "" and "stop" in O0000OO0OO0OOO0O0[:15]:  # line:118
        print("终止机器人运动")  # line:120
        OOOOOOOO000OOOOO0.update(code=666, msg="动作已经终止", err="前端请求主动中断动作，杀死运行进程。")  # line:121
        return json.dumps(OOOOOOOO000OOOOO0)  # line:122
    O00O0OOO0OO0O00OO = str(time.time())[-6:] + ".py"  # line:124
    print(O00O0OOO0OO0O00OO)  # line:125
    with open(O00O0OOO0OO0O00OO, "w+", encoding="u8")as O0000OOO00O000O00:  # line:126
        O0000OOO00O000O00.write(O0000OO0OO0OOO0O0)  # line:128
        O0000OOO00O000O00.close()  # line:129
    O0OO0OO0O000OOO00 = "python " + O00O0OOO0OO0O00OO  # line:131
    print(O0OO0OO0O000OOO00)  # line:132
    try:  # line:133
        O00OOOO00O0OO0O0O = subprocess.Popen(O0OO0OO0O000OOO00, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                             encoding="u8", shell=False)  # line:134
    except Exception as O0O00OOO0OOO0O000:  # line:135
        print(O0O00OOO0OOO0O000)  # line:136
        OOOOOOOO000OOOOO0.update(err=O0O00OOO0OOO0O000)  # line:137
        return json.dumps(OOOOOOOO000OOOOO0)  # line:139
    try:  # line:140
        O000O00000OOO00O0, O00OO00OO00O0O0O0 = O00OOOO00O0OO0O0O.communicate(timeout=60)  # line:141
    except subprocess.TimeoutExpired:  # line:142
        O00OOOO00O0OO0O0O.kill()  # line:143
        OOOOOOOO000OOOOO0.update(code=233, msg="机器运行超时，中断机器人链接。")  # line:144
    else:  # line:145
        if O00OO00OO00O0O0O0:  # line:146
            OOOOOOOO000OOOOO0.update(err=O00OO00OO00O0O0O0)  # line:147
        else:  # line:148
            OOOOOOOO000OOOOO0.update(code=0, data={"moduleData": [O000O00000OOO00O0],
                                                   "printData": O000O00000OOO00O0, })  # line:152
    finally:  # line:153
        os.remove(O00O0OOO0OO0O00OO)  # line:154
    return json.dumps(OOOOOOOO000OOOOO0)  # line:155


def Mac_maker():  # line:158
    O00OOO0O0OOO0000O = {"msg": "", "code": 1, "data": {}}  # line:159
    O00OOO0O0OOO0000O.update(err="当前系统为Mac,暂时不支持此系统！")  # line:160
    return json.dumps(O00OOO0O0OOO0000O)  # line:161


def other_maker():  # line:164
    O000O0OO0O0O0O00O = {"msg": "", "code": 1, "data": {}}  # line:165
    O000O0OO0O0O0O00O.update(err="你这是啥系统呀，暂时不支持哟！")  # line:166
    return json.dumps(O000O0OO0O0O0O00O)  # line:167
