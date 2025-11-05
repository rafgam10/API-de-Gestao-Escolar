from pydantic import BaseModel, field_validator


class DisciplinaSchema(BaseModel):
    
    id: int
    nome: str
    carga_horario: int
    professor_id: int
    
    