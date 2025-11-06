from src.models.Matricula import Matricula
from src.models.Alunos import Alunos
from src.models.Disciplina import Disciplina
from src.settings.database import SessionLocal


def matricula_aluno_em_disciplina(ano_letivo:int, status:int, aluno_id:int, disciplina_id:int) -> None:
    db = SessionLocal()
    
    try:
        aluno = db.query(Alunos).filter(Alunos.id == aluno_id).first()
        if not aluno:
            return f"Aluno não encontrado: {aluno}"
        id_aluno = aluno.id 
        disciplina = db.query(Disciplina).filter(Disciplina.id == disciplina_id).first()
        if not disciplina:
            return f"Disciplina não encontrado: {disciplina}"
        id_disciplina = disciplina.id
        
        matricula = Matricula(ano_letivo=ano_letivo, status=status, aluno_id=id_aluno, disciplina_id=disciplina_id)
        db.add(matricula)
        db.commit()
        return f"Cadastrado da matricula criando."
    except Exception as e:
        db.rollback()
        return e
    finally:
        db.close()

def listar_todas_matriculas() -> list:
    db = SessionLocal()
    
    try:
        lista_matriculas = db.query(Matricula).all()
        return lista_matriculas
    except Exception as e:
        return e
    finally:
        db.close()

def buscar_matricula_por_aluno(aluno_nome:str) -> None:
    db = SessionLocal()
    
    try:
        id_aluno = db.query(Alunos).filter(Alunos.nome == aluno_nome).first().id
        matricula_select = db.query(Matricula).filter(Matricula.aluno_id == id_aluno).first()
        return matricula_select
    except Exception as e:
        return e
    finally:
        db.close()

def atualizar_status(id_matricula:int, novo_status:int) -> None:
    db = SessionLocal()
    
    try:
        matricula_select = db.query(Matricula).filter(Matricula.id == id_matricula).first()
        matricula_select.status = novo_status
        
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()

def excluir_matricula(id_matricula:int) -> None:
    db = SessionLocal()
    
    try:
        matricula_select = db.query(Matricula).filter(Matricula.id == id_matricula).first()
        db.delete(matricula_select)
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()