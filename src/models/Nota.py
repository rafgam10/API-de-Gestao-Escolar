from src.settings.database import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Nota(Base):
    
    __tablename__ = "nota"
    
    
    id = Column(Integer, primary_key=True)
    bimestre = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

    #FK
    matricula_id = Column(Integer, ForeignKey("matricula.id"), nullable=False)
    
    matricula = relationship("Matricula", back_populates="notas")
