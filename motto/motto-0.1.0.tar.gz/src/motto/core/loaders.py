import importlib
from typing import List
from . import Config
from .base import SkillBase


def load_skills(config: Config) -> List[SkillBase]:
    skills = []
    for k, param in config["skills"].items():
        module = importlib.import_module(param["module"])
        if hasattr(module, "Skill"):
            skill = getattr(module, "Skill")(param)
            skills.append(skill)
    return skills
