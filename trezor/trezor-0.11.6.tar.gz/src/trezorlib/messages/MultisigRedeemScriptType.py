# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .HDNodePathType import HDNodePathType
from .HDNodeType import HDNodeType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MultisigRedeemScriptType(p.MessageType):

    def __init__(
        self,
        pubkeys: List[HDNodePathType] = None,
        signatures: List[bytes] = None,
        m: int = None,
        nodes: List[HDNodeType] = None,
        address_n: List[int] = None,
    ) -> None:
        self.pubkeys = pubkeys if pubkeys is not None else []
        self.signatures = signatures if signatures is not None else []
        self.m = m
        self.nodes = nodes if nodes is not None else []
        self.address_n = address_n if address_n is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('pubkeys', HDNodePathType, p.FLAG_REPEATED),
            2: ('signatures', p.BytesType, p.FLAG_REPEATED),
            3: ('m', p.UVarintType, 0),
            4: ('nodes', HDNodeType, p.FLAG_REPEATED),
            5: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        }
