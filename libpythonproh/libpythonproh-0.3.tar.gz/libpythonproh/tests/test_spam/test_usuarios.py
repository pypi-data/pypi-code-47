from libpythonproh.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='renzo', email='renzo@python.pro.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='renzo', email='renzo@python.pro.com.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
