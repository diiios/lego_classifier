from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class PartType(Base): #Тип детали
  __tablename__ = 'тип_детали'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)

  id_classificator = Column(Integer, ForeignKey('классификатор.id'))
  classificator = relationship("Classificator", backref="classificator_part_types", foreign_keys=[id_classificator])

class Part(Base): #Деталь
  __tablename__ = 'деталь'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  color = Column(String(100))
  code = Column(String(100), nullable=False)
  size_width = Column(Integer)
  size_length = Column(Integer)
  size_height = Column(Integer)
  weight = Column(Integer)

  id_type = Column(Integer, ForeignKey('тип_детали.id'))
  type = relationship("PartType", backref="type_details", foreign_keys=[id_type])

  id_classificator = Column(Integer, ForeignKey('классификатор.id'))
  classificator = relationship("Classificator", backref="classificator_details", foreign_keys=[id_classificator])

