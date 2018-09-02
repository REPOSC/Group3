"""This module includes some functions about books of miniprogram."""
# coding=utf-8
from django.http import JsonResponse
from django.http import HttpResponse
from backend import models


def get_books(request):
    ##
    # Get the information of the books of a specific level.
    # @param user_level level of current user
    # @param number id of current user
    # @param books books information of the current level
    # @param user_book_info list of the books in current level
    # @param process the user reading process of a book
    # @param one_info the information of one book
    # @retval user_book_info
    user_level = request.POST.get('level')
    number = request.POST.get('id')
    books = models.Book_info.objects.filter(level=user_level)
    user_book_info = []
    for book in books:
        try:
            process = models.User_process.objects.get(
                user_number=number, book_number=book.number)
            one_info = {'number': book.number, 'name': book.name,
                        'process': process.process,
                        'is_persual': book.is_persual}
        except:
            process = 0
            one_info = {'number': book.number, 'name': book.name,
                        'process': process, 'is_persual': book.is_persual}
        user_book_info.append(one_info)
    return JsonResponse({'answer': user_book_info})


def get_first_function(request):
    ##
    # Get the guide contents of the books.
    # @param book_id id of the books to get guide contents from
    # @param book_knowledge_set a list of knowledge got from the book
    # @param book_guide_set a list of guide got from the book
    # @param book_words_set a list of word texts got from the book
    # @param book_knowledge_dict dict of the knowledge, for every piece key is the number of the knowledge and the value is the knowledge itself.
    # @param book_guide_dict dict of the guide, for every piece key is the number of the guide and the value is the guide itself.
    # @param book_words_dict dict of the word texts, for every piece key is the number of the word texts and the value is the word text itself.
    # @retval book_knowledge_dict
    # @retval book_guide_dict
    # @retval book_words_dict
    # @retval the summary of the words
    book_id = request.POST.get('book_id', '')
    book_knowledge_set = models.Book_knowledge.objects.filter(
        book_number=book_id)
    book_guide_set = models.Book_guide.objects.filter(book_number=book_id)
    book_words_set = models.Book_words.objects.filter(book_number=book_id)
    book_knowledge_dict = {}
    book_words_dict = {}
    book_guide_dict = {}
    for book_knowledge in book_knowledge_set:
        book_knowledge_dict[book_knowledge.knowledge_number] = \
        book_knowledge.knowledge_text
    for book_guide in book_guide_set:
        book_guide_dict[book_guide.guide_number] = book_guide.guide_text
    for book_word in book_words_set:
        book_words_dict[book_word.word_number] = book_word.word_content
    return JsonResponse({
        "knowledge": book_knowledge_dict,
        "guide": book_guide_dict,
        "words": book_words_dict,
        "wordslen": len(book_words_dict)
    })


def get_word_audio(request):
    ##
    # Get the word audio binary HttpResponse of a specific word text
    # @param book_id id of the book containing the word from
    # @param word_id id of the word number of the specific book
    # @retval the binary audio value
    book_id = request.GET.get('book_id')
    word_id = request.GET.get('audio_index')
    book_word = models.Book_words.objects.get(
        book_number=book_id, word_number=word_id)
    return HttpResponse(book_word.word_sound)


def get_second_function(request):
    ##
    # Get the page summary of a book
    # @param book_id the id of the book to get page summary from
    # @param book a book object got by the book_id
    # @retval the summary of the book pages
    book_id = request.POST.get('book_id', '')
    book = models.Book_info.objects.get(number=int(book_id))
    return JsonResponse({'page_number': book.pages})


def get_page_texts(request):
    ##
    # Get the english and chinese text of a specific page of a book
    # @param book_id the id of the book to get texts from
    # @param book_page the page number of the text
    # @param page the page object containing the english and chinese text
    # @retval english text of the page
    # @retval chinese text of the page
    book_id = request.POST.get('book_id', '')
    book_page = request.POST.get('book_page', '')
    page = models.Page_content.objects.get(
        number=int(book_id), page=int(book_page))
    return JsonResponse({
        'english': page.english_text,
        'chinese': page.chinese_text
    })


def get_page_audio(request):
    ##
    # Get the page audio binary HttpResponse of a specific page
    # @param book_id the id of the book to get audio from
    # @param book_page the page number of the audio
    # @param page the page object containing the audio
    # @retval the binary audio value
    book_id = request.GET.get('book_id')
    page_id = request.GET.get('page_index')
    page = models.Page_content.objects.get(number=book_id, page=page_id)
    return HttpResponse(page.audio)


def get_page_image(request):
    ##
    # Get the page image binary HttpResponse of a specific page
    # @param book_id the id of the book to get image from
    # @param book_page the page number of the image
    # @param page the page object containing the image
    # @retval the binary image value
    book_id = request.GET.get('book_id')
    page_id = request.GET.get('page_index')
    page = models.Page_content.objects.get(number=book_id, page=page_id)
    return HttpResponse(page.image)


