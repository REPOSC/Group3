from django.http import JsonResponse
from backend import models


def get_process(request):
    username = request.POST.get('username')
    booknumber = request.POST.get('booknumber')
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=int(booknumber))
    bookprocess = 0
    try:
        user_process = models.User_process.objects.get(
            user_number=user,
            book_number=book)
        bookprocess = user_process.process
    except:
        pass
    return JsonResponse({'bookprocess': bookprocess})
