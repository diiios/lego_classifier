from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.theme_service as theme
from database import SessionLocal
from schemas.theme import ThemeCreate

router = APIRouter(prefix="/theme", tags=["theme"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_all_themes(db: Session = Depends(get_db)):
   return theme.get_all_themes(db)

@router.get("/{theme_id}")
def get_theme(theme_id: int, db: Session = Depends(get_db)):
   return theme.get_theme(db, theme_id)

@router.post("/")
def create_theme(data: ThemeCreate, db: Session = Depends(get_db)):
    return theme.create_theme(db, data.name, data.description)

@router.delete("/{theme_id}")
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    result = theme.delete_theme(db, theme_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Тематика не найдена")
    return result