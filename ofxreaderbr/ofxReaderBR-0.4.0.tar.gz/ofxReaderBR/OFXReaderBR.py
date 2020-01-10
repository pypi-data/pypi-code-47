from .factory.OFXReaderFactory import OFXReaderFactory
from .factory.XLSReaderFactory import XLSReaderFactory
from .factory.PDFReaderFactory import PDFReaderFactory
from .factory.XLSMWriterFactory import XLSMWriterFactory
from .factory.BSWriterFactory import BSWriterFactory

from .utils.BankStatementAdder import BankStatementAdder

from .model.BankStatement import BankStatement

import logging

logger = logging.getLogger(__name__)


class OFXReaderBR(object):

    def run(self, files, returnBankStatement=False):
        # ler o caminho do arquivo e verificar se ele existe
        if (not files):
            logger.info('No files specified.')
            return

        xls_files = []
        ofx_files = []
        pdf_files = []

        for file in files:
            try:
                if '.xls' in file.filename:
                    xls_files.append(file)
                elif '.pdf' in file.filename:
                    pdf_files.append(file)
                else:
                    ofx_files.append(file)
            except AttributeError:
                if '.xls' in file.name:
                    xls_files.append(file)
                elif '.pdf' in file.name:
                    pdf_files.append(file)
                else:
                    ofx_files.append(file)

        logger.info(ofx_files)
        logger.info(xls_files)
        logger.info(pdf_files)

        file_status = {}

        # chamar o leitor ofx
        factory_ofx = OFXReaderFactory()
        reader_controller = factory_ofx.createReaderController()
        ofx_bank_stmts = reader_controller.read(factory_ofx, files=ofx_files)
        ofx_status = reader_controller.status
        file_status.update(ofx_status)

        # chamar o leitor xls
        factory_xls = XLSReaderFactory()
        reader_controller = factory_xls.createReaderController()
        xls_bank_stmts = reader_controller.read(factory_xls, files=xls_files)
        xls_status = reader_controller.status
        file_status.update(xls_status)

        # chamar o leitor pdf
        factory_pdf = PDFReaderFactory()
        reader_controller = factory_pdf.createReaderController()
        pdf_bank_stmts = reader_controller.read(factory_pdf, files=pdf_files)
        pdf_status = reader_controller.status
        file_status.update(pdf_status)

        bank_stmt = BankStatement()
        logger.info(bank_stmt)

        adder = BankStatementAdder()

        for bs in ofx_bank_stmts:
            bank_stmt = adder.add(bank_stmt, bs, True)
        for bs in xls_bank_stmts:
            bank_stmt = adder.add(bank_stmt, bs, True)
        for bs in pdf_bank_stmts:
            bank_stmt = adder.add(bank_stmt, bs, True)
        bank_stmts = [bank_stmt]

        if returnBankStatement:
            factory = BSWriterFactory()
        else:
            # chamar o escritor xlsm
            factory = XLSMWriterFactory()

        writer_controller = factory.createWriterController()
        return writer_controller.write(bank_stmts, factory), file_status

    def createXLSX(self, bankStatement):
        print(bankStatement)
