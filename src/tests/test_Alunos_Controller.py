from src.models.Alunos import Alunos
from datetime import date

def test_criar_aluno():
    aluno_test = Alunos(
        nome="test",
        matricula="000-123456",
        data_nascimento=date(2020, 3, 12),
        status=1
    )

    assert aluno_test.nome == "test"
    assert aluno_test.matricula == "000-123456"
    assert aluno_test.status == 1
    assert aluno_test.data_nascimento == date(2020, 3, 12)


def test_lista_alunos():
    pass

def test_busca_aluno_id():
    pass

def test_atualizar_aluno():
    pass

def test_excluir_aluno():
    pass