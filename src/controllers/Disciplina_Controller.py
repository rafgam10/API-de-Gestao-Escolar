from src.models.Disciplina import Disciplina
from src.models.Professor import Professor
from src.settings.database import SessionLocal

def criar_disciplina(nome:str, carga_horario:int, professor_id:int) -> None:
    db = SessionLocal()
    
    try: 
        professor_select = db.query(Professor).filter(Professor.id == professor_id).first()
        
        if not professor_select:
            return f"Professor Resposável não encontrado..."
        
        nova_disciplina = Disciplina(nome=nome, carga_horario=carga_horario, professor_id=professor_id)
        db.add(nova_disciplina)
        db.commit()
        return f"Nova disciplina adicionada com sucesso {nova_disciplina}."
    except Exception as e:
        return e
    finally:
        db.close()

def lista_disciplinas() -> list:
    db = SessionLocal()
    
    try:
        lista_de_disciplina = db.query(Disciplina).all()
        return lista_disciplinas
    except Exception as e:
        return e
    finally:
        db.close()

def buscar_disciplina_pelo_nome(nome:str) -> None:
    db = SessionLocal()
    
    try:
        disciplina_select = db.query(Disciplina).filter(Disciplina.nome == nome).first()
        return disciplina_select
    except Exception as e:
        return e
    finally:
        db.close()

def atualizar_dados_disciplina(id: int, nome:str, carga_horario: int, professor_id:int) -> None:
    db = SessionLocal()
    
    try:
        disciplina_select = db.query(Disciplina).filter(Disciplina.id == id)
        if not disciplina_select:
            return f"Disciplina não foi encontrado..."
        
        disciplina_select.nome = nome
        disciplina_select.carga_horario = carga_horario
        disciplina_select.professor_id = professor_id
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()

def excluir_disciplina(id:int):
    db = SessionLocal()
    
    try:
        disciplina_select = db.query(Disciplina).filter(Disciplina.id == id).first()
        db.delete(disciplina_select)
        db.commit()
        return
    except Exception as e:
        return e
    finally:
        db.close()
    