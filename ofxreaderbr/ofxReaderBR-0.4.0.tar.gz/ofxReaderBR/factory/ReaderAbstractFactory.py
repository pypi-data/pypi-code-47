import abc

from ofxReaderBR.reader.readerbankstatement import IReaderBankStatement
from ofxReaderBR.reader.readercashflow import IReaderCashFlow

class ReaderAbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createReaderBankStatement(self) -> IReaderBankStatement:
        pass

    @abc.abstractmethod
    def createReaderCashFlow(self) -> IReaderCashFlow:
        pass