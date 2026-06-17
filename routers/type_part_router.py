from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.type_part_service as type_part_service
from database import SessionLocal

router = APIRouter(prefix="/type_part", tags=["type_part"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_all_types(db: Session = Depends(get_db)):
   return type_part_service.get_all_types(db)

@router.get("/{type_id}")
def get_type(type_id: int, db: Session = Depends(get_db)):
   return type_part_service.get_type(db, type_id)

@router.post("/")
def create_type(name: str, parent_id: int, db: Session = Depends(get_db)):
    return type_part_service.create_type(
        db, 
        name=name,
        parent_id=parent_id
    )

@router.delete("/{type_id}")
def delete_type(type_id: int, db: Session = Depends(get_db)):
    result = type_part_service.delete_type(db, type_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Тип детали не найден")
    return result