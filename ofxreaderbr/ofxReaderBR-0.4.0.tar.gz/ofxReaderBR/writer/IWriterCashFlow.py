import abc

from ofxReaderBR.model.CashFlow import CashFlow

class IWriterCashFlow(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, cashFlow: CashFlow, factory, output):
        pass