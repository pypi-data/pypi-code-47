import abc
import typing
from decimal import Decimal

from currenpy.currency import Currency
from currenpy.exceptions import InvalidExchangeRateError


class BaseExchangeRatesBackend(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_exchange_rate(
        self,
        source_currency: typing.Union[Currency, str],
        target_currency: typing.Union[Currency, str],
    ) -> Decimal:
        raise NotImplementedError


class Exchange:
    def __init__(self, exchange_rates_backend: BaseExchangeRatesBackend) -> None:
        self.exchange_rates_backend = exchange_rates_backend

    def __call__(
        self,
        source_currency: typing.Union[Currency, str],
        target_currency: typing.Union[Currency, str],
        amount: Decimal = 1.0,
    ):
        exchange_rate = self.exchange_rates_backend.get_exchange_rate(
            source_currency, target_currency
        )
        if not exchange_rate:
            raise InvalidExchangeRateError

        exchange_result = amount * exchange_rate
        return exchange_result
