from datetime import date
from pydantic import BaseModel, constr, field_validator


class AlunoSchema(BaseModel):
    
    id: int
    nome: str
    matricula: str
    data_nascimento: date
    status: int
    
    @field_validator("status")
    def validar_status(self, valor):
        # Corrigido: precisa ser AND
        if valor != 0 and valor != 1:
            raise ValueError("Status deve ser 0 (inativo) ou 1 (ativo).")
        return valor
    
    @field_validator("matricula")
    def validar_matricula(self, valor):
        if len(valor) != 9:
            raise ValueError("A matricula precisa ter no máximo 9 caracteres.")
        
        if valor not in "-":
            raise ValueError("Matricula está com formatação incorreta não possuir (-).")
        return valor
    
            