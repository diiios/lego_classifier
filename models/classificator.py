from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database import Base

class Classificator(Base): #Классификатор
  __tablename__ = 'классификатор'

  id = Column(Integer, primary_key=True)
  name = Column(String(100), nullable=False)
  node_type = Column(String(100), nullable=False)
  meshering_unit = Column(String(100)) 
  sort_order = Column(Integer, default=0) #Порядок сортировки среди узлов одного уровня

  parent_id = Column(Integer, ForeignKey('классификатор.id'))
  children = relationship("Classificator", backref="parent", foreign_keys=[parent_id], remote_side=[id])


# node.children — список дочерних узлов
# node.parent — родительский узел
# node.parent_id — просто число (id родителя)

