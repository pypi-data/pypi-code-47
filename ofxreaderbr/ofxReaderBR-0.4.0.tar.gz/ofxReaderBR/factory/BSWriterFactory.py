from .WriterAbstractFactory import WriterAbstractFactory

from ofxReaderBR.writer.IWriterCashFlow import IWriterCashFlow
from ofxReaderBR.writer.IWriterBankStatement import IWriterBankStatement
from ofxReaderBR.writer.IWriterController import IWriterController

from ofxReaderBR.writer.bankstatement.BSWriterController import BSWriterController

class BSWriterFactory(WriterAbstractFactory):
    def createWriterController(self) -> IWriterController:
        return BSWriterController()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return None
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return None