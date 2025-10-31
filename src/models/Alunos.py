from src.settings.database import get_db, Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Alunos(Base):
    __tablename__ = "alunos"
    
    db = get_db()
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    status = Column(Integer, nullable=False)
    
    matricula = relationship("", back_populates="")