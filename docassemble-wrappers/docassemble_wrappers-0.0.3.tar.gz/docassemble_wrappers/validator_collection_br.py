from docassemble.base.util import validation_error
from validator_collection_br import validators_br

def validate_cpf(value):
    # Docassemble only performs validation if the field is filled
    if not value:
        return True
    
    try:
        value = validators_br.cpf(value)
    except Exception as e:
        msg = validation_error(str(e))
        validation_error(msg)
    return True


def validate_cnpj(value):
    # Docassemble only performs validation if the field is filled
    if not value:
        return True
    
    try:
        value = validators_br.cnpj(value)
    except Exception as e:
        msg = validation_error(str(e))
        validation_error(msg)

    return True
