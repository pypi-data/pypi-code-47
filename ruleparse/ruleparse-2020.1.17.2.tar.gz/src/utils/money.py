#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 12:52
# @Author  : Niyoufa
import re
from ruleadmin.utils.number import FloatParse


class MoneyParse:
    regex1 = r"^(?P<数量>[\d\.〇一二三四五六七八九零壹贰叁肆伍陆柒捌玖貮两十拾百佰千仟万萬亿億兆点]+)(?<!万)$"
    regex2 = r"^(?P<数量>[\d\.〇一二三四五六七八九零壹贰叁肆伍陆柒捌玖貮两十拾百佰千仟萬亿億兆点]+)(?P<单位>万)$"
    regex1_compile = re.compile(regex1)
    regex2_compile = re.compile(regex2)
    float_parser = FloatParse()

    def preprocess(self, value):
        value = re.sub(r"[,，多余]", "", value)
        return value

    def parse(self, value):
        value = self.preprocess(value)
        matched = self.regex1_compile.search(value) or \
                  self.regex2_compile.search(value)

        groupdict = matched.groupdict()
        amount = groupdict["数量"]
        unit = groupdict.get("单位")
        amount = self.float_parser.parse([amount])[0]
        if unit == "万":
            amount = amount * 10000
        return [int(amount)]

if __name__ == "__main__":
    parser = MoneyParse()
    print(parser.parse("83735元"))