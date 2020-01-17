#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/20 11:27
# @Author  : Niyoufa
import re
from typing import Callable
from ruleparse.collections import Context
from ruleparse.slots import StringSlot, IntegerSlot, FloatSlot, DatetimeSlot
from ruleparse.rules import Rule, CompositeConditionRule
from ruleparse.cache import EXRECache

import logging
logger = logging.getLogger(__name__)


class ExReRule(Rule):
    """EXRE文本规则"""
    ref_regex = r"<(?!!)" \
                r"(?P<rule_name>[_a-zA-Z0-9\u4e00-\u9fa5]+)" \
                r"(?:{(?P<slot_name>[_a-zA-Z0-9\u4e00-\u9fa5]+)(?P<operator>(?:=|\+=))(?P<value>[^<{>]+)})?" \
                r">"

    def __init__(self, content: str = None, name: str = None,
                 textParse: Callable = None,
                 conditionRule: CompositeConditionRule = None,
                 cache: EXRECache = None, parser = None):
        """

        :param content: 规则表达式
        :param name: 规则名称，默认为None，不为None的规则需要加入exre缓存, 作为公共规则库
        :param textParse: 获取解析文本
        :param conditionRule: 规则条件
        :param cache: exre缓存器
        :param parser: 规则解析器
        """
        if not conditionRule and not content:
            raise Exception("规则条件和表达式不能同时为空")

        self.content = content
        self.name = name
        self.conditionRule = conditionRule

        self.cache = cache
        if self.cache:
            self.cache.set_rule(self)

        self.parser = parser
        self.textParse = textParse
        self.slots = {}
        self.compile_regex = None
        self.fieldId = str(id(str))

    def analyzeContent(self, matched):
        if self.cache is None:
            raise Exception("cache 不能为空")
        groupdict = matched.groupdict()
        rule_name = groupdict["rule_name"]
        rule_dict = self.cache.get_rule(rule_name)
        if not rule_dict:
            raise Exception("规则不存在：{}".format(rule_name))
        content = r"(?:{})".format(rule_dict["content"])
        content = self.compileContent(content)

        slot_name = groupdict.get("slot_name")
        if slot_name:
            operator = groupdict["operator"]
            value = groupdict["value"]

            slot_repr = self.cache.get_slot(slot_name)
            if not slot_repr:
                raise Exception("变量不存在: {}".format(slot_name))
            else:
                slot_obj = eval(slot_repr)

            if value == "$":
                content = r"(?P<{}>{})".format(slot_name, content)
                default_value = []
            else:
                default_value = slot_obj.parse_slot_value(value)

            self.slots[slot_name] = {
                "operator": operator,
                "slot_obj": slot_obj,
                "value": value,
                "default_value": default_value
            }

        return content

    def compileContent(self, content):
        """
        编译规则表达式为正则表达式
        :param content:
        :return:
        """
        expression = re.sub(self.ref_regex, self.analyzeContent, content)
        return expression

    def preprocess(self, context: Context, content):
        """
        规则表达式预处理，处理系统规则
        :param context:
        :param content:
        :return:
        """
        content = re.sub(r"<exclude\((.+)\)>", r"((?!\1)[\s\S])*?", content)
        if self.parser:
            content = self.parser.preprocess(context, content)
        return content

    def condition(self, context: Context, **kwargs):
        flag = False

        # 执行条件判断
        if self.conditionRule and not self.conditionRule.condition(context):
            return False

        if not self.content:
            return True
        else:
            # 编译规则表达式
            if self.compile_regex is None:
                content = self.preprocess(context, self.content)
                logger.debug("content: {}".format(content))
                self.compile_regex = re.compile(self.compileContent(content), flags=re.M)

            # 获取规则解析文本
            if not self.textParse:
                text = kwargs.pop("text")
            else:
                text = self.textParse(context)

        slots = []
        for matched in self.compile_regex.finditer(text):
            flag = True
            groupdict = matched.groupdict()
            slot_dict = {}
            slot_dict["span"] = matched.span()
            for slot_name, slot in self.slots.items():
                value = groupdict.get(slot_name)
                if slot["value"] == "$" and value:
                    values = self.slots[slot_name]["slot_obj"].parse_slot_value(value)
                    slot_dict[slot_name] = values
                else:
                    slot_dict[slot_name] = slot["default_value"]
            slots.append(slot_dict)

        if slots:
            self.action(context, slots=slots)
        return flag

    def action(self, context:Context, **kwargs):
        if not "fields" in context:
            context.fields = {}
        if self.parser:
            context.fields[self.parser.name] = kwargs["slots"]
        else:
            context[self.fieldId] = kwargs["slots"]