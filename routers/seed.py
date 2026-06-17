from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.classificator as services
import services.seed as seed
from database import SessionLocal
from schemas.classificator import ClassificatorCreate

router = APIRouter(prefix="/seed", tags=["seed"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.post("/")
def seed_db(db: Session = Depends(get_db)):
   return seed.seed_db(db)


@router.delete("")
def clear_db(db: Session = Depends(get_db)):
   return seed.clear_db(db)
