from sqlalchemy.orm import Session
from sqlalchemy import text
from models.classificator import Classificator
from sqlalchemy import nulls_first

def get_all_categories(db: Session):
  return db.query(Classificator).order_by(nulls_first(Classificator.parent_id), Classificator.sort_order).all()

def get_category(db: Session, node_id: int):
  return db.query(Classificator).filter(Classificator.id == node_id).first()

def create_category(db: Session, name: str, node_type: str, parent_id=None):
  siblings_count = db.query(Classificator).filter(Classificator.parent_id == parent_id).count() # посчитать сколько уже есть детей у этого родителя
  new_node = Classificator(name=name, node_type=node_type, parent_id=parent_id, sort_order=siblings_count + 1)
  db.add(new_node)
  db.commit()        
  db.refresh(new_node)  
  return new_node

def get_descendants(db: Session, node_id: int):
    sql = text("""
        WITH RECURSIVE descendants AS (
            SELECT id, name, node_type, parent_id 
            FROM классификатор WHERE id = :node_id
            UNION ALL
            SELECT c.id, c.name, c.node_type, c.parent_id
            FROM классификатор c
            JOIN descendants d ON c.parent_id = d.id
        )
        SELECT * FROM descendants WHERE id != :node_id
    """)
    result = db.execute(sql, {"node_id": node_id})
    return [dict(row._mapping) for row in result]

def check_cycle(db: Session, node_id: int, new_parent_id: int):
    descendants = get_descendants(db, node_id)
    return new_parent_id in [d['id'] for d in descendants]

def move_category(db: Session, node_id: int, new_parent_id: int):
  if check_cycle(db, node_id, new_parent_id):
    return {"error": "Нельзя переместить узел внутрь его потомка!"} 
  category = db.query(Classificator).filter(Classificator.id == node_id).first()
  
  if category:
    category.parent_id = new_parent_id
    db.commit()
    db.refresh(category)
    return category
  return None

def delete_category(db: Session, node_id: int):
  # проверить есть ли дети
  children_count = db.query(Classificator).filter(
      Classificator.parent_id == node_id
  ).count()
  if children_count > 0:
      return {"error": "Нельзя удалить узел у которого есть потомки"}
  category = db.query(Classificator).filter(Classificator.id == node_id).first()
  if not category:
    return None
  db.delete(category)
  db.commit()
  return category

def get_ancestors(db: Session, node_id: int):
    sql = text("""
        WITH RECURSIVE ancestors AS (
            -- базовый случай: берём сам узел
            SELECT id, name, node_type, parent_id 
            FROM классификатор WHERE id = :node_id
            UNION ALL
            -- рекурсивный случай: идём вверх
            SELECT c.id, c.name, c.node_type, c.parent_id
            FROM классификатор c
            JOIN ancestors a ON c.id = a.parent_id
        )
        SELECT * FROM ancestors WHERE id != :node_id
    """)
    result = db.execute(sql, {"node_id": node_id})
    return [dict(row._mapping) for row in result]

def get_terminals(db: Session, node_id: int):
    sql = text("""
        WITH RECURSIVE descendants AS (
            SELECT id, name, node_type, parent_id 
            FROM классификатор WHERE id = :node_id
            UNION ALL
            SELECT c.id, c.name, c.node_type, c.parent_id
            FROM классификатор c
            JOIN descendants d ON c.parent_id = d.id
        )
        SELECT * FROM descendants d
        WHERE NOT EXISTS (SELECT 1 FROM классификатор c WHERE c.parent_id = d.id)
    """)
    result = db.execute(sql, {"node_id": node_id})
    return [dict(row._mapping) for row in result]

def check_all_cycles(db: Session):
    all_nodes = db.query(Classificator).all()
    cycles = []

    for node in all_nodes:
      ancestors = get_ancestors(db, node.id)
      anacestors_ids = [a['id'] for a in ancestors]

      if node.id in anacestors_ids:
        cycles.append(node.id)
    return cycles

def reorder_children(db: Session, parent_id: int, order_ids: list):
  children = db.query(Classificator).filter(Classificator.parent_id == parent_id).all()
  children_ids = [c.id for c in children]

  for index, node_id in enumerate(order_ids, start=1):
    if node_id not in children_ids:
      return {"error": "Один из указанных узлов не является ребёнком данного родителя!"}
    node = db.query(Classificator).filter(Classificator.id == node_id).first()
    if node:
      node.sort_order = index

  db.commit()
  return children

def set_unit(db: Session, node_id: int, unit: str):
   node = db.query(Classificator).filter(Classificator.id == node_id).first()
   if not node:
     return None
   node.meshering_unit = unit
   db.commit()
   return node