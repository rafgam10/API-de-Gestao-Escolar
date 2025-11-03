# src/controllers/alunos_controller.py
from datetime import date
from src.models.Alunos import Alunos
from src.settings.database import SessionLocal


def criar_aluno(nome: str, matricula: str, data_nasc: date, status: int):
    db = SessionLocal()
    try:
        novo_aluno = Alunos(
            nome=nome,
            matricula=matricula,
            data_nascimento=data_nasc,
            status=status
        )
        db.add(novo_aluno)
        db.commit()
        db.refresh(novo_aluno)
        return novo_aluno
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def listar_alunos():
    db = SessionLocal()
    try:
        return db.query(Alunos).all()
    finally:
        db.close()


def buscar_aluno_por_id(id: int):
    db = SessionLocal()
    try:
        return db.query(Alunos).filter(Alunos.id == id).first()
    finally:
        db.close()


def atualizar_aluno(matricula: str, novo_nome: str, nova_data_nasc: date, novo_status: int):
    db = SessionLocal()
    try:
        aluno = db.query(Alunos).filter(Alunos.matricula == matricula).first()
        if not aluno:
            return None

        aluno.nome = novo_nome
        aluno.data_nascimento = nova_data_nasc
        aluno.status = novo_status

        db.commit()
        db.refresh(aluno)
        return aluno
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def excluir_aluno(id: int):
    db = SessionLocal()
    try:
        aluno = db.query(Alunos).filter(Alunos.id == id).first()
        if not aluno:
            return None

        db.delete(aluno)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
