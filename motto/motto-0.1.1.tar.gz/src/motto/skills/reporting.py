"""This skill-module add report already
"""
from motto.core import Message
from motto.core.base import SkillBase


class Skill(SkillBase):
    def proc(self, tokens, params):
        return Message("This skill is regnsted.")
