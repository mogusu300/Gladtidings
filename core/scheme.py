from pydantic import BaseModel, EmailStr
from typing import List 
from typing import Optional
from ninja import Schema, ModelSchema
from .models import Enrollment  # Ensure the correct model is imported
class UserCreateSchema(Schema):
    username: str
    email: EmailStr
    password: str
    role: str  # Adjust based on your role field in the user model

class UserSchema(Schema):
    id: int
    username: str
    email: EmailStr
    role: str  # Adjust based on your role field in the user model


class EnrollmentSchema(ModelSchema):
    class Config:
        model = Enrollment  # Ensure the model is correctly referenced
        model_fields = '__all__'  # Customize fields as needed





