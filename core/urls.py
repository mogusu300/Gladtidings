from django.urls import path
from .api import api  # Import the API instance
from . import views

urlpatterns = [
    path("api/", api.urls), # Include the URLs defined by the API instance
    path('courses/<int:course_id>/topics/', views.course_topics, name='course_topics'),#List topics 
]