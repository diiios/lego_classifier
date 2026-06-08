from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Figure(Base): #Фигурка
  __tablename__ = 'мини_фигурка'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  series = Column(String(100), nullable=False)
  code = Column(String(100), nullable=False)
  id_classificator = Column(Integer, ForeignKey('классификатор.id'))
  classificator = relationship("Classificator", backref="classificator_figures", foreign_keys=[id_classificator])

class Figures_in_set(Base): #Фигурки в наборе
  __tablename__ = 'фигурки_в_наборе'

  id = Column(Integer, primary_key=True)
  
  id_set = Column(Integer, ForeignKey('набор.id'))
  set = relationship("Set", backref="figures_in_set", foreign_keys=[id_set])

  id_figure = Column(Integer, ForeignKey('мини_фигурка.id'))
  figure = relationship("Figure", backref="figure_sets", foreign_keys=[id_figure]) 
