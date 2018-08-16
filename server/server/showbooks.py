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

def find_books(require):
  try:
    user_number = require.POST.get('id','')
    book_level = require.POST.get('level','')
    search = require.POST.get('search','')
    books_get = []
    books_info = models.Book_info.object.filter(level=book_level)
    for book in books_info:
      if book.name.find(search) != -1:
        newbook = models.User_process.object.filter(user_number=user_number,book_number=book.number)
        books_get.append([book.name, book.id, newbook.process])
    if len(books_get) == 0:
      return JsonResponse({'answer':'no_match'})
    else:
      return JsonResponse({'answer':books_get})
  except:
    return JsonResponse({'answer':'error'})
