from src.settings.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Frequencia(Base):
    
    __tablename__ = "frequencia"
    
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    presente = Column(Integer, nullable=False)
    
    #Fk 
    matricula_id = Column(Integer, ForeignKey("matricula.id"), nullable=False)
    
    matricula = relationship("Matricula", back_populates="frequencias")