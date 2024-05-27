from django.urls import path
from .api import api  # Import the API instance

urlpatterns = [
    path("api/", api.urls),  # Include the URLs defined by the API instance
]