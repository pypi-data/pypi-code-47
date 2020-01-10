from .ReaderAbstractFactory import ReaderAbstractFactory

from ofxReaderBR.reader.readercashflow import IReaderCashFlow, XMLReaderCashFlow
from ofxReaderBR.reader.readerbankstatement import IReaderBankStatement, XMLReaderBankStatement
from ofxReaderBR.reader.readercontroller import IReaderController, XMLReaderController


class XMLReaderFactory(ReaderAbstractFactory):
    def createReaderController(self) -> IReaderController:
        return XMLReaderController()

    def createReaderBankStatement(self) -> IReaderBankStatement:
        return XMLReaderBankStatement()
    
    def createReaderCashFlow(self) -> IReaderCashFlow:
        return XMLReaderCashFlow()