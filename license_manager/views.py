from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from datetime import datetime
from .models import UserActivation
import json
from license_manager.use_cases import app_version_usecase
from django.utils import timezone


@csrf_exempt
@require_POST
def check_license_key(request):
    data = json.loads(request.body)
    license_key = data.get('licenseKey', None)
    device_id = data.get('deviceId', None)
    app_version = data.get('version', None)


    if app_version_usecase.is_force_to_update(app_version):
        return JsonResponse({'code': 110, 'message': 'به روز رسانی اجباری!'}, status=200)

    if not license_key:
        return JsonResponse({'error': 'License key not provided'}, status=400)

    try:
        user_activation = UserActivation.objects.get(license_key=license_key)
    except UserActivation.DoesNotExist:
        return JsonResponse({'code': 111, 'message': 'لایسنس وجود ندارد!'}, status=200)

    if user_activation.expiration_date < timezone.now():
        return JsonResponse({'code': 112, 'message': 'لایسنس منقضی شده است!'}, status=200)

    if user_activation.device_id and user_activation.device_id != device_id:
        return JsonResponse({'code': 113, 'message': 'لایسنس به دستگاه دیگری تعلق دارد!'}, status=200)

    if not user_activation.device_id:
        user_activation.device_id = device_id
        user_activation.save()

    if app_version_usecase.is_update_available(app_version):
        return JsonResponse({'code': 101, 'message': 'به روز رسانی!'}, status=200)  # fix message

    return JsonResponse({'code': 100, 'message': user_activation.phone_number + ' عزیز به اپلیکیشن آسا خوش آمدید!'}, status=200)
