#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 15:43
# @Author  : Niyoufa
import re
import copy
import string
from ruleparse.collections import Context
from ruleparse.slots import Slot

import logging
logger = logging.getLogger(__name__)


class Rule:
    """规则父类"""

    def condition(self, context:Context, **kwargs) -> bool:
        """
        条件判断
        :param block:
        :param handler:
        :param kwargs:
        :return:
        """
        raise NotImplementedError

    def action(self, context:Context, **kwargs):
        """
        动作
        :param block:
        :param handler:
        :param kwargs:
        :return:
        """
        pass

class RuleSet:
    """规则集"""

    def __init__(self, rules):
        if not isinstance(rules, list):
            raise ValueError("The rules item must be a rule or ruleset object")
        else:
            for rule in rules:
                if not isinstance(rule, Rule) and not isinstance(rule, RuleSet):
                    raise ValueError("The rules item must be a rule or ruleset object")

        self.rules = rules

    def __iter__(self):
        for rule in self.rules:
            yield rule

    def __repr__(self):
        return "%s"%self.rules


class OR(Rule):
    """
    OR规则组合
    """

    def __init__(self, rules):
        self.ruleset = RuleSet(rules)

    def condition(self, context:Context, **kwargs):
        return any([rule.condition(context, **kwargs) for rule in self.ruleset])

    def action(self, context:Context, **kwargs):
        return [rule.action(context, **kwargs) for rule in self.ruleset if rule.condition(context, **kwargs)]

    def __repr__(self):
        return "({})".format(" or ".join([repr(rule) for rule in self.ruleset.rules]))


class AND(Rule):
    """
    AND规则组合
    """

    def __init__(self, rules):
        self.ruleset = RuleSet(rules)

    def condition(self, context:Context, **kwargs):
        return all([rule.condition(context, **kwargs) for rule in self.ruleset])

    def __repr__(self):
        return "({})".format(" and ".join([repr(rule) for rule in self.ruleset.rules]))


class NOT(Rule):
    """
    NOT规则组合
    """

    def __init__(self, rule):
        self.ruleset = RuleSet(rule)

    def condition(self, context:Context, **kwargs):
        return not(any([rule.condition(context, **kwargs) for rule in self.ruleset]))

    def __repr__(self):
        return "NOT{}".format(self.ruleset)


class ConditionRule(Rule):
    """条件规则"""

    def __init__(self, slot:Slot, value, operator="=="):
        self.slot = slot
        self.value = value
        self.operator = operator

    def condition(self, context:Context, **kwargs):
        context_value = self.slot.get_context_value(context)
        if context_value == None:
            return False

        if self.operator == "==" or self.operator == "=":
            return context_value == self.value \
                   or (isinstance(context_value, list) and self.value in context_value) \
                   or (isinstance(self.value, list) and context_value in self.value) \
                   or (isinstance(context_value, list) and isinstance(self.value, list) and bool(set(context_value)&set(self.value)) )
        elif self.operator == "!=":
            return context_value != self.value
        elif self.operator == ">":
            return float(context_value) > float(self.value)
        elif self.operator == ">=":
            return float(context_value) >= float(self.value)
        elif self.operator == "<":
            return float(context_value) < float(self.value)
        elif self.operator == "<=":
            return float(context_value) <= float(self.value)
        elif self.operator == "in":
            return context_value in self.value
        else:
            raise Exception("条件运算符不支持:%s"%self.operator)

    def __repr__(self):
        return "<rule {}{}{}>".format(self.slot.name, self.operator, self.value)


class RegexRule(Rule):
    """正则规则"""

    def __init__(self, regex):
        self.regex = regex
        self.regex_compile = re.compile(regex, flags=re.M)

    def condition(self, context:Context, **kwargs):
        if context["text"] and self.regex_compile.search(context["text"]):
            return True
        else:
            return False

    def __repr__(self):
        return "<regex rule r'{}'>".format(self.regex)

    def action(self, context:Context, **kwargs):
        matched = self.regex_compile.search(context["text"])
        if matched:
            return matched.group()

class AndRegexRule(Rule):

    def __init__(self, ruleset:RuleSet):
        self.ruleset = ruleset

    def condition(self, context:Context, **kwargs):
        for rule in self.ruleset:
            if not rule.condition(context):
                return False
        return True

    def __repr__(self):
        return "({})".format(" and ".join([repr(rule) for rule in self.ruleset.rules]))

class AndConditionRule(Rule):
    """事务条件规则"""

    def __init__(self, ruleset:RuleSet):
        self.ruleset = ruleset

    def condition(self, context:Context, **kwargs):
        temp = {}
        for condition in self.ruleset:
            if not isinstance(condition, ConditionRule):
                raise Exception("条件类型错误：{}".format(type(condition)))
            temp.setdefault(condition.slot.name, []).\
                append(ConditionRule(condition.slot, condition.value, condition.operator))
        rule = AND([AND(rules) for rules in temp.values() if rules])
        if rule.condition(context, **kwargs):
            return True
        else:
            return False


class CompositeConditionRule(Rule):
    """字段条件规则"""

    def __init__(self, ruleset:RuleSet):
        self.ruleset = ruleset

    def condition(self, context: Context, **kwargs):
        rules = []
        for obj in self.ruleset:
            if isinstance(obj, Rule):
                rules.append(OR([obj]))
            elif isinstance(obj, RuleSet):
                rules.append(OR(obj.rules))
            else:
                raise ValueError("The ruleset item must be a rule or ruleset object")

        rule = AND([rule for rule in rules])
        logger.debug(rule)
        if rule.condition(context, **kwargs):
            return True
        else:
            return False