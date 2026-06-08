from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Theme(Base): #Тематика
  __tablename__ = 'тематика'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  description = Column(String(1000))

  id_classificator = Column(Integer, ForeignKey('классификатор.id'))
  classificator = relationship("Classificator", backref="classificator_themes", foreign_keys=[id_classificator])
