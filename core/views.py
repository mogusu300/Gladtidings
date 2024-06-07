from django.shortcuts import render
from .models import models

# Create your views here.

#List topics
def course_topics(request, course_id):
    return render(request, 'course_topics.html', {'course_id': course_id})
