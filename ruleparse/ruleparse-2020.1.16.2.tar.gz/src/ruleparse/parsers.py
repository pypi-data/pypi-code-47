# @Time    : 2018/12/17 20:46
# @Author  : Niyoufa
from ruleparse.collections import Context
from ruleparse.rules import Rule


class FieldParser:
    """字段解析器"""
    name = None

    def __init__(self):
        self.rules = []

    def addRule(self, rule:Rule):
        """
        添加规则
        """
        if not hasattr(self, "rules"):
            self.rules = []
        rule.parser = self
        if hasattr(self, "cache"):
            rule.cache = self.cache
            rule.textParse = lambda context:context.text
        self.rules.append(rule)

    def preprocess(self, context: Context, expression: str) -> str:
        """
        预处理
        :param context:
        :param content:
        :return:
        """
        return expression

    def parse(self, context: Context, **kwargs) -> bool:
        """
        解析字段
        :param context:
        :param args:
        :param kwargs:
        :return:
        """
        flag = False
        for rule in self.rules:
            if rule.condition(context, **kwargs):
                flag = True
                break
        return flag