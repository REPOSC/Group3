from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from backend import models


def auth_student(request):
    number = request.POST.get('id', '')
    user_pwd = request.POST.get('password', '')
    user = authenticate(username=number, password=user_pwd, is_manager=False)
    if user is None:
        return JsonResponse({'status': 'error'})
    else:
        login(request, user)
        last_levels = models.User_info.objects.filter(username=number)
        last_level = last_levels[0].lasttime_level
        return JsonResponse({'status': 'right', 'last_level': last_level})


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


def change_user_image(request):
    username = request.POST.get('username')
    picture = request.FILES.get('image')
    user = models.User_info.objects.get(username=username)
    user.image = picture
    user.save()
    return JsonResponse({'success': 'true'})


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


def get_user_image(request):
    username = request.GET.get('username')
    user = models.User_info.objects.get(username=username)
    try:
        return HttpResponse(user.image)
    except:
        return HttpResponse('None')


def get_user_nickname(request):
    username = request.POST.get('username')
    user = models.User_info.objects.get(username=username)
    return JsonResponse({'nickname': user.nickname})


def change_user_nickname(request):
    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    user = models.User_info.objects.get(username=username)
    user.nickname = nickname
    user.save()
    return JsonResponse({'success': True})


def change_user_password(request):
    username = request.POST.get('username')
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    user = authenticate(username=username, password=old_password)
    if user is None:
        return JsonResponse({'success': 'false'})
    else:
        user.set_password(new_password)
        user.save()
        return JsonResponse({'success': 'true'})


def show_level(request):
    number = request.POST.get('id', '')
    levels = models.User_level.objects.filter(number=number)
    level_list = []
    for onelevel in levels:
        level_list.append(onelevel.level)
    return JsonResponse({"levels": level_list})


def change_last_level(request):
    number = request.POST.get('id', '')
    new_last_level = request.POST.get('newlevel', '')
    try:
        user = models.User_info.objects.get(username=number)
        user.lasttime_level = new_last_level
        user.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def log_out(request):
    logout(request)
    return JsonResponse({'success': 'true'})
