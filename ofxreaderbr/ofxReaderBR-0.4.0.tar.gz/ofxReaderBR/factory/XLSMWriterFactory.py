from .WriterAbstractFactory import WriterAbstractFactory

from ofxReaderBR.writer.IWriterCashFlow import IWriterCashFlow
from ofxReaderBR.writer.IWriterBankStatement import IWriterBankStatement
from ofxReaderBR.writer.IWriterController import IWriterController

from ofxReaderBR.writer.xlsm.XLSMWriterCashFlow import XLSMWriterCashFlow
from ofxReaderBR.writer.xlsm.XLSMWriterBankStatement import XLSMWriterBankStatement
from ofxReaderBR.writer.xlsm.XLSMWriterController import XLSMWriterController

class XLSMWriterFactory(WriterAbstractFactory):
    def createWriterController(self) -> IWriterController:
        return XLSMWriterController()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return XLSMWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return XLSMWriterCashFlow()