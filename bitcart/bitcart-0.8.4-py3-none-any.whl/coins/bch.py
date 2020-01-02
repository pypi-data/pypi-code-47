from typing import Union

from .btc import BTC

ASYNC = False


class BCH(BTC):
    coin_name = "BCH"
    friendly_name = "Bitcoin Cash"
    RPC_URL = "http://localhost:5004"

    def history(self: "BCH") -> dict:
        return self.server.history()  # type: ignore

    def addrequest(
        self: "BCH",
        amount: Union[int, float],
        description: str = "",
        expire: Union[int, float] = 15,
    ) -> dict:
        expiration = 60 * expire if expire else None
        return self.server.addrequest(  # type: ignore
            amount=amount, memo=description, expiration=expiration, force=True
        )
