from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.part_service as part_service
from database import SessionLocal
from schemas.part import PartCreate

router = APIRouter(prefix="/part", tags=["part"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_all_parts(db: Session = Depends(get_db)):
   return part_service.get_all_parts(db)

@router.get("/{part_id}")
def get_part(part_id: int, db: Session = Depends(get_db)):
   return part_service.get_part(db, part_id)

@router.post("/")
def create_part(data: PartCreate, db: Session = Depends(get_db)):
    return part_service.create_part(
        db,
        data.name,
        data.color,
        data.code,
        data.size_width,
        data.size_length,
        data.size_height,
        data.weight,
        data.id_type
    )

@router.delete("/{part_id}")
def delete_part(part_id: int, db: Session = Depends(get_db)):
    result = part_service.delete_part(db, part_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Деталь не найдена")
    return result