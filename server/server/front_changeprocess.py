from django.http import HttpResponse
from backend import models
from django.http import JsonResponse


def change_process(request):
    username = request.POST.get('username')
    booknumber = request.POST.get('booknumber')
    process = request.POST.get('process')
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=int(booknumber))
    try:
        user_process = models.User_process.objects.get(
            user_number=user, book_number=book)
        user_process.process = float(process)
        user_process.save()
    except:
        user_process = models.User_process.objects.create(
            user_number=user, book_number=book, process=float(process))
        user_process.save()
    return JsonResponse({'success': True})
