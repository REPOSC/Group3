from django.http import JsonResponse
from django.http import HttpResponse
from backend import models
from . import debug


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


def get_first_function(request):
    book_id = request.POST.get('book_id', '')
    book_knowledge_set = models.Book_knowledge.objects.filter(
        book_number=book_id)
    book_guide_set = models.Book_guide.objects.filter(book_number=book_id)
    book_words_set = models.Book_words.objects.filter(book_number=book_id)
    book_knowledge_dict = {}
    book_words_dict = {}
    book_guide_dict = {}
    for book_knowledge in book_knowledge_set:
        book_knowledge_dict[book_knowledge.knowledge_number] = book_knowledge.knowledge_text
    for book_guide in book_guide_set:
        book_guide_dict[book_guide.guide_number] = book_guide.guide_text
    for book_word in book_words_set:
        book_words_dict[book_word.word_number] = book_word.word_content
    return JsonResponse({"knowledge": book_knowledge_dict, "guide": book_guide_dict, "words": book_words_dict})


def get_word_audio(request):
    book_id = request.GET.get('book_id')
    word_id = request.GET.get('audio_index')
    book_word = models.Book_words.objects.get(
        book_number=book_id, word_number=word_id)
    return HttpResponse(book_word.word_sound)


def get_second_function(request):
    book_id = request.POST.get('book_id', '')
    book = models.Book_info.objects.get(number=int(book_id))
    return JsonResponse({'page_number': book.pages})


def get_page_texts(request):
    book_id = request.POST.get('book_id', '')
    book_page = request.POST.get('book_page', '')
    page = models.Page_content.objects.get(
        number=int(book_id), page=int(book_page))
    return JsonResponse({'english': page.english_text, 'chinese': page.chinese_text})


def get_page_audio(request):
    book_id = request.GET.get('book_id')
    page_id = request.GET.get('page_index')
    page = models.Page_content.objects.get(number=book_id, page=page_id)
    return HttpResponse(page.audio)


def get_page_image(request):
    book_id = request.GET.get('book_id')
    page_id = request.GET.get('page_index')
    page = models.Page_content.objects.get(number=book_id, page=page_id)
    return HttpResponse(page.image)


def get_first_game_texts(request):
    book_id = request.POST.get('book_id')
    words = models.First_game.objects.filter(number=book_id)
    texts = []
    for i in words:
        texts.append(i.key)
    return JsonResponse({'texts': texts})


def get_first_game_image(request):
    book_id = request.GET.get('book_id')
    word_text = request.GET.get('word_text')
    book = models.Book_info.objects.get(number=book_id)
    word = models.First_game.objects.get(number=book, key=word_text)
    return HttpResponse(word.value)


def get_second_game_text(request):
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    text = models.Second_game.objects.get(number=book)
    return JsonResponse({'text': text.key})


def get_second_game_image(request):
    book_id = request.GET.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    status = request.GET.get('status')
    number = int(request.GET.get('number'))
    pictures = models.Second_game.objects.get(number=book)
    if status == 'true':
        return HttpResponse(pictures.true_value)
    else:
        if number == 1:
            return HttpResponse(pictures.false_value_one)
        elif number == 2:
            return HttpResponse(pictures.false_value_two)
        else:
            return HttpResponse(pictures.false_value_three)


def get_third_game_number(request):
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    book_number = models.Third_game.objects.filter(number=book).count()
    return JsonResponse({'number': book_number-1})


def get_third_game_image(request):
    book_id = request.GET.get('book_id')
    number = int(request.GET.get('number'))
    book = models.Book_info.objects.get(number=book_id)
    picture = models.Third_game.objects.get(
        number=book, value_number=number)
    return HttpResponse(picture.value)


def get_third_game_text(request):
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    book_number = models.Third_game.objects.filter(number=book)[0]
    return JsonResponse({'text': book_number.key})


def get_fourth_game_image(request):
    book_id = request.GET.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    status = request.GET.get('status')
    number = int(request.GET.get('number'))
    pictures = models.Fourth_game.objects.get(number=book)
    if status == 'true':
        return HttpResponse(pictures.true_value)
    else:
        if number == 1:
            return HttpResponse(pictures.false_value_one)
        elif number == 2:
            return HttpResponse(pictures.false_value_two)
        else:
            return HttpResponse(pictures.false_value_three)


def get_fourth_game_text(request):
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    text = models.Fourth_game.objects.get(number=book)
    return JsonResponse({'text': text.text})


def get_fourth_game_audio(request):
    book_id = request.GET.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    audio = models.Fourth_game.objects.get(number=book)
    return HttpResponse(audio.key)


def get_book_info(request):
    booknumber = request.POST.get('booknumber')
    book = models.Book_info.objects.get(number=booknumber)
    return JsonResponse({'bookpersual': 'true' if book.is_persual else 'false',
                         'bookname': book.name,
                         'booklevel': book.level})
