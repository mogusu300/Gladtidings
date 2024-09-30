from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Institution


class CustomUserAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Additional info'), {'fields': ('role',)}),  # Custom field for role
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Additional info'), {'fields': ('role',)}),  # Custom field for role
    )
    # Fields to display in the user list view
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'role')
    # Fields to enable search functionality in the admin
    search_fields = ('username', 'first_name', 'last_name', 'email', 'role')
    # Default ordering of the user list
    ordering = ('username',)


# Register the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Institution)
