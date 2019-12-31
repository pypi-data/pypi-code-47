from base64 import b64encode
from enum import Enum
from typing import Optional, Dict

from pydantic import BaseModel

from nidhoggr.models.session import UserProperty
from nidhoggr.utils.transformer import JSONResponseTransformer

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


class TextureResponse(BaseModel, JSONResponseTransformer):
    timestamp: int
    profileId: str
    profileName: str
    textures: Dict[TextureType, TextureItem]

    class Config:
        allow_mutation = False
        use_enum_values = True

    def pack(self) -> UserProperty:
        return UserProperty(
            name="textures",
            value=b64encode(self.json().encode('ascii')).decode('ascii')
        )


class TextureToken(BaseModel):
    name: str
    ip: str
    server_id: str
    value: str

    class Config:
        allow_mutation = False
