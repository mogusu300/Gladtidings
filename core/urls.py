from django.urls import path
from .api import api  # Import the API instance
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('courses/', views.list_courses, name='list_courses'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('enroll/', views.enroll, name='enroll'),
    path('certificates/', views.my_certificates, name='certificates'),
    path('change-password/', views.change_password, name='change_password'),
    path('create-course/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/topics/', views.list_topics, name='list_topics'),
    path('topics/<int:topic_id>/', views.get_topic, name='get_topic'),
    path('courses/<int:course_id>/topics/create/', views.create_topic, name='create_topic'),
    path('topics/<int:topic_id>/update/', views.update_topic, name='update_topic'),
    path('topics/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers, name='teachers'),
]
