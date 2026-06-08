from sqlalchemy.orm import Session
from sqlalchemy import text
from models.classificator import Classificator

def get_all_categories(db: Session):
  return db.query(Classificator).all()

def get_category(db: Session, node_id: int):
  return db.query(Classificator).filter(Classificator.id == node_id).first()

def create_category(db: Session, name: str, node_type: str, parent_id=None):
  new_node = Classificator(name=name, node_type=node_type, parent_id=parent_id)
  db.add(new_node)
  db.commit()        
  db.refresh(new_node)  
  return new_node

def move_category(db: Session, node_id: int, new_parent_id: int):
  category = db.query(Classificator).filter(Classificator.id == node_id).first()
  if category:
    category.parent_id = new_parent_id
    db.commit()
    db.refresh(category)
    return category
  return None

def delete_category(db: Session, node_id: int):
  category = db.query(Classificator).filter(Classificator.id == node_id).first()
  if not category:
    return None
  db.delete(category)
  db.commit()
  return category

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

