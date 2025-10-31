from src.settings.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Disciplina(Base):
    
    __tablename__ = "disciplina"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    carga_horaria = Column(Integer, nullable=False)
    professor_id = Column(Integer, ForeignKey('professor.id'), nullable=False)
    
    professor = relationship("Professor", back_populates="disciplinas")