from app.funcao import funcao_hello_world

def test_funcao_retorna__hello_workd():
    saida = funcao_hello_world()
    gabarito = "ola turma"
    assert saida == gabarito