"""Core custom readers for docutils
"""
from typing import List, Type
from docutils import readers
from docutils.transforms import Transform
from .base import SkillBase
from .transforms import InitializeReportTransform, TokenizeTransform


class Reader(readers.Reader):
    """Basic custom reader class.

    Includes
    - Tokenize transform
    - Skills
    """

    def __init__(self, parser=None, parser_name=None):
        super().__init__(parser=parser, parser_name=parser_name)
        self._skills: List[SkillBase] = []

    def add_skill(self, skill: SkillBase):
        self._skills.append(skill)

    def get_transforms(self) -> List[Type[Transform]]:
        """Return all transforms.
        """
        transforms = super().get_transforms()
        transforms += [TokenizeTransform, InitializeReportTransform]
        transforms += self._skills
        return transforms
