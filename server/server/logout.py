from django.http import JsonResponse
from django.contrib.auth import logout


def log_out(request):
    logout(request)
    return JsonResponse({'success': 'true'})
