from pydantic import BaseModel
from typing import Optional

class ThemeBase(BaseModel):
  name: str
  description: Optional[str] = None

class ThemeCreate(ThemeBase):
  pass

class ThemeResponse(ThemeBase):
  id: int

  class Config:
    from_attributes = True