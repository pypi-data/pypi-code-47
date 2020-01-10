from .ReaderAbstractFactory import ReaderAbstractFactory

from ofxReaderBR.reader.readercashflow import IReaderCashFlow, PDFReaderCashFlow
from ofxReaderBR.reader.readerbankstatement import IReaderBankStatement, PDFReaderBankStatement

from ofxReaderBR.reader.readercontroller import PDFReaderController, IReaderController


class PDFReaderFactory(ReaderAbstractFactory):
    def createReaderController(self) -> IReaderController:
        return PDFReaderController()

    def createReaderBankStatement(self) -> IReaderBankStatement:
        return PDFReaderBankStatement()
    
    def createReaderCashFlow(self) -> IReaderCashFlow:
        return PDFReaderCashFlow()