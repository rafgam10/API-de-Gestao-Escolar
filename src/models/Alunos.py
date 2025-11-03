from src.settings.database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Alunos(Base):
    __tablename__ = "alunos"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    status = Column(Integer, nullable=False)
    
    matriculas = relationship("Matricula", back_populates="aluno", cascade="all, delete-orphan")
