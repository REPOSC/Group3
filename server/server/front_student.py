"""This module include some functions about the students of miniprogram."""
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from backend import models


def auth_student(request):
    ##
    # Varify the login of the student.
    # @param number id of the student
    # @param user_pwd password of the student
    # @retval status whether successfully login or not
    # @retval last_level the last level the user reading
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
    ##
    # Change the process of one book.
    # @param username id of the user
    # @param booknumber id of the book
    # @param process new process of the book
    # @param user user information in database
    # @param book book information in database
    # @retval success whether successfully change the process or not
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
    ##
    # Change the profile image of the user.
    # @param username id of the user
    # @param picture new profile of the user
    # @param user user information in database
    # @retval success whether successfully change the profile or not
    username = request.POST.get('username')
    picture = request.FILES.get('image')
    user = models.User_info.objects.get(username=username)
    user.image = picture
    user.save()
    return JsonResponse({'success': 'true'})


def get_process(request):
    ##
    # Get the process of one book.
    # @param username id of the user
    # @param booknumber id of the book
    # @param bookprocess the process of the book
    # @param user user information in database
    # @param book book information in database
    # @retval bookprocess
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
    ##
    # Get the profile of the user.
    # @param username id of the user
    # @param user user information in database
    # @retval user.image
    username = request.GET.get('username')
    user = models.User_info.objects.get(username=username)
    try:
        return HttpResponse(user.image)
    except:
        return HttpResponse('None')


def get_user_nickname(request):
    ##
    # Get the nickname of the user.
    # @param username id of the user
    # @param user user information in database
    # @retval nickname the nickname of the user
    username = request.POST.get('username')
    user = models.User_info.objects.get(username=username)
    return JsonResponse({'nickname': user.nickname})


def change_user_nickname(request):
    ##
    # Change the nickname of the user.
    # @param username id of the user
    # @param nickname new nickname of the user
    # @param user user information in database
    # @retval success whether successfully change the nickname or not
    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    user = models.User_info.objects.get(username=username)
    user.nickname = nickname
    user.save()
    return JsonResponse({'success': True})


def change_user_password(request):
    ##
    # Change the password of the user.
    # @param username id of the user
    # @param old_password old password of the user
    # @param new_password new password of the user
    # @param user user information in database
    # @retval success whether successfully change the password or not
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
    ##
    # Get all the levels that the current user has.
    # @param number id of the user
    # @param levels quary set of the levels of the user
    # @param level_list level list that the user has
    # @retval level_list
    number = request.POST.get('id', '')
    levels = models.User_level.objects.filter(number=number)
    level_list = []
    for onelevel in levels:
        level_list.append(onelevel.level)
    return JsonResponse({"levels": level_list})


def change_last_level(request):
    ##
    # Change the last level that the user read last time.
    # @param number id of the user
    # @param new_last_level the changed last level of the user
    # @retval success whether successfully change the level or not
    number = request.POST.get('id', '')
    new_last_level = request.POST.get('newlevel', '')
    try:
        user = models.User_info.objects.get(username=number)
        user.lasttime_level = new_last_level
        user.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def get_key(obj):
    ##
    # Get the level.
    return -obj['mark']


def get_all_ranks(request):
    ##
    # Get all users' ranks in a level.
    # @param level the book level
    # @param all_people the users information who have this level
    # @param all_book all books in this level
    # @param result the list of rank result
    # @retval result
    level = request.POST.get('level')
    all_people_level = models.User_level.objects.filter(level=level)
    all_book = models.Book_info.objects.filter(level=level)
    result = []
    counter = 0
    for person_level in all_people_level:
        person = models.User_info.objects.get(
            number=person_level.number.number)
        person_process_mark = 0
        for book in all_book:
            if models.User_process.objects.filter(
                    user_number=person,
                    book_number=book
            ).count() != 0:
                person_process_mark += models.User_process.objects.get(
                    user_number=person,
                    book_number=book
                ).process*60
            if models.User_punch.objects.filter(
                    user_number=person,
                    book_number=book).count() != 0:
                person_process_mark += (40 if models.User_punch.objects.get(
                    user_number=person,
                    book_number=book
                ).is_punched else 0)
        result.append({
            'username': person.username,
            'nickname': person.nickname,
            'mark': person_process_mark
        })
    result.sort(key=get_key)
    return JsonResponse({'people': result})


def log_out(request):
    ##
    # Logout the user.
    # @retval success whether successfully logout or not
    logout(request)
    return JsonResponse({'success': 'true'})
