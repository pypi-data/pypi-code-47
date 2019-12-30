from rest_framework import serializers

from .models import Transaction
# from sender.serializers import SenderSerializer
# from beneficiary.serializers import BeneficiarySerializer


class TransactionSerializer(serializers.ModelSerializer):
    # senders_entity = SenderSerializer()
    # beneficiaries_entities = BeneficiarySerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'status', 'status_message', 'status_class', 'status_class_message', 'quotation', 'external_id',
                  'external_code', 'payer_transaction_reference', 'payer_transaction_code', 'creation_date',
                  'expiration_date', 'callback_url', 'wholesale_fx_rate', 'retail_rate', 'sender', 'beneficiary',
                  'retail_fee', 'retail_fee_currency', 'purpose_of_remittance']
