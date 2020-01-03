from enum import Enum

class Tags(Enum):
    NAME = "displayName"
    TYPE = "type"
    DESCRIPTION = "description"
    RARITY = "rarity"
    ID = "id"
    BACKEND_RARITY = "backendRarity"
    BACKEND_TYPE = "backendType"

class Filters(Enum):
    NAME = "displayName"
    BACKEND_TYPE = "backendType"
    ICON = "icon"
    DESCRIPTION = "description"
    BACKEND_RARITY = "backendRarity"
    GAMEPLAY_TAGS = "gameplay_tags"
    VARIANTS = "variants"
    ID = "id"
    TYPE = "type"
    RARITY = "rarity"
