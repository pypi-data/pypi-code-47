class Enviador():

    def enviar(self, destinatario, remetente, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f'Email de destinatario inválido: {remetente}')
        return destinatario


class EmailInvalido(Exception):
    pass
