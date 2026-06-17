from sqlalchemy.orm import Session
from models.set import Set
from services.classificator import create_category

def get_all_sets(db: Session):
  return db.query(Set).all()

def get_set(db: Session, set_id: int):
  return db.query(Set).filter(Set.id == set_id).first()

def create_set(db, name, parent_id, number_of_set, price, description, year_of_issue, count_of_details, id_theme, id_year_category):
  node = create_category(db, name, "терминальный", parent_id)
  new_set = Set(
     name=name, 
     number_of_set=number_of_set,
     price=price, 
     description=description,
     year_of_issue=year_of_issue,
     count_of_details=count_of_details, 
     id_classificator=node.id,
     id_theme=id_theme,
     id_year_category=id_year_category
  )
  db.add(new_set)
  db.commit()
  db.refresh(new_set)
  return new_set

def delete_set(db: Session, set_id):
    set_delete = db.query(Set).filter(Set.id == set_id).first()
    if not set_delete:
        return None
    db.delete(set_delete)
    db.commit()
    return set_delete