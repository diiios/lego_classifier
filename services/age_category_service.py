from sqlalchemy.orm import Session
from models.age_category import AgeCategory
from models.set import Set

def get_all_ages(db: Session):
  return db.query(AgeCategory).all()

def get_age(db: Session, age_id: int):
  return db.query(AgeCategory).filter(AgeCategory.id == age_id).first()

def create_age(db: Session, name: str, min_age: int, max_age: int):
  new_age = AgeCategory(name=name, min_age=min_age, max_age=max_age)
  db.add(new_age)
  db.commit()
  db.refresh(new_age)
  return new_age

def delete_age(db: Session, age_id):
    # проверяем, что нет наборов этой категории
    parts_count = db.query(Set).filter(Set.id_year_category == age_id).count()
    if parts_count > 0:
       return {"нельзя удалить возрастную категорию, если есть набор с ней"}
    age_delete = db.query(AgeCategory).filter(AgeCategory.id == age_id).first()
    if not age_delete:
        return None
    db.delete(age_delete)
    db.commit()
    return age_delete
