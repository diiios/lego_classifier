from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services.figures_service as figures_service
from database import SessionLocal
from schemas.figure import FigureCreate

router = APIRouter(prefix="/figures", tags=["figures"])

def get_db():
    db = SessionLocal() # открыть сессию
    try:
        yield db # передать сессию в эндпоинт
    finally:
        db.close() # закрыть сессию всегда

@router.get("/")
def get_all_figures(db: Session = Depends(get_db)):
   return figures_service.get_all_figures(db)

@router.get("/{figure_id}")
def get_set(figure_id: int, db: Session = Depends(get_db)):
   return figures_service.get_figure(db, figure_id)

@router.post("/")
def create_figure(data: FigureCreate, db: Session = Depends(get_db)):
    return figures_service.create_figure(
        db,
        data.name,
        data.series,
        data.code,
    )

@router.delete("/{figure_id}")
def delete_figure(figure_id: int, db: Session = Depends(get_db)):
    result = figures_service.delete_figure(db, figure_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Фигурка не найдена")
    return result