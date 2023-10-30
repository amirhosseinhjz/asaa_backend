from django.urls import path
from .views import check_license_key


urlpatterns = [
    path('validate/', check_license_key),
]
