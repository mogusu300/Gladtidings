from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True)  # Assuming 'role' is a user role field
    
    def __str__(self):
        return self.username  # Display username as strin

class Institution(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='topics/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='topics/', null=True, blank=True)
    description = models.TextField()
    public = models.BooleanField(default=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True)

class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='topics/', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Certificate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)


CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'