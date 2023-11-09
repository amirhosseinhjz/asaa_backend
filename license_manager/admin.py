from django.contrib import admin
from . import models


class UserActivationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'license_key', 'device_id', 'expiration_date')
    search_fields = ('phone_number', 'license_key', 'device_id')
    list_filter = ('expiration_date',)
    readonly_fields = ('license_key',)

admin.site.register(models.UserActivation, UserActivationAdmin)
