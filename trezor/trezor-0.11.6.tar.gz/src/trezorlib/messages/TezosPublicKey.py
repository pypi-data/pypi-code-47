# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TezosPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 155

    def __init__(
        self,
        public_key: str = None,
    ) -> None:
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('public_key', p.UnicodeType, 0),
        }
