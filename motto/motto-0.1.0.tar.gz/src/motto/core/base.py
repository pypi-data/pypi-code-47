from typing import Optional
from . import Message, SkillParams, TokenRepository
from .transforms import SkillTransform


class SkillBase(object):
    """Base class of motto-skills.
    """

    default_priority = 400

    def __init__(self, params: Optional[SkillParams] = None):
        self.params = params if params is not None else {}

    def __call__(self, document, startnode=None) -> SkillTransform:
        return SkillTransform(self.proc, self.params, document, startnode)

    def proc(self, tokens: TokenRepository, params: SkillParams) -> Optional[Message]:
        """Skill implementation for tokens.
        """
        raise NotImplementedError()
