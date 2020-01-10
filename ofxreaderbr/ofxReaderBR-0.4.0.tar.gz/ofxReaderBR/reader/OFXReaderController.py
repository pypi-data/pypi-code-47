import datetime
import logging
from typing import List

from pytz import timezone

from ofxReaderBR.factory.XMLReaderFactory import XMLReaderFactory
from ofxReaderBR.model.BankStatement import BankStatement
from ofxReaderBR.reader.readercontroller import IReaderController, BaseReaderController

logger = logging.getLogger(__name__)

from ofxtools import OFXTree


class OFXReaderController(IReaderController, BaseReaderController):

    def _get_result(self, file, options):
        file.seek(0)
        tree = OFXTree()
        tree.parse(file)
        self.treatBradescoException(tree)

        # check creditcard
        root = tree.getroot()
        if root.findall("CREDITCARDMSGSRSV1"):
            options['creditcard'] = True

            # KN-177 - Check if Bradesco credit card
            ccstmttrnrs = root.findall(
                'CREDITCARDMSGSRSV1')[0].findall('CCSTMTTRNRS')[0]
            banktranlist = ccstmttrnrs.findall(
                'CCSTMTRS')[0].findall('BANKTRANLIST')[0]
            dtstart = banktranlist.findall('DTSTART')[0]
            dtend = banktranlist.findall('DTEND')[0]
            if dtstart.text == dtend.text:
                options['bradesco'] = True
        else:
            options['creditcard'] = False

        options['bancodobrasil'] = False
        fi = root.findall("SIGNONMSGSRSV1")[0].findall(
            "SONRS")[0].findall("FI")
        if fi:
            org = fi[0].findall("ORG")
            if (org != None and "Banco do Brasil" in org[0].text):
                options['bancodobrasil'] = True

        return tree.convert()

    def read(self, factory, files=[]) -> List[BankStatement]:
        bank_statements = []
        for file in files:
            try:
                bs = self._read(factory, [file])
                bank_statements.extend(bs)
            except IndexError:
                # ofx nao consegue ler versao 220. Ler como XML
                file.seek(0)
                xml_factory = XMLReaderFactory()
                xml_controller = xml_factory.createReaderController()
                bs = xml_controller.read(xml_factory, [file])
                bank_statements.extend(bs)
                self.status.update(xml_controller.status)
        return bank_statements

    # Este tratamento de erro tem que ser melhor descrito
    def treatBradescoException(self, tree):
        root = tree.getroot()
        dtServer = root.findall("SIGNONMSGSRSV1")[0].findall(
            "SONRS")[0].findall("DTSERVER")[0]
        try:
            if int(dtServer.text) == 0:
                unknown_date_in_the_past = datetime.datetime(
                    1985, 10, 21, tzinfo=timezone('Brazil/East'))
                dtServer.text = unknown_date_in_the_past
        except ValueError:
            pass
            # se dtServer for um datetime, ele da erro na conversao para int
            # logger.info('Correcting DTServer')

        # se for cartao de credito, a data do balanco vem errada
        try:
            creditCardTransRs = root.findall("CREDITCARDMSGSRSV1")[0].findall(
                "CCSTMTTRNRS")

            for c in creditCardTransRs:
                dt_balance = c.findall("CCSTMTRS")[0].findall(
                    "LEDGERBAL")[0].findall("DTASOF")[0]

                try:
                    if int(dt_balance.text) == 0:
                        unknown_date_in_the_past = datetime.datetime(
                            1985, 10, 21, tzinfo=timezone('Brazil/East'))
                        dt_balance.text = unknown_date_in_the_past
                except ValueError:
                    pass
        except IndexError:
            pass
