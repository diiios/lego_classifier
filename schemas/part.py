from pydantic import BaseModel
from typing import Optional

class PartBase(BaseModel):
  name: str
  color: Optional[str] = None
  code: str
  size_width: Optional[int] = None
  size_length: Optional[int] = None
  size_height: Optional[int] = None
  weight: Optional[int] = None
  id_type: Optional[int] = None

class PartCreate(PartBase):
  pass

class PartResponse(PartBase):
  id: int

  class Config:
    from_attributes = True