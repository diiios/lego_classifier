from sqlalchemy.orm import Session
from models.theme import Theme
from models.set import Set

def get_all_themes(db: Session):
  return db.query(Theme).all()

def get_theme(db: Session, theme_id: int):
  return db.query(Theme).filter(Theme.id == theme_id).first()

def create_theme(db: Session, name: str, description: str):
  new_theme = Theme(name=name, description=description)
  db.add(new_theme)
  db.commit()
  db.refresh(new_theme)
  return new_theme

def delete_theme(db: Session, theme_id):
    # проверяем, что нет наборов этой тематики
    parts_count = db.query(Set).filter(Set.id_theme == theme_id).count()
    if parts_count > 0:
       return {"нельзя удалить тематику, если есть набор с этой тематикой"}
    theme_delete = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme_delete:
        return None
    db.delete(theme_delete)
    db.commit()
    return theme_delete
