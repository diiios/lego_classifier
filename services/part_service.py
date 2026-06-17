from sqlalchemy.orm import Session
from models.part import Part
from models.part import PartType
from services.classificator import create_category

def get_all_parts(db: Session):
  return db.query(Part).all()

def get_part(db: Session, part_id: int):
  return db.query(Part).filter(Part.id == part_id).first()

def create_part(db, name, color, code, size_width, size_length, size_height, weight, id_type):
  part_type = db.query(PartType).filter(PartType.id == id_type).first()
  node = create_category(db, name, "терминальный", part_type.id_classificator)
  new_part = Part(
     name=name, 
     color=color,
     code=code, 
     size_width=size_width, 
     size_length=size_length, 
     size_height=size_height, 
     weight=weight,
     id_type=id_type,
     id_classificator=node.id
  )
  db.add(new_part)
  db.commit()
  db.refresh(new_part)
  return new_part

def delete_part(db: Session, part_id):
    part_delete = db.query(Part).filter(Part.id == part_id).first()
    if not part_delete:
        return None
    db.delete(part_delete)
    db.commit()
    return part_delete