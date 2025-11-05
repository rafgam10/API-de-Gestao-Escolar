from pydantic import BaseModel, field_validator

class NotaSchema(BaseModel):
    
    id: int
    bimestre: int
    nota: float
    matricula_id: int
    
    @field_validator("nota")
    def validar_nota(self, valor):
        return round(valor, 1)