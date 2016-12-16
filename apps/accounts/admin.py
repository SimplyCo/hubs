from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import CustomUser, UserConfirmToken

# from djcelery import models as celery_models


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'email',
        'is_staff',
        'is_superuser',
        'is_active',
        'email_confirmed'
    )
    list_filter = (
        'is_staff',
        'is_active',
        'is_superuser',
        'email_confirmed',
    )
    fieldsets = (
        ('User data', {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('user_name', 'phone', 'city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'email_confirmed')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    readonly_fields = (
        'date_joined',
        'last_login'
    )
    search_fields = (
        'email',
        'user_name',
    )
    ordering = (
        'email',
    )
    list_display_links = (
        'id',
        'email',
    )
    filter_horizontal = ()


@admin.register(UserConfirmToken)
class UserConfirmTokenAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'token',
        'uid',
        'reason',
        'used',
        'created',
    )
    readonly_fields = (
        'created',
    )

    list_filter = (
        'reason',
        'used',
    )


# admin.site.unregister(celery_models.CrontabSchedule)
# admin.site.unregister(celery_models.PeriodicTask)
# admin.site.unregister(celery_models.WorkerState)
# admin.site.unregister(celery_models.IntervalSchedule)
# admin.site.unregister(celery_models.TaskState)
admin.site.unregister(Group)
