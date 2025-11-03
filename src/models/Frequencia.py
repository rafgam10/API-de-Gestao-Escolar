from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from src.settings.database import Base

class Frequencia(Base):
    __tablename__ = "frequencia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    matricula_id = Column(Integer, ForeignKey("matricula.id"), nullable=False)
    data = Column(Date, nullable=False)
    presente = Column(Boolean, nullable=False)

    matricula = relationship("Matricula", back_populates="frequencia")
