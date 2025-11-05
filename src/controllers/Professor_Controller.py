from src.models.Professor import Professor
from src.settings.database import SessionLocal


def cadastrar_professor(nome:str, cpf:str, especialidade:str) -> None:
    db = SessionLocal()
    
    try:
        novo_professor = Professor(nome=nome, cpf=cpf, especialidade=especialidade)
        db.add(novo_professor)
        db.commit()
        return f"Professor cadastrado com sucesso!"
    except Exception as e:
        db.rollback()
        return f"Erro: {e}"
    finally:
        db.close()    

def listar_professores() -> None:
    db = SessionLocal()
    
    try:
        lista_professores = db.query(Professor).all()
        return listar_professores
    except Exception as e:
        return e
    finally:
        db.close()

def buscasr_cpf_professor(cpf:str):
    db = SessionLocal()
    
    try:
        professor_select = db.query(Professor).filter(Professor.cpf == cpf).first()
        if not professor_select:
            return f"Professor não encontrado."
        
        return professor_select
    except Exception as e:
        return e
    finally:
        db.close()
        
def atualizar_dados(id:int, nome:str, cpf:str, especialidade:str):
    db = SessionLocal()
    
    try:
        professor_select = db.query(Professor).filter(Professor.id == id).first()
        professor_select.nome = nome
        professor_select.cpf = cpf
        professor_select.especialidade = especialidade
        db.commit()
    except Exception as e:
        return e
    finally:
        db.close()
        
def excluir_professor(id:int):
    db = SessionLocal()
    
    try:
        professor_select = db.query(Professor).filter(Professor.id == id).first()
        db.delete(professor_select)
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()
