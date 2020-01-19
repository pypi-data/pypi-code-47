from enum import Enum


class Service(Enum):
    """Enum for Services

    Service.LIST: 巻号一覧取得
    Service.SEARCH: 論文検索結果取得
    """
    LIST = 2
    SEARCH = 3
