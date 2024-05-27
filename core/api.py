# core/api.py
from ninja import NinjaAPI, Router
from .models import CustomUser
from .scheme import UserCreateSchema, UserSchema

api = NinjaAPI()

router = Router()

@router.post("/register", response=UserSchema)
def register(request, data: UserCreateSchema):
    user = CustomUser.objects.create_user(
        username=data.username,
        email=data.email,
        password=data.password,
        role=data.role
    )
    return user

api.add_router("/", router)  # Add the router to the API instance
