from src.models.Nota import Nota
from src.models.Matricula import Matricula
from src.models.Alunos import Alunos
from src.settings.database import SessionLocal

def registrar_nota(bimestre:int, nota:float, matricula_id:int) -> None:
    db = SessionLocal()
    
    try:
        id_matricula = db.query(Matricula).filter(Matricula.id == matricula_id).first().id
        obj_nota = Nota(bimestre=bimestre, nota=nota, matricula_id=id_matricula)
        db.add(obj_nota)
        db.commit()
        return f"Nota registrado {obj_nota}."
    except Exception as e:
        db.rollback()
        return e
    finally:
        db.close()

def listar_notas_por_aluno(nome_aluno:str) -> list:
    db = SessionLocal()
    
    try:
        obj_aluno_select = db.query(Alunos).filter(Alunos.nome == nome_aluno).first()
        listar_notas = db.query(Nota).filter(Nota.matricula_id == obj_aluno_select.matricula)
        return listar_notas
    except Exception as e:
        return e
    finally:
        db.close()

def atualizar_nota(id_nota:int, nota_nova: float) -> None:
    db = SessionLocal()
    
    try:
        nota_select = db.query(Nota).filter(Nota.id == id_nota).first()
        nota_select.nota = nota_nova
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()

def excluir_nota(id_nota:int) -> None:
    db = SessionLocal()
    
    try:
        obj_nota_select = db.query(Nota).filter(Nota.id == id_nota).first()
        db.delete(obj_nota_select)
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()

def calcular_media_final() -> None:
    pass