from sqlalchemy.orm import Session
from database import Base
from models.classificator import Classificator
from models.age_category import AgeCategory
from models.set import Set
from models.part import Part
from models.figure import Figure
from models.theme import Theme
from models.part import PartType

def clear_db(db: Session):
  for tabel in reversed(Base.metadata.sorted_tables):
    db.execute(tabel.delete())
  db.commit()

def seed_db(db: Session):
  clear_db(db)
  root = Classificator(name="Изделия LEGO", node_type="промежуточный")
  db.add(root)
  db.flush() # получение id без commit


  theme_wars = Theme(
    name="Star Wars", 
    description="Звёздные войны",
  )
  db.add(theme_wars)
  
  theme_city = Theme(
    name="Lego City", 
    description="Город",
  )
  db.add(theme_city)
  
  theme_arch = Theme(
    name="Architecture", 
    description="Архитектура",
  )
  db.add(theme_arch)
  db.flush()


  sets_node = Classificator(name="Наборы", node_type="промежуточный", parent_id=root.id) # узел наборов
  db.add(sets_node)
  detailes_node = Classificator(name="Детали", node_type="промежуточный", parent_id=root.id) # узел деталей
  db.add(detailes_node)
  figures_node = Classificator(name="Мини-фигурки", node_type="промежуточный", parent_id=root.id) # узел мини-фигурок
  db.add(figures_node)
  db.flush()

  age_1 = AgeCategory(name="1-7", min_age=1, max_age=7)
  db.add(age_1)
  age_2 = AgeCategory(name="8-10", min_age=8, max_age=10)
  db.add(age_2)
  age_3 = AgeCategory(name="11-15", min_age=11, max_age=15)
  db.add(age_3)
  db.flush()

  set_star_node = Classificator(name="Звезда смерти", node_type="терминальный", parent_id=sets_node.id) # узел наборов
  db.add(set_star_node)
  db.flush()

  set_star = Set(
    name = "Звезда Смерти",
    number_of_set = 95594,
    price = 500.5,
    year_of_issue = 2004,
    count_of_details = 5000,
    description = "набор про космический корабль",
    id_classificator=set_star_node.id,
    id_theme=theme_wars.id,
    id_year_category=age_3.id
  )
  db.add(set_star)


  set_police_node = Classificator(name="Отдел полиции", node_type="терминальный", parent_id=sets_node.id) # узел наборов
  db.add(set_police_node)
  db.flush()

  set_police = Set(
    name = "Отдел полиции",
    number_of_set = 48859,
    price = 490.5,
    year_of_issue = 2006,
    count_of_details = 4000,
    description = "набор с отделом полиции",
    id_classificator=set_police_node.id,
    id_theme=theme_city.id,
    id_year_category=age_2.id
  )
  db.add(set_police)


  # узел типа детали в дереве
  plate_type_node = Classificator(name="Плиты", node_type="промежуточный", parent_id=detailes_node.id)
  db.add(plate_type_node)
  brick_type_node = Classificator(name="Кирпичи", node_type="промежуточный", parent_id=detailes_node.id)
  db.add(brick_type_node)
  db.flush()

  # создаём типы деталей
  plate_type = PartType(name="Плита", id_classificator=plate_type_node.id)
  db.add(plate_type)
  brick_type = PartType(name="Кирпич", id_classificator=brick_type_node.id)
  db.add(brick_type)
  db.flush()


  part_plate_node = Classificator(name="Плита 2х2", node_type="терминальный", parent_id=plate_type_node.id) 
  db.add(part_plate_node)
  db.flush()

  part_plate = Part(
    name = "Плита 2х2",
    color = "Красный",
    code = "FDG454",
    size_width = 22,
    size_length = 22,
    size_height = 11,
    weight = 45,
    id_type = plate_type.id,
    id_classificator = part_plate_node.id
  )
  db.add(part_plate)

  part_block_node = Classificator(name="Кирпич 3х4", node_type="терминальный", parent_id=brick_type_node.id) 
  db.add(part_block_node)
  db.flush()

  part_block = Part(
    name = "Кирпич 3х4",
    color = "Красный",
    code = "FDG454",
    size_width = 33,
    size_length = 44,
    size_height = 11,
    weight = 55,
    id_type = brick_type.id,
    id_classificator = part_block_node.id
  )
  db.add(part_block)

  dart_waider = Figure(
    name = "Дарт Вейдер",
    series = "3344-22",
    code = "EREF443-1",
    id_classificator = figures_node.id
  )
  db.add(dart_waider)

  db.commit()