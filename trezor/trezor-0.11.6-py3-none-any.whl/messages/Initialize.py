# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class Initialize(p.MessageType):
    MESSAGE_WIRE_TYPE = 0

    def __init__(
        self,
        state: bytes = None,
        skip_passphrase: bool = None,
    ) -> None:
        self.state = state
        self.skip_passphrase = skip_passphrase

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('state', p.BytesType, 0),
            2: ('skip_passphrase', p.BoolType, 0),
        }
