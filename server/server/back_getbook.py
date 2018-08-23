from django.http import JsonResponse
from backend import models


def get_book(request):
    book_name = request.POST.get('bookname')
    book_level = request.POST.get('level')
    book_level = int(book_level) - 1
    book_introduction = request.POST.get('introduction')
    book_persual = request.POST.get('persual')
    book_persual = True if book_persual == 'true' else False
    book_num = models.Book_info.objects.all().count()
    book_num += 1
    book_guides = request.POST.getlist('guides')
    book_knowledges = request.POST.getlist('knowledges')
    word_texts = request.POST.getlist('word_text')
    word_audios = request.FILES.getlist('word_audio')
    page_english_texts = request.POST.getlist('book_english_text')
    page_chinese_texts = request.POST.getlist('book_chinese_text')
    page_audios = request.FILES.getlist('book_audio')
    page_pictures = request.FILES.getlist('book_picture')
    book = models.Book_info.objects.create(
        number=book_num,
        level=book_level,
        name=book_name,
        introduction=book_introduction,
        pages=len(page_chinese_texts),
        is_persual=book_persual
    )
    book.save()
    for i in range(len(book_guides)):
        book_guide = models.Book_guide.objects.create(
            book_number=book,
            guide_number=i,
            guide_text=book_guides[i]
        )
        book_guide.save()
    for i in range(len(book_knowledges)):
        book_knowledge = models.Book_knowledge.objects.create(
            book_number=book,
            knowledge_number=i,
            knowledge_text=book_knowledges[i]
        )
        book_knowledge.save()
    for i in range(len(word_texts)):
        word = models.Book_words.objects.create(
            book_number=book,
            word_number=i,
            word_content=word_texts[i],
            word_sound=word_audios[i]
        )
        word.save()
    for i in range(len(page_english_texts)):
        page = models.Page_content.objects.create(
            number=book,
            page=i,
            image=page_pictures[i],
            audio=page_audios[i],
            english_text=page_english_texts[i],
            chinese_text=page_chinese_texts[i]
        )
        page.save()
    return JsonResponse({"success": True})
