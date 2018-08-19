from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools
from . import debug


def get_book(request):
  book_name = request.POST.get ('bookname')
  book_level = request.POST.get ('level')
  book_level = int (book_level) - 1
  book_introduction = request.POST.get ('introduction')
  book_persual = request.POST.get ('persual')
  book_persual = True if book_persual == 'true' else False
  book_num = models.Book_info.objects.all ().count ()
  book_num += 1
  book = models.Book_info.objects.create (
    number=book_num,
    level=book_level,
    name=book_name,
    introduction=book_introduction,
    is_persual=book_persual
  )
  book.save ()

  book_guides = request.POST.getlist ('guides')
  for i in range (len (book_guides)):
    book_guide = models.Book_guide.objects.create (
      book_number=book,
      guide_number=i,
      guide_text=book_guides[i]
    )
    book_guide.save ()
  book_knowledges = request.POST.getlist ('knowledges')
  for i in range (len (book_knowledges)):
    book_knowledge = models.Book_knowledge.objects.create (
      book_number=book,
      knowledge_number=i,
      knowledge_text=book_knowledges[i]
    )
    book_knowledge.save ()
  word_texts = request.POST.getlist ('word_text')
  word_audios = request.POST.getlist ('word_audio')
  for i in range (len (word_texts)):
    word = models.Book_words.objects.create (
      book_number=book,
      word_number=i,
      word_content=word_texts[i],
      word_sound=word_audios[i]
    )
    word.save ()
  return JsonResponse ({"success": True})
