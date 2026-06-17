from pydantic import BaseModel
from typing import Optional

class SetBase(BaseModel):
  name: str
  parent_id: int
  number_of_set: str
  price: float
  year_of_issue: int
  count_of_details: int
  description: Optional[str] = None
  id_theme: Optional[int] = None
  id_age_category: Optional[int] = None

class SetCreate(SetBase):
  pass

class SetResponse(SetBase):
  id: int

  class Config:
    from_attributes = True


class Details_in_setBase(BaseModel):
  count_detail: int
  id_detail: Optional[int] = None
  id_set: Optional[int] = None

class Details_in_setCreate(Details_in_setBase):
  pass

class Details_in_setResponse(Details_in_setBase):
  id: int

  class Config:
    from_attributes = True