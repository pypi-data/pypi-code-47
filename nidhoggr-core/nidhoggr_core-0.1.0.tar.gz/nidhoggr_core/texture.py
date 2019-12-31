from enum import Enum
from typing import Optional, Dict

from pydantic.main import BaseModel

TextureMeta = Optional[Dict[str, str]]


class TextureType(Enum):
    SKIN = "SKIN"
    CAPE = "CAPE"
    ELYTRA = "ELYTRA"


class TextureItem(BaseModel):
    url: str
    metadata: TextureMeta = None

    class Config:
        allow_mutation = False
