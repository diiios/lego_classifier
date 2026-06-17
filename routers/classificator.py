from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.classificator as services
from database import SessionLocal
from schemas.classificator import ClassificatorCreate

router = APIRouter(prefix="/categories", tags=["categories"])
# prefix="/categories" — это общее начало URL для всех эндпоинтов в этом роутере.
# tags=["categories"] — это просто группировка в Swagger UI. Все эндпоинты с этим тегом будут в одной секции. 
def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return services.get_all_categories(db)

@router.get("/check-cycle")
def check_all_cycles(db: Session = Depends(get_db)):
  return services.check_all_cycles(db)

@router.get("/{node_id}")
def get_category(node_id: int, db: Session = Depends(get_db)):
  return services.get_category(db, node_id)

@router.post("/")
def create_category(category: ClassificatorCreate, db: Session = Depends(get_db)):
  return services.create_category(db, category.name, category.node_type, category.parent_id)

@router.put("/{node_id}/move")
def move_category(node_id: int, new_parent_id: int, db: Session = Depends(get_db)):
  return services.move_category(db, node_id, new_parent_id)

@router.delete("/{node_id}")
def delete_category(node_id: int, db: Session = Depends(get_db)):
  return services.delete_category(db, node_id)

@router.get("/{node_id}/descendants")
def get_descendants(node_id: int, db: Session = Depends(get_db)):
  return services.get_descendants(db, node_id)

@router.get("/{node_id}/ancestors")
def get_ancestors(node_id: int, db: Session = Depends(get_db)):
  return services.get_ancestors(db, node_id)

@router.get("/{node_id}/get-terminals")
def get_terminals(node_id: int, db: Session = Depends(get_db)):
  return services.get_terminals(db, node_id)

from schemas.classificator import ReorderChildren

@router.put("/{node_id}/reorder-children")
def reorder_children(parent_id: int, order_list: ReorderChildren, db: Session = Depends(get_db)):
   return services.reorder_children(db, parent_id, order_list.order_ids)

from schemas.classificator import SetUnit

@router.put("/{node_id}/set-unit")
def set_unit(node_id: int, data_unit: SetUnit, db: Session = Depends(get_db)):
   return services.set_unit(db, node_id, data_unit.unit)
