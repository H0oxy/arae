from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authapp.models import KpkUser


class KpkAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2'),
        }),
    )

    list_display = ('login', 'email', 'name', 'surname', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('login', 'name', 'surname', 'email')
    ordering = ('login',)


admin.site.register(KpkUser, KpkAdmin)
