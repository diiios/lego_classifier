from fastapi import APIRouter, Depends
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