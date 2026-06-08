from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Set(Base): #Набор
  __tablename__ = 'набор'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  number_of_set = Column(String(100), nullable=False)
  price = Column(Numeric(100, 5), nullable=False)
  year_of_issue = Column(Integer, nullable=False)
  count_of_details = Column(Integer, nullable=False)
  description = Column(String(1000))

  id_theme = Column(Integer, ForeignKey('тематика.id'))
  theme = relationship("Theme", backref="theme_sets", foreign_keys=[id_theme])

  id_year_category = Column(Integer, ForeignKey('возрастная_категория.id'))
  age_category = relationship("AgeCategory", backref="age_categories", foreign_keys=[id_year_category])

  id_classificator = Column(Integer, ForeignKey('классификатор.id'))
  classificator = relationship("Classificator", backref="classificator_sets", foreign_keys=[id_classificator])


class Details_in_set(Base): #Состав набора
  __tablename__ = 'состав_набора'

  id = Column(Integer, primary_key=True)

  count_detail = Column(Integer)
  
  id_set = Column(Integer, ForeignKey('набор.id'))
  set = relationship("Set", backref="details_in_set", foreign_keys=[id_set])

  id_detail = Column(Integer, ForeignKey('деталь.id'))
  detail = relationship("Part", backref="detail_sets", foreign_keys=[id_detail])