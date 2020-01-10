from in3.model.enum import In3Methods
from in3.model.client import Config, RPCRequest, Address
from in3.bind.runtime import In3Runtime


def config(in3_config: Config):
    rpc = RPCRequest(In3Methods.CONFIG, params=(in3_config,))
    return In3Runtime.call_in3_rpc(rpc)


def checksum_address(_address: Address or str, _chain: int) -> Address:
    rpc = RPCRequest(In3Methods.CHECKSUM_ADDRESS, params=(str(_address), _chain,))
    return In3Runtime.call_in3_rpc(rpc)


def abi_encode(method: str, args: list) -> int:
    rpc = RPCRequest(In3Methods.ABI_ENCODE, params=(method, args,))
    return In3Runtime.call_in3_rpc(rpc)


def node_list():
    rpc = RPCRequest(In3Methods.IN3_NODE_LIST)
    return In3Runtime.call_in3_rpc(rpc)


def node_stats():
    rpc = RPCRequest(In3Methods.IN3_STATS)
    return In3Runtime.call_in3_rpc(rpc)
