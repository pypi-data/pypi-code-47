# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEMMosaic(p.MessageType):

    def __init__(
        self,
        namespace: str = None,
        mosaic: str = None,
        quantity: int = None,
    ) -> None:
        self.namespace = namespace
        self.mosaic = mosaic
        self.quantity = quantity

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('namespace', p.UnicodeType, 0),
            2: ('mosaic', p.UnicodeType, 0),
            3: ('quantity', p.UVarintType, 0),
        }
