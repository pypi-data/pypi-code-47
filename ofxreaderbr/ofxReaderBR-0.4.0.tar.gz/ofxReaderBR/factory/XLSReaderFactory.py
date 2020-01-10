from .ReaderAbstractFactory import ReaderAbstractFactory

from ofxReaderBR.reader.readercashflow import IReaderCashFlow, XLSReaderCashFlow
from ofxReaderBR.reader.readerbankstatement import IReaderBankStatement, XLSReaderBankStatement

from ofxReaderBR.reader.readercontroller import XLSReaderController, IReaderController


class XLSReaderFactory(ReaderAbstractFactory):
    def createReaderController(self) -> IReaderController:
        return XLSReaderController()

    def createReaderBankStatement(self) -> IReaderBankStatement:
        return XLSReaderBankStatement()
    
    def createReaderCashFlow(self) -> IReaderCashFlow:
        return XLSReaderCashFlow()