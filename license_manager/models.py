from django.db import models
import uuid


class UserActivation(models.Model):
    phone_number = models.CharField(max_length=200)
    license_key = models.CharField(max_length=200, unique=True, blank=True)
    device_id = models.CharField(max_length=200, blank=True)
    expiration_date = models.DateTimeField()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.license_key:
            self.license_key = str(uuid.uuid4())[:8]

        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.phone_number
