from django.contrib import admin
from django import forms
from django.db import transaction, IntegrityError
import logging

from .models import Institution, Course, Topic, Enrollment, Certificate, CustomUser

logger = logging.getLogger(__name__)

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'

class InstitutionAdmin(admin.ModelAdmin):
    form = InstitutionForm
    list_display = ('name', 'description')
    search_fields = ('name',)
    
    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                logger.debug(f"Saving Institution: {obj}")
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            logger.error(f"IntegrityError while saving institution: {e}")
            logger.debug(f"Request data: {request.POST}")
            logger.debug(f"Form errors: {form.errors}")
            raise e
        
admin.site.register(Institution, InstitutionAdmin)
# Registering other models similarly with enhanced logging
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'institution', 'public')
    search_fields = ('title', 'institution__name')

    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            logger.error(f"IntegrityError while saving course: {e}")
            logger.debug(f"Request data: {request.POST}")
            logger.debug(f"Form errors: {form.errors}")
            raise e

admin.site.register(Course, CourseAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')

    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            logger.error(f"IntegrityError while saving topic: {e}")
            logger.debug(f"Request data: {request.POST}")
            logger.debug(f"Form errors: {form.errors}")
            raise e

admin.site.register(Topic, TopicAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user__username', 'course__title')

    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            logger.error(f"IntegrityError while saving enrollment: {e}")
            logger.debug(f"Request data: {request.POST}")
            logger.debug(f"Form errors: {form.errors}")
            raise e

admin.site.register(Enrollment, EnrollmentAdmin)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'issued_at')
    search_fields = ('user__username', 'course__title')

    def save_model(self, request, obj, form, change):
        try:
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            logger.error(f"IntegrityError while saving certificate: {e}")
            logger.debug(f"Request data: {request.POST}")
            logger.debug(f"Form errors: {form.errors}")
            raise e

admin.site.register(Certificate, CertificateAdmin)

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
