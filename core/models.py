from django.db import models
from django.contrib.auth.models import User


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)

class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)
