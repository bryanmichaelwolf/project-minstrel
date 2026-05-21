from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        'id',
        'email',
        'username',
        'is_staff',
        'is_active',
    )

    ordering = ('email',)

    fieldsets = UserAdmin.fieldsets + (
        (
            'Custom Fields',
            {
                'fields': ()
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Custom Fields',
            {
                'fields': ()
            },
        ),
    )
    