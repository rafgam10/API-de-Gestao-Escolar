from pydantic import BaseModel, field_validator

class MatriculaSchema(BaseModel):
    
    id: int
    ano_letivo: int
    status: int
    aluno_id: int
    disciplina_id: int
    
    @field_validator("status")
    def validar_status(self, valor):
        if valor != 0 and valor != 1:
            raise ValueError("Status deve ser 0 (inativo) ou 1 (ativo).")