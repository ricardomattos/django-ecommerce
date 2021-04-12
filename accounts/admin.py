from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from accounts.forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

    list_display = ["username", "name", "email", "is_active", "is_staff"]

    # form to register User into django admin
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            "fields": ("username", "email", "password1", "password2")
        }),
    )

    # form to manage all info. about user (groups, permissions)
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        ('Permissões', {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        })
    )


admin.site.register(User, UserAdmin)
