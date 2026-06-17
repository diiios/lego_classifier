from fastapi import FastAPI
from database import Base, engine
import models
from routers import classificator
from routers import seed
from routers import theme_router
from routers import set_router
from routers import part_router
from routers import type_part_router
from routers import figures_router
from routers import age_category_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

#  роутеры
app.include_router(classificator.router)
app.include_router(seed.router)
app.include_router(theme_router.router)
app.include_router(set_router.router)
app.include_router(part_router.router)
app.include_router(type_part_router.router)
app.include_router(figures_router.router)
app.include_router(age_category_router.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}