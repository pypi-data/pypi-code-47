import abc
import logging
from typing import List

from lxml import etree
from openpyxl import load_workbook

from ofxReaderBR.model.BankStatement import BankStatement
from ofxReaderBR.reader.pdf.PDFParserSantander import PDFParserSantander
from ofxReaderBR.reader.pdf.pdfParser import PDFParser

logger = logging.getLogger(__name__)


class IReaderController(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, factory, files=()) -> List[BankStatement]:
        pass


class BaseReaderController(abc.ABC):

    def __init__(self):
        self.status = {}

    @abc.abstractmethod
    def _get_result(self, file, options):
        pass

    def _read(self, factory, files):
        logger.debug(files)

        bank_stmts = []
        bs_reader = factory.createReaderBankStatement()

        if files:
            for file in files:
                options = {}

                result = self._get_result(file, options)

                try:
                    bs = bs_reader.read(factory, result, options=options)
                except (RuntimeError, ValueError) as err:
                    self.status[file.name] = 'error'
                    logger.error(f'Error reading file {file}: {err}')
                    continue

                bank_stmts.append(bs)
                self.status[file.name] = bs_reader.status

            return bank_stmts

        bs_null = BankStatement()
        return [bs_null]


class PDFReaderController(IReaderController, BaseReaderController):

    def read(self, factory, files=()) -> List[BankStatement]:
        return self._read(factory, files)

    def _get_result(self, file, options):
        try:
            parser = PDFParserSantander(file)
            result = parser.run()
            options['has_header'] = False
        except ValueError as err:
            logger.debug(err)
            parser = PDFParser()
            result = parser.run(file)
        return result


class XLSReaderController(IReaderController, BaseReaderController):

    def read(self, factory, files=()) -> List[BankStatement]:
        return self._read(factory, files)

    def _get_result(self, file, options):
        wb = load_workbook(file)
        return wb.active


class XMLReaderController(IReaderController, BaseReaderController):

    def read(self, factory, files=()):
        return self._read(factory, files)

    def _get_result(self, file, options):
        data = str(file.read())
        data = data[data.find('<OFX>'):]

        parser = etree.XMLParser(recover=True)
        tree = etree.fromstring(data, parser=parser)

        if tree.findall("CREDITCARDMSGSRSV1"):
            options['creditcard'] = True
        else:
            options['creditcard'] = False

        return tree
