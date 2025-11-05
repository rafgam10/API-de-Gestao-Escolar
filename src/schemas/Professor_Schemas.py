from pydantic import BaseModel, field_validator

class ProfessorSchema(BaseModel):
    
    id: int
    nome: str
    cpf: str
    especialidade: str
    
    @field_validator("cpf")
    def validar_cpf(self, valor):
        if len(valor) != 11:
            raise ValueError("CPF não tem caracteres suficiente.")