from django.contrib import admin
from .models import Sender

# Register your models here.
@admin.register(Sender)
class SenderAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'nationality_country_iso_code', 'date_of_birth', 'gender',
                    'country_of_birth_iso_code', 'address', 'postal_code', 'city', 'country_iso_code',
                    'msisdn', 'email', 'id_type', 'id_country_iso_code', 'id_number', 'id_delivery_date',
                    'occupation', 'beneficiary_relationship']
    list_editable = ['date_of_birth', 'gender', 'id_type', 'id_delivery_date', 'beneficiary_relationship']
