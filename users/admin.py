from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from . import models
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'id', 'email', 'name', 'is_staff', 'is_active', 'role',
    )
    list_filter = (
        'is_staff', 'is_active', 'role',
    )
    fieldsets = (
        (
            None,
            {'fields': ('name', )},
        ),
        (None, {'fields': ('email', 'password')}),
        (None, {'fields': ('created_at', 'updated_at', 'last_login')}),
        (
            'Permissions',
            {
                'fields': (
                    'role',
                    'is_superuser',
                    'is_staff',
                    'is_active',
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'email',
                    'password1',
                    'password2',
                    'role',
                    'is_superuser',
                    'is_staff',
                    'is_active',
                )
            },
        ),
    )
    readonly_fields = ('created_at', 'updated_at', 'last_login')
    search_fields = ('email', 'name')
    ordering = ('created_at', )


@admin.register(models.CompanyUser)
class CompanyUserAdmin(CustomUserAdmin):
    pass


@admin.register(models.CustomerUser)
class CustomerUserAdmin(CustomUserAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
