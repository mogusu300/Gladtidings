from pydantic import BaseModel, EmailStr
from typing import List 
from ninja import Schema, ModelSchema
from core.models import Enrollment


class EnrollmentSchema(ModelSchema):
    class Config:
        model = Enrollment
        include = ["id", "user", "course", "issued_at"]

class UserSchema(BaseModel):
  id: int
  username: str
  email: str
  role: str

  class Config:
    orm_mode: True
