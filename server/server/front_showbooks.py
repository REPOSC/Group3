from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from backend import models


def get_books(request):
    user_level = request.POST.get('level')
    number = request.POST.get('id')
    books = models.Book_info.objects.filter(level=user_level)
    user_book_info = []
    for book in books:
        try:
            process = models.User_process.objects.get(
                user_number=number, book_number=book.number)
            one_info = {'number': book.number, 'name': book.name,
                        'process': process.process, 'is_persual': book.is_persual}
        except:
            process = 0
            one_info = {'number': book.number, 'name': book.name,
                        'process': process, 'is_persual': book.is_persual}
        user_book_info.append(one_info)
    return JsonResponse({'answer': user_book_info})


def find_books(request):
    try:
        user_number = request.POST.get('id', '')
        book_level = request.POST.get('level', '')
        search = request.POST.get('search', '')
        books_get = []
        books_info = models.Book_info.objects.filter(level=book_level)
        for book in books_info:
            if book.name.find(search) != -1:
                newbook = models.User_process.objects.filter(
                    user_number=user_number, book_number=book.number)
                books_get.append([book.name, book.id, newbook.process])
        if len(books_get) == 0:
            return JsonResponse({'answer': 'no_match'})
        else:
            return JsonResponse({'answer': books_get})
    except:
        return JsonResponse({'answer': 'error'})
