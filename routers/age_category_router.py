from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.age_category_service as age_category
from database import SessionLocal
from schemas.age_category import AgeCategoryCreate

router = APIRouter(prefix="/age_category", tags=["age_category"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_all_ages(db: Session = Depends(get_db)):
   return age_category.get_all_ages(db)

@router.get("/{age_id}")
def get_age(age_id: int, db: Session = Depends(get_db)):
   return age_category.get_age(db, age_id)

@router.post("/")
def create_age(data: AgeCategoryCreate, db: Session = Depends(get_db)):
    return age_category.create_age(db, data.name, data.min_age, data.max_age)

@router.delete("/{age_id}")
def delete_age(age_id: int, db: Session = Depends(get_db)):
    result = age_category.delete_age(db, age_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return result