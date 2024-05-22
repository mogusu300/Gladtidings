from ninja import NinjaApi, Router
from django.contri.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .scheme import (UserCreateSchema, UserSchema)

api=NinjaAPI()

router = Router()

@router.post("/register", reponse=UserSchema)
def register (request, data: UserCreateSchema):
  user = CustomUser.objects.create_user(
    username=data.username,
    email=data.email,
    password=data.password,
    role=data.role
  )
  return user 
