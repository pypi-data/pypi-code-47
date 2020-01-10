from .WriterAbstractFactory import WriterAbstractFactory

from ofxReaderBR.writer.IWriterCashFlow import IWriterCashFlow
from ofxReaderBR.writer.IWriterBankStatement import IWriterBankStatement
from ofxReaderBR.writer.IWriterController import IWriterController

from ofxReaderBR.writer.csv.CSVWriterCashFlow import CSVWriterCashFlow
from ofxReaderBR.writer.csv.CSVWriteBankStatement import CSVWriterBankStatement
from ofxReaderBR.writer.csv.CSVWriterController import CSVWriterController

class CSVWriterFactory(WriterAbstractFactory):
    def createWriterController(self) -> IWriterController:
        return CSVWriterController()

    def createWriterBankStatement(self) -> IWriterBankStatement:
        return CSVWriterBankStatement()
    
    def createWriterCashFlow(self) -> IWriterCashFlow:
        return CSVWriterCashFlow()