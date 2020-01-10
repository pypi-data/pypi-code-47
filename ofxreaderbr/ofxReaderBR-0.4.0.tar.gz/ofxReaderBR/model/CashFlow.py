from datetime import datetime
from enum import Enum

from .Origin import Origin


class CashFlowType(Enum):
    DEBIT = 1
    CREDIT = 2


class CashFlow(object):

    def __init__(self,
                 name: str = 'N/A',
                 flow_type: CashFlowType = CashFlowType.DEBIT,
                 value: float = 0.0,
                 date: str = 'N/A',
                 cash_date: str = 'N/A',
                 origin: Origin = None):
        self.name = name
        self.flowType = flow_type
        self.value = value
        self.date = date
        self.cash_date = cash_date
        self.origin = origin

    @staticmethod
    def __is_valid_date(date):
        return date == 'N/A' or isinstance(date, datetime)

    @staticmethod
    def __is_valid_value(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __is_valid_cash_date(self):
        return self.cash_date >= self.date

    def is_valid(self):
        return (self.__is_valid_value(self.value) and
                self.__is_valid_date(self.date) and
                self.__is_valid_date(self.cash_date) and
                self.__is_valid_cash_date() and
                isinstance(self.flowType, CashFlowType) and
                (isinstance(self.origin, Origin) or self.origin is None) and
                type(self.name) == str)

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.name.strip() == other.name.strip() and
                self.value == other.value and self.date == other.date and
                self.cash_date == other.cash_date and
                self.origin == other.origin)

    def __repr__(self):
        return 'CashFlow: \
                \n\tName: {} \
                \n\tType: {} \
                \n\tValue: {} \
                \n\tDate: {} \
                \n\tCash date: {} \
                \n\tOrigin: {}'.format(self.name, self.flowType.name,
                                       self.value, self.date, self.cash_date,
                                       self.origin)
