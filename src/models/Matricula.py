from src.settings.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Matricula(Base):
    
    __tablename__ = "matricula"
    
    id = Column(Integer, primary_key=True)
    ano_letivo = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    
    # FK
    aluno_id = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    disciplina_id = Column(Integer, ForeignKey("disciplina.id", nullable=False))
    
    aluno = relationship("Alunos", back_populates="matriculas")
    disciplina = relationship("Disciplina", back_populates="matriculas")
    notas = relationship("Nota", back_populates="matricula", cascade="all, delete-orphan")
    frequencia = relationship("Frequencia", back_populates="matricula", cascade="all, delete-orphan")