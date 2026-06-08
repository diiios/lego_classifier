from pydantic import BaseModel
from typing import Optional

class FigureBase(BaseModel):
  name: str
  series: str
  code: str
  id_classificator: int

class FigureCreate(FigureBase):
  pass

class FigureResponse(FigureBase):
  id: int

  class Config:
    from_attributes = True