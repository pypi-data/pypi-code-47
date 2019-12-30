from django.db import models

from sender.models import Sender
from beneficiary.models import Beneficiary
from quotation.models import Quotation


# Create your models here.
class Transaction(models.Model):
    TRANSACTION_STATUS = (
        ('10000', 'CREATED'),
        ('20000', 'CONFIRMED'),
        ('20110', 'CONFIRMED-UNDER-REVIEW-SLS'),
        ('20150', 'CONFIRMED-WAITING-FOR-PICKUP'),
        ('30000', 'REJECTED'),
        ('30110', 'REJECTED-SLS-SENDER'),
        ('30120', 'REJECTED-SLS-BENEFICIARY'),
        ('30200', 'REJECTED-INVALID-BENEFICIARY'),
        ('30201', 'REJECTED-BARRED-BENEFICIARY'),
        ('30210', 'REJECTED-INVALID-BENEFICIARY-DETAILS'),
        ('30305', 'REJECTED-LIMITATIONS-ON-TRANSACTION-VALUE'),
        ('30310', 'REJECTED-LIMITATIONS-ON-SENDER-VALUE'),
        ('30320', 'REJECTED-LIMITATIONS-ON-BENEFICIARY-VALUE'),
        ('30330', 'REJECTED-LIMITATIONS-ON-ACCOUNT-VALUE'),
        ('30350', 'REJECTED-LIMITATIONS-ON-SENDER-QUANTITY'),
        ('30360', 'REJECTED-LIMITATIONS-ON-BENEFICIARY-QUANTITY'),
        ('30370', 'REJECTED-LIMITATIONS-ON-ACCOUNT-QUANTITY'),
        ('30400', 'REJECTED-PAYER-CURRENTLY-UNAVAILABLE'),
        ('30500', 'REJECTED-INSUFFICIENT-BALANCE'),
        ('40000', 'CANCELLED'),
        ('50000', 'SUBMITTED'),
        ('60000', 'AVAILABLE'),
        ('70000', 'COMPLETED'),
        ('80000', 'REVERSED'),
        ('90000', 'DECLINED'),
        ('90110', 'DECLINED-SLS-SENDER'),
        ('90120', 'DECLINED-SLS-BENEFICIARY'),
        ('90200', 'DECLINED-INVALID-BENEFICIARY'),
        ('90201', 'DECLINED-BARRED-BENEFICIARY'),
        ('90202', 'DECLINED-UNSUPPORTED-BENEFICIARY'),
        ('90210', 'DECLINED-INVALID-BENEFICIARY-DETAILS'),
        ('90305', 'DECLINED-LIMITATIONS-ON-TRANSACTION-VALUE'),
        ('90310', 'DECLINED-LIMITATIONS-ON-SENDER-VALUE'),
        ('90320', 'DECLINED-LIMITATIONS-ON-BENEFICIARY-VALUE'),
        ('90330', 'DECLINED-LIMITATIONS-ON-ACCOUNT-VALUE'),
        ('90331', 'DECLINED-LIMITATIONS-ON-ACCOUNT-VALUE-DAILY'),
        ('90332', 'DECLINED-LIMITATIONS-ON-ACCOUNT-VALUE-WEEKLY'),
        ('90333', 'DECLINED-LIMITATIONS-ON-ACCOUNT-VALUE-MONTHLY'),
        ('90334', 'DECLINED-LIMITATIONS-ON-ACCOUNT-VALUE-YEARLY'),
        ('90350', 'DECLINED-LIMITATIONS-ON-SENDER-QUANTITY'),
        ('90360', 'DECLINED-LIMITATIONS-ON-BENEFICIARY-QUANTITY'),
        ('90370', 'DECLINED-LIMITATIONS-ON-ACCOUNT-QUANTITY'),
        ('90400', 'DECLINED-PAYER-CURRENTLY-UNAVAILABLE')
    )
    TRANSACTION_STATUS_CLASS = (
        ('1', 'CREATED'),
        ('2', 'CONFIRMED'),
        ('3', 'REJECTED'),
        ('4', 'CANCELLED'),
        ('5', 'SUBMITTED'),
        ('6', 'AVAILABLE'),
        ('7', 'COMPLETED'),
        ('8', 'REVERSED'),
        ('9', 'DECLINED'),
    )
    transaction_id = models.CharField(max_length=20, verbose_name='Related Transaction ID')
    quotation = models.OneToOneField(Quotation, max_length=50, verbose_name='Related Quotation Id',
                                     related_name='transaction', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=False,
                              default='10000', choices=TRANSACTION_STATUS, verbose_name='Transaction status code')
    status_message = models.CharField(max_length=50, blank=False, default='10000', choices=TRANSACTION_STATUS,
                                      verbose_name='Transaction status description')
    status_class = models.CharField(max_length=50, blank=False, default='1', choices=TRANSACTION_STATUS_CLASS,
                                    verbose_name='Transaction status class')
    status_class_message = models.CharField(max_length=50, blank=False, default='1', choices=TRANSACTION_STATUS_CLASS)
    external_id = models.CharField(max_length=50, blank=False, verbose_name='External ID')
    external_code = models.CharField(max_length=50, blank=False, verbose_name='External reference code')
    payer_transaction_reference = models.CharField(max_length=50, blank=True,
                                                   verbose_name='Payer transaction reference')
    payer_transaction_code = models.CharField(max_length=50, blank=True, verbose_name='Payer transaction code')
    creation_date = models.DateTimeField(max_length=50, auto_now=True, verbose_name='Creation date in HTTP format')
    expiration_date = models.DateTimeField(max_length=50, blank=True, null=True,
                                           verbose_name='Expiration date in HTTP format')
    sender = models.ForeignKey(Sender, related_name='senders', on_delete=models.CASCADE,
                               verbose_name='Sender information')
    beneficiary = models.ForeignKey(Beneficiary, related_name='beneficiaries',
                                    on_delete=models.CASCADE, verbose_name='Beneficiary information')
    callback_url = models.CharField(max_length=50, blank=False, verbose_name='Callback URL')
    wholesale_fx_rate = models.DecimalField(max_digits=15, blank=True, null=True, decimal_places=15,
                                            verbose_name='Wholesale FX rate')
    retail_rate = models.DecimalField(max_digits=15, blank=True, null=True, decimal_places=15,
                                      verbose_name='Retail rate')
    retail_fee = models.DecimalField(max_digits=15, blank=True, null=True, decimal_places=15, verbose_name='Retail fee')
    retail_fee_currency = models.CharField(max_length=50, blank=False,
                                           verbose_name='Retail fee currency in ISO 4217 format')
    purpose_of_remittance = models.CharField(max_length=50, blank=False, verbose_name='Purpose of remittance')
    additional_information_1 = models.CharField(max_length=50, blank=True, verbose_name='Additional information')
    additional_information_2 = models.CharField(max_length=50, blank=True, verbose_name='Additional information')
    additional_information_3 = models.CharField(max_length=50, blank=True, verbose_name='Additional information')

    def __str__(self):
        return 'Transaction {}'.format(self.external_id)

    def getconfirmtranslist(self):
        return Transaction.objects.filter(status='20000')

    def getunconfirmtranslist(self):
        return Transaction.objects.filter(status='10000')

    class Meta:
        index_together = (('sender', 'beneficiary'),)
        verbose_name = 'transaction'
        db_table = 'transaction'


class CreditPartyIdentity(models.Model):
    msisdn = models.CharField(max_length=50, blank=False, verbose_name='MSISDN in international format')
    bank_account_number = models.CharField(max_length=50, blank=False, verbose_name='Bank account number')
    swift_bic_code = models.CharField(max_length=50, blank=False, verbose_name='SWIFT-BIC code')

    def __str__(self):
        return "Credit Party Identity {} {} {}".format(self.msisdn, self.bank_account_number, self.swift_bic_code)

    class Meta:
        db_table = 'Credit Party Identity'
        verbose_name = 'Credit Party Identity'

# class TransactionSenderBeneficiary(models.Model):
#     sender = models.OneToOneField(Sender, verbose_name='sender entity in this transaction', on_delete=models.CASCADE)
#     beneficiary = models.OneToOneField(Beneficiary, verbose_name='beneficiary entity in this transaction',
#                                        on_delete=models.CASCADE)
