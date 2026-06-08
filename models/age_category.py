from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class AgeCategory(Base): #Возрастная категория
  __tablename__ = 'возрастная_категория'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  min_age = Column(Integer, nullable=False)
  max_age = Column(Integer, nullable=False)
