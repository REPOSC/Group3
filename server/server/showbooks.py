from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from backend import models


def get_books(require):
  try:
    user_level = require.POST.get('level')
    number = require.POST.get('id')
    books = models.Book_info.object.filter(level=user_level)
    user_book_info = []
    for book in books:
      process = models.User_process.object.filter(number=number, book_id=book.number)
      one_info = [book.number, book.name, process.process]
      user_book_info.append(one_info)
    return JsonResponse({'answer':user_book_info})
  except:
    return JsonResponse({'answer':'error'})
