from pydantic import BaseModel, EmailStr
from typing import List 
from ninja import Schema, ModelSchema
from core.models import Enrollment
from rest_framework import serializers
from .models import Certificate


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


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'user', 'course', 'issued_at']
        depth = 1  # To include related course and user details
