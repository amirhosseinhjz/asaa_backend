from django.db import models
import uuid
from django.core.validators import RegexValidator
from .utils import normalize_phone_number


class UserActivation(models.Model):
    phone_regex = RegexValidator(regex=r'^(\+98|00|0)?9\d{9}$', message="شماره تلفن نامعتبر")

    name = models.CharField(max_length=200, blank=True, verbose_name='نام')
    phone_number = models.CharField(max_length=200, blank=False, verbose_name='تلفن')
    license_key = models.CharField(max_length=200, unique=True, blank=True, verbose_name='کلید لایسنس')
    device_id = models.CharField(max_length=200, blank=True)
    expiration_date = models.DateTimeField(verbose_name='تاریخ انقضا')

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.license_key:
            self.license_key = str(uuid.uuid4())[:8]
        if self.phone_number:
            self.phone_number = normalize_phone_number(str(self.phone_number))

        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.name) + ' ' + str(self.phone_number)

    class Meta:
        verbose_name_plural = "شماره سریال ها"
        verbose_name = "شماره سریال"
