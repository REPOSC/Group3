from django.http import JsonResponse
from backend import models


def all_daka(request):
    dakas = models.User_punch.objects.filter(is_punched=True)
    booknumbers = []
    usernumbers = []
    comments = []
    riqis = []
    likenums = []
    for i in dakas:
        booknumbers.append(i.book_number)
        usernumbers.append(i.user_number)
        punch = models.User_punch.objects.filter(user_number=i.user_number, book_number=i.book_number)
        comments.append(punch.punch_text)
        riqis.append(i.time)
        likenums.append(i.like_number)
    return JsonResponse({
        'booknums': booknumbers,
        'usernums': usernumbers,
        'likenums':likenums,
        'riqis':riqis,
        'contents':comments
    })