def get_first_game_texts(request):
    ##
    # Get all the texts of the first game(matching game) of a book
    # @param book_id id of the book to get texts from
    # @param words all the texts of the words and their corresponding images
    # @param texts all the texts of the book
    # @retval texts
    book_id = request.POST.get('book_id')
    words = models.First_game.objects.filter(number=book_id)
    texts = []
    for i in words:
        texts.append(i.key)
    return JsonResponse({'texts': texts})


def get_first_game_image(request):
    ##
    # Get the image binary HttpResponse of a specific word of the first game
    # @param book_id the id of the book to get image from
    # @param book the book object got by the book_id
    # @param word_text the word text corresponding to the image
    # @param word the word object got by the book and word_text
    # @retval the binary image value
    book_id = request.GET.get('book_id')
    word_text = request.GET.get('word_text')
    book = models.Book_info.objects.get(number=book_id)
    word = models.First_game.objects.get(number=book, key=word_text)
    return HttpResponse(word.value)


def get_second_game_text(request):
    ##
    # Get the text of the second game(select image according to a word)
    # @param book_id the id of the book to get text from
    # @param book the book object got by the book_id
    # @param text the second_game object of the book
    # @retval the text of the second_game object
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    text = models.Second_game.objects.get(number=book)
    return JsonResponse({'text': text.key})


def get_second_game_image(request):
    ##
    # Get the image binary of the 1st, 2nd or 3rd wrong answer or the right answer of the second game of a book
    # @param book_id the id of the book to get image from
    # @param book the book object got by the book_id
    # @param status the right or wrong answer image of the second game
    # @param number if wrong answer image, the 1st, 2nd or 3rd wrong answer
    # @param pictures the second_game object got by book object
    # @retval the binary image value
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
    ##
    # Get the amount of the pictures of the third game(jigsaw puzzle)
    # @param book_id the id of the book to get number from
    # @param book the book object got by the book_id
    # @param book_number the third_game the amount of the pictures(including the full image)of the third game
    # @retval booknumber-1 to get the amount of all image but the full one
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    book_number = models.Third_game.objects.filter(number=book).count()
    return JsonResponse({'number': book_number-1})


def get_third_game_image(request):
    ##
    # Get the image binary of the third game
    # @param book_id the id of the book to get image from
    # @param number the number of the image (-1 if the full image)
    # @param book the book object got by the book_id
    # @param picture the third_game object
    # @retval the image binary of the specific number
    book_id = request.GET.get('book_id')
    number = int(request.GET.get('number'))
    book = models.Book_info.objects.get(number=book_id)
    picture = models.Third_game.objects.get(
        number=book, value_number=number)
    return HttpResponse(picture.value)


def get_third_game_text(request):
    ##
    # Get the text of the third game
    # @param book_id the id of the book to get text from
    # @param book the book object got by the book_id
    # @param book_number the third_game object
    # @retval the text of the third_game object
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    book_number = models.Third_game.objects.filter(number=book)[0]
    return JsonResponse({'text': book_number.key})


def get_fourth_game_image(request):
    ##
    # Get the image binary of the 1st, 2nd or 3rd wrong answer or the right answer of the fourth game(select image according to an audio) of a book
    # @param book_id the id of the book to get image from
    # @param book the book object got by the book_id
    # @param status the right or wrong answer image of the second game
    # @param number if wrong answer image, the 1st, 2nd or 3rd wrong answer
    # @param pictures the fourth_game object got by book object
    # @retval the binary image value
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
    ##
    # Get the text of the fourth game
    # @param book_id the id of the book to get text from
    # @param book the book object got by the book_id
    # @param text the fourth_game object of the book
    # @retval the text of the fourth_game object
    book_id = request.POST.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    text = models.Fourth_game.objects.get(number=book)
    return JsonResponse({'text': text.text})


def get_fourth_game_audio(request):
    ##
    # Get the audio binary of the fourth game
    # @param book_id the id of the book to get audio from
    # @param book the book object got by the book_id
    # @param audio the fourth_game object of the book
    # @retval the audio binary of the fourth_game object
    book_id = request.GET.get('book_id')
    book = models.Book_info.objects.get(number=book_id)
    audio = models.Fourth_game.objects.get(number=book)
    return HttpResponse(audio.key)


def get_book_info(request):
    ##
    # Get the information of a book
    # @param booknumber the id of the book to get information from
    # @param book the book object got by the booknumber
    # @retval bookpersual whether the book is persual or not
    # @retval bookname the name of the book
    # @retval booklevel the level of the book
    booknumber = request.POST.get('booknumber')
    book = models.Book_info.objects.get(number=booknumber)
    return JsonResponse({'bookpersual': 'true' if book.is_persual else 'false',
                         'bookname': book.name,
                         'booklevel': book.level})
