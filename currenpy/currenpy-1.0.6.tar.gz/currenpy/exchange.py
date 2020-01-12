import abc
import typing
from dataclasses import dataclass
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


@dataclass
class ExchangeResult:
    source_currency_amount: Decimal
    target_currency_amount: Decimal
    exchange_rate: Decimal


class Exchange:
    def __init__(self, exchange_rates_backend: BaseExchangeRatesBackend) -> None:
        self.exchange_rates_backend = exchange_rates_backend

    def __call__(
        self,
        source_currency: typing.Union[Currency, str],
        target_currency: typing.Union[Currency, str],
        amount: Decimal = 1.0,
    ) -> ExchangeResult:
        exchange_rate = self.exchange_rates_backend.get_exchange_rate(
            source_currency, target_currency
        )
        if not exchange_rate:
            raise InvalidExchangeRateError

        target_currency_amount = amount * exchange_rate
        exchange_result = ExchangeResult(
            source_currency_amount=amount,
            target_currency_amount=target_currency_amount,
            exchange_rate=exchange_rate,
        )
        return exchange_result
