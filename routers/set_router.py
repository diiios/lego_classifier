from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.set_service as set_service
from database import SessionLocal
from schemas.set import SetCreate

router = APIRouter(prefix="/set", tags=["set"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_all_sets(db: Session = Depends(get_db)):
   return set_service.get_all_sets(db)

@router.get("/{set_id}")
def get_set(set_id: int, db: Session = Depends(get_db)):
   return set_service.get_set(db, set_id)

@router.post("/")
def create_set(data: SetCreate, db: Session = Depends(get_db)):
    return set_service.create_set(
        db,
        data.name,
        data.parent_id,
        data.number_of_set,
        data.price,
        data.description,
        data.year_of_issue,
        data.count_of_details,
        data.id_theme,
        data.id_age_category
    )

@router.delete("/{set_id}")
def delete_set(set_id: int, db: Session = Depends(get_db)):
    result = set_service.delete_set(db, set_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Набор не найден")
    return result