import abc

from ofxReaderBR.writer.IWriterBankStatement import IWriterBankStatement
from ofxReaderBR.writer.IWriterCashFlow import IWriterCashFlow

class WriterAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createWriterBankStatement(self) -> IWriterBankStatement:
        pass

    @abc.abstractmethod
    def createWriterCashFlow(self) -> IWriterCashFlow:
        pass