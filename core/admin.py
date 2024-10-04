from django.contrib import admin
from .models import CustomUser, Institution, Course, Topic, Enrollment, Certificate
from django.contrib.auth.admin import UserAdmin

# CustomUser Admin
class CustomUserAdmin(UserAdmin):
    # Add 'age' and 'role' to the fields displayed in the admin panel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'role')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'role', 'is_staff', 'is_active')

    # Make 'date_joined' and 'last_login' read-only to avoid editing errors
    readonly_fields = ('date_joined', 'last_login')

# Institution Admin
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Course Admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'public')
    search_fields = ('title', 'institution__name')
    list_filter = ('public', 'institution')

# Topic Admin
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')

# Enrollment Admin
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user__username', 'course__title')

# Certificate Admin
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'issued_at')
    search_fields = ('user__username', 'course__title')

# Register models with their respective Admin classes
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Certificate, CertificateAdmin)
