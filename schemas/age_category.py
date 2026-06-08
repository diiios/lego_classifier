from pydantic import BaseModel
from typing import Optional

class AgeCategoryBase(BaseModel):
  name: str
  min_age: int
  max_age: int

class AgeCategoryCreate(AgeCategoryBase):
  pass

class AgeCategoryResponse(AgeCategoryBase):
  id: int

  class Config:
    from_attributes = True