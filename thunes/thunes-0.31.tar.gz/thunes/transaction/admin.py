from django.contrib import admin

from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['status', 'status_message', 'status_class', 'status_class_message', 'external_id',
                    'external_code', 'payer_transaction_reference', 'payer_transaction_code', 'creation_date',
                    'expiration_date', 'callback_url', 'wholesale_fx_rate', 'retail_rate',
                    'retail_fee', 'retail_fee_currency', 'purpose_of_remittance']

