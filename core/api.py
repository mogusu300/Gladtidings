# core/api.py
from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404
from .models import Course, Topic
from .schema import TopicSchema

api = NinjaAPI()

@api.get("/courses/{course_id}/topics", response=List[TopicSchema])
def list_topics(request, course_id: int):
    course = get_object_or_404(Course, id=course_id)
    topics = Topic.objects.filter(course=course)
    return topics
