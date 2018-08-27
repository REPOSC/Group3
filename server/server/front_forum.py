from django.http import JsonResponse
from django.http import HttpResponse
from backend import models


def get_punch_info(request):
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    punch_require = models.Book_punch_requirement.objects.filter(
        number=booknumber)
    punch_info = models.User_punch.objects.filter(
        user_number=username,
        book_number=booknumber)
    if punch_require:
        requirement = punch_require[0].requirement
        if punch_info:
            is_punched = punch_info[0].is_punched
            return JsonResponse({'is_punched': is_punched, 'requirement': requirement})
        else:
            return JsonResponse({'is_punched': False, 'requirement': requirement})
    else:
        return JsonResponse({'is_punched': 'cannot', 'requirement': 'No expanding yet!'})


def upload_homework(request):
    fileList = request.FILES.getlist('files', '')
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    textcontent = request.POST.get('content', '')
    punch_info = models.User_punch.objects.filter(
        user_number=username,
        book_number=booknumber)
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=booknumber)
    contentnumber = models.Punch_content.objects.filter(
        user_number=user,
        book_number=book
    ).count()
    try:
        for i in range(len(fileList)):
            content = models.Punch_content.objects.create(
                user_number=user,
                book_number=book,
                content_number=contentnumber,
                content=fileList[i]
            )
            content.save()
            contentnumber += 1
        user.is_punched = True
        user.save()
        punch_info.punch_text = content
        punch_info.save()
        return JsonResponse({'status': 'true', 'totalfile': contentnumber})
    except:
        return JsonResponse({'status': 'error'})
