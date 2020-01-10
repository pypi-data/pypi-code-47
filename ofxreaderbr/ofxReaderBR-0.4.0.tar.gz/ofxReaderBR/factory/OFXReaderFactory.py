from .ReaderAbstractFactory import ReaderAbstractFactory

from ofxReaderBR.reader.readercashflow import IReaderCashFlow, OFXReaderCashFlow

from ofxReaderBR.reader.readerbankstatement import IReaderBankStatement, OFXReaderBankStatement

from ofxReaderBR.reader.readercontroller import IReaderController
from ofxReaderBR.reader.OFXReaderController import OFXReaderController

class OFXReaderFactory(ReaderAbstractFactory):
    def createReaderController(self) -> IReaderController:
        return OFXReaderController()

    def createReaderBankStatement(self) -> IReaderBankStatement:
        return OFXReaderBankStatement()
    
    def createReaderCashFlow(self) -> IReaderCashFlow:
        return OFXReaderCashFlow()