import abc
import logging
from decimal import Decimal

from ofxReaderBR.model.BankStatement import BankStatement
from ofxReaderBR.model.Origin import Origin

logger = logging.getLogger(__name__)


class IReaderBankStatement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def read(self, factory, ofx, options) -> BankStatement:
        pass


class OFXReaderBankStatement(IReaderBankStatement):

    def __init__(self):
        self.status = 'waiting'

    def read(self, factory, ofx, options=None):
        signal_multiplier = 1
        if options:
            if options['creditcard'] is True and options[
                    'bancodobrasil'] is False:
                signal_multiplier = -1

        stmts = ofx.statements

        cs_reader = factory.createReaderCashFlow()

        bank_stmts = []

        self.status = 'complete'
        # btmts -> bs
        for stmt in stmts:
            bs = BankStatement()
            account = stmt.account
            origin = Origin(account)

            txs = stmt.transactions

            for tx in txs:
                cs = cs_reader.read(factory, tx)
                cs.value = Decimal(cs.value)
                cs.value *= signal_multiplier

                cs.origin = origin
                if origin.is_bank_account():
                    cs.cash_date = cs.date
                elif options['creditcard'] and options.get('bradesco'):
                    cs.cash_date = stmt.dtstart

                if cs.is_valid():
                    if cs.value >= Decimal(0.0):
                        bs.inflows.append(cs)
                    else:
                        bs.outflows.append(cs)
                else:
                    self.status = 'incomplete'

            bank_stmts.append(bs)

        return bank_stmts


class PDFReaderBankStatement(IReaderBankStatement):

    def __init__(self):
        self.status = 'waiting'

    def read(self, factory, ofx, options=None) -> BankStatement:
        bs = BankStatement()

        result = ofx

        cs_reader = factory.createReaderCashFlow()
        header_row = True
        self.status = 'complete'
        for row in result:
            # Pulando o cabecalho
            has_header = options.get('has_header', True)
            if header_row and has_header:
                header_row = False
                continue

            cs = cs_reader.read(factory, row)
            if not cs.is_valid():
                self.status = 'incomplete'
            elif '-' not in cs.value:
                bs.inflows.append(cs)
            else:
                bs.outflows.append(cs)

        return bs


class XMLReaderBankStatement(IReaderBankStatement):

    def __init__(self):
        self.status = 'waiting'

    def read(self, factory, ofx, options=None) -> BankStatement:
        bs = BankStatement()

        if options is not None and options.get('creditcard'):
            tran_list = ofx.find('CREDITCARDMSGSRSV1').find('CCSTMTTRNRS').find(
                'CCSTMTRS')

            # Origin
            institution = None
            branch = None
            account_id = tran_list.find('CCACCTFROM').find('ACCTID').text
            account_type = 'CREDITCARD'
        else:
            tran_list = ofx.find('BANKMSGSRSV1').find('STMTTRNRS').find(
                'STMTRS')

            # Origin
            account = tran_list.find('BANKACCTFROM')
            institution = account.find('BANKID').text
            branch = account.find('BRANCHID').text
            account_id = account.find('ACCTID').text
            account_type = 'BANKACCOUNT'

        origin = Origin(
            account_id=account_id,
            branch=branch,
            institution=institution,
            type=account_type,
        )

        if tran_list is not None:
            tran_list = tran_list.find('BANKTRANLIST')

        txs = tran_list.findall('STMTTRN')

        cs_reader = factory.createReaderCashFlow()
        self.status = 'complete'
        for tx in txs:
            cs = cs_reader.read(factory, tx)
            cs.origin = origin
            cs.value = float(cs.value)
            if cs.is_valid():
                if cs.value >= float(0.0):
                    bs.inflows.append(cs)
                else:
                    bs.outflows.append(cs)
            else:
                self.status = 'incomplete'

        return bs


class XLSReaderBankStatement(IReaderBankStatement):

    def __init__(self):
        self.status = 'waiting'

    def read(self, factory, ofx, options=None) -> BankStatement:
        bs = BankStatement()

        ws = ofx

        cs_reader = factory.createReaderCashFlow()
        header_row = True
        self.status = 'complete'
        for row in ws.values:
            # Pulando o cabeçalho
            if header_row:
                header_row = False
                continue

            cs = cs_reader.read(factory, row)
            if cs.is_valid():
                if isinstance(cs.value, str):
                    cs.value = Decimal(cs.value.replace(',', '.'))
                if cs.value >= Decimal(0.0):
                    bs.inflows.append(cs)
                else:
                    bs.outflows.append(cs)
            else:
                self.status = 'incomplete'

        return bs
