from sqlalchemy.orm import Session
from services.classificator import create_category
from models.part import PartType
from models.part import Part

def get_all_types(db: Session):
  return db.query(PartType).all()

def get_type(db: Session, type_id: int):
  return db.query(PartType).filter(PartType.id == type_id).first()

def create_type(db, name, parent_id):
  node = create_category(db, name, "промежуточный", parent_id)
  new_type = PartType(
     name=name, 
     id_classificator=node.id,
  )
  db.add(new_type)
  db.commit()
  db.refresh(new_type)
  return new_type

def delete_type(db: Session, type_id):
    # проверить есть ли дети
    children_count = db.query(Part).filter(
        Part.id_type == type_id
    ).count()
    if children_count > 0:
        return {"error": "Нельзя удалить тип — есть детали этого типа"}
    type_delete = db.query(PartType).filter(PartType.id == type_id).first()
    if not type_delete:
        return None
    db.delete(type_delete)
    db.commit()
    return type_delete
