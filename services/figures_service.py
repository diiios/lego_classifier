from sqlalchemy.orm import Session
from models.figure import Figure
from services.classificator import create_category
from models.classificator import Classificator

def get_all_figures(db: Session):
  return db.query(Figure).all()

def get_figure(db: Session, set_id: int):
  return db.query(Figure).filter(Figure.id == set_id).first()

def create_figure(db, name, series, code):
  figures_node = db.query(Classificator).filter(
      Classificator.name == "Мини-фигурки"
  ).first()
  node = create_category(db, name, "терминальный", figures_node.id)
  new_figure = Figure(
     name=name, 
     series=series,
     code=code,
     id_classificator=node.id
  )
  db.add(new_figure)
  db.commit()
  db.refresh(new_figure)
  return new_figure

def delete_figure(db: Session, set_id):
    figure_delete = db.query(Figure).filter(Figure.id == set_id).first()
    if not figure_delete:
        return None
    db.delete(figure_delete)
    db.commit()
    return figure_delete