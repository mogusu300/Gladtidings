from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError




from django.db import models
from django.core.exceptions import ValidationError

class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='institutions/', null=True, blank=True)  # Add image field

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, blank=True)  # Link to institution

    def __str__(self):
        return self.username
    
    
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, blank=True, db_constraint=False)
    image = models.ImageField(upload_to='courses/', null=True, blank=True)  # Add image field

    def clean(self):
        if self.institution and not Institution.objects.filter(id=self.institution_id).exists():
            raise ValidationError(f"Institution with id {self.institution_id} does not exist.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='topics/', null=True, blank=True)  # Add image field


class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Certificate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)


CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'