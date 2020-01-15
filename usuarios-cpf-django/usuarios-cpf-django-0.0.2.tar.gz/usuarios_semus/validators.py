from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pycpfcnpj import cpf

def validate_cpf(value):
    if not cpf.validate(value):
        raise ValidationError(
            _('%(value)s is not an valid cpf number'),
            params={'value': value},
        )