import pytest

from libpythonproh.spam.enviador_de_email import Enviador
from libpythonproh.spam.main import EnviadorDeSpam
from libpythonproh.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='renzo', email='renzo@python.pro.com.br'),
            Usuario(nome='herminio', email='herminio@python.pro.com.br')
        ],
        [
            Usuario(nome='renzo', email='renzo@python.pro.com.br')
        ]
    ]
)
def test_qde_envio_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso de Python Profissional',
        'Confira os Módulos Fantastico'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, destinatario, remetente, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo):
        self.qtd_email_enviados += 1



def test_parametros_de_spam(sessao, usuarios):
    Usuario(nome='renzo', email='renzo@python.pro.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock(Enviador)
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'Luciano@python.pro.br',
        'Curso de Python Profissional',
        'Confira os Módulos Fantastico'
    )
    assert enviador.parametros_de_envio == (
        'Luciano@python.pro.br',
        'Curso de Python Profissional',
        'Confira os Módulos Fantastico'
    )
