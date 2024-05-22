from pydynatic import Basemodel, EmailStr
from typing import List 

class UserCreateSchema(BaseModel):
  username: str
  email: EmailStr
  password: str
  role: str

class UserSchema(BaseModel):
  id: int
  username: str
  email: str
  role: str

  class Config:
    orm_mode: True
