from pydantic import BaseModel
from typing import Optional

class ClassificatorBase(BaseModel):
  name: str
  node_type: str
  meshering_unit: Optional[str] = None
  parent_id: Optional[int] = None


class ClassificatorCreate(ClassificatorBase):
  pass

class ClassificatorResponse(ClassificatorBase):
  id: int

  class Config:
    from_attributes = True