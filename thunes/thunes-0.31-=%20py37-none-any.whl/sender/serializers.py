from rest_framework import serializers

from .models import Sender


class SenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sender
        fields = ['id', 'lastname', 'lastname2', 'middlename', 'firstname', 'nativename',
                  'nationality_country_iso_code', 'code', 'date_of_birth', 'country_of_birth_iso_code',
                  'gender', 'address', 'postal_code', 'city', 'country_iso_code', 'msisdn', 'email',
                  'id_type', 'id_country_iso_code', 'id_number', 'id_delivery_date', 'id_expiration_date', 'occupation',
                  'bank', 'bank_account', 'card', 'province_state', 'beneficiary_relationship', 'source_of_funds']
