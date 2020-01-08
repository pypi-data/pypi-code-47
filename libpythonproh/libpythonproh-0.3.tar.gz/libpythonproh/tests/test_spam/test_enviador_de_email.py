from libpythonproh.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'herminio.junior@bol.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'renzo@python.pro.br',
        'Cursos Python Pro',
        'Primeira Turma de Guido VOn Rossum aberta',
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['foor.com.br', 'hermiol.com.br']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'renzo@python.pro.br',
            'Cursos Python Pro',
            'Primeira Turma de Guido VOn Rossum aberta',)
