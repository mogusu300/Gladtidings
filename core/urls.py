from django.urls import path
from ninja import NinjaAPI
from .api import router

api = NinjaAPI()

urlpatterns = [
    path('', router.urls),  # Include the URLs defined in your app's API router
]