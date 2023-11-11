from django.contrib import admin
from . import models


@admin.register(models.UserActivation)
class UserActivationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'license_key', 'device_id', 'expiration_date')
    search_fields = ('name', 'phone_number')
    list_filter = ('expiration_date',)
    readonly_fields = ('license_key', 'device_id')
    list_display_links = ('name', 'phone_number', 'license_key', 'device_id', 'expiration_date')
