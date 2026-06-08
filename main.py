from fastapi import FastAPI
from database import Base, engine
import models
from routers import classificator

app = FastAPI()

Base.metadata.create_all(bind=engine)

#  роутер для классификатора
app.include_router(classificator.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}