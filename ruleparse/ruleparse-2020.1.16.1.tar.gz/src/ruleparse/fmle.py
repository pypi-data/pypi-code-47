#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 15:45
# @Author  : Niyoufa
from typing import List
from ruleparse.collections import Context
from ruleparse.rules import Rule
from ruleparse.parsers import FieldParser
from ruleparse.exre import ExReRule


class FmLeRule(Rule):
    """先匹配后提取"""

    def __init__(self, fmRule: ExReRule, leRules: List[ExReRule], parser:FieldParser):
        self.fmRule = fmRule
        self.leRules = leRules
        self.parser = parser

    def condition(self, context:Context, **kwargs):
        flag = self.fmRule.condition(context, **kwargs)
        if flag:
            self.action(context)
        return flag

    def action(self, context:Context, **kwargs):
        text = self.fmRule.textParse(context)
        texts = [text[slot["span"][0]:slot["span"][1]] for slot in context.pop(self.fmRule.fieldId)]
        slots = []
        for text in texts:
            slot_dict = {}
            for rule in self.leRules:
                if rule.condition(context, text=text):
                    context_slots = context.pop(rule.fieldId)
                    for slot_name, slot in rule.slots.items():
                        values = []
                        for context_slot_dict in context_slots:
                            if context_slot_dict.get(slot_name):
                                values.extend(context_slot_dict[slot_name])
                        if slot["value"] == "$" and values:
                            value = rule.slots[slot_name]["slot_obj"].parse_slot_value(list(set(values)))
                            slot_dict[slot_name] = value
                        else:
                            slot_dict[slot_name] = slot["default_value"]
            slots.append(slot_dict)

        if slots:
            if not "fields" in context:
                context.fields = {}
            context.fields[self.parser.name] = slots
