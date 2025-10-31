from src.settings.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Professor(Base):
    
    __tablename__ = "professor"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)
    
    disciplinas = relationship("Disciplina", back_populates="professor", cascade="all, delete-orphan")