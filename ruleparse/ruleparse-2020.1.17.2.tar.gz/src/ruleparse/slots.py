#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 17:23
# @Author  : Niyoufa
import math
from ruleparse.collections import Context


class Slot(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_context_value(self, context:Context):
        """获取上下文中的变量值"""
        return context[self.name]

    def parse_slot_value(self, values:list) -> list:
        """
        解析提取的变量值
        :param value:
        :return:
        """
        raise NotImplementedError

    def __repr__(self):
        return '{}("{}", {})'.format(self.__class__.__name__, self.name, self.type)


class StringSlot(Slot):

    def __init__(self, name, type="str"):
        self.name = name
        super(StringSlot, self).__init__(name, type)

    def parse_slot_value(self, values):
        if not isinstance(values, list):
            values = [values]
        return [str(value).strip() for value in values]


class FloatSlot(Slot):

    def __init__(self, name, type="float"):
        self.name = name
        super(FloatSlot, self).__init__(name, type)

    CN_NUM = {
        '〇': 0,
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9,
        '十': 10,

        '零': 0,
        '壹': 1,
        '贰': 2,
        '叁': 3,
        '肆': 4,
        '伍': 5,
        '陆': 6,
        '柒': 7,
        '捌': 8,
        '玖': 9,

        '貮': 2,
        '两': 2,

    }
    CN_UNIT = {
        '十': 10,
        '拾': 10,
        '百': 100,
        '佰': 100,
        '千': 1000,
        '仟': 1000,
        '万': 10000,
        '萬': 10000,
        '亿': 100000000,
        '億': 100000000,
        '兆': 1000000000000,
    }

    def cn2dig(self, cn):
        lcn = list(cn)
        unit = 0  # 当前的单位
        ldig = []  # 临时数组
        while lcn:
            cndig = lcn.pop()

            if cndig in self.CN_UNIT:
                unit = self.CN_UNIT.get(cndig)
                if unit == 10000:
                    ldig.append('w')  # 标示万位
                    unit = 1
                elif unit == 100000000:
                    ldig.append('y')  # 标示亿位
                    unit = 1
                elif unit == 1000000000000:  # 标示兆位
                    ldig.append('z')
                    unit = 1

                continue
            else:
                if cndig.isdigit():
                    dig = int(cndig)
                else:
                    dig = self.CN_NUM.get(cndig)
                if unit:
                    print("{} * {}".format(dig, unit))
                    dig = dig * unit
                    unit = 0
                ldig.append(dig)

        if unit == 10:  # 处理10-19的数字
            ldig.append(10)

        ret = 0
        tmp = 0

        while ldig:
            x = ldig.pop()

            if x == 'w':
                tmp *= 10000
                ret += tmp
                tmp = 0

            elif x == 'y':
                tmp *= 100000000
                ret += tmp
                tmp = 0

            elif x == 'z':
                tmp *= 1000000000000
                ret += tmp
                tmp = 0

            else:
                tmp += x

        ret += tmp
        return ret

    def is_number(self, s):
        try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
            float(s)
            return True
        except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
            pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
        try:
            import unicodedata  # 处理ASCii码的包
            unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
            return True
        except (TypeError, ValueError):
            pass
        return False

    def cn2flo(self, cn):
        string = ""
        for cndig in cn:
            string += str(self.CN_NUM.get(cndig))
        ret = float(string) * math.pow(10, -(len(string)))
        if len(cn) + 2 != len(str(ret)):
            ret = round(float(string) * math.pow(10, -(len(string))), len(cn))
        return ret

    def parse(self, values):
        action_result = []
        for cn in values:
            if self.is_number(cn):
                if cn in self.CN_NUM.keys():
                    cn = self.CN_NUM.get(cn)
                    action_result.append(cn)
                else:
                    action_result.append(cn)
            else:
                cns = cn.split("点")
                if len(cns) == 1:
                    z = self.cn2dig(cns[0])
                else:
                    x = self.cn2dig(cns[0])
                    y = self.cn2flo(cns[1])
                    z = x + y
                action_result.append(z)
        values = [float(value) for value in action_result]
        return values

    def parse_slot_value(self, values):
        if not isinstance(values, list):
            values = [values]
        values = self.parse(values)
        return values


class IntegerSlot(FloatSlot):

    def __init__(self, name, type="int"):
        self.name = name
        super(IntegerSlot, self).__init__(name, type)

    def parse(self, values):
        if not isinstance(values, list):
            values = [values]
        values = super(IntegerSlot, self).parse(values)
        values = [int(value) for value in values]
        return values


class DatetimeSlot(Slot):
    name = "datetime"

    def __init__(self, name, type="datetime"):
        self.name = name
        super(DatetimeSlot, self).__init__(name, type)
