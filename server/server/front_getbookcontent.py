from django.http import JsonResponse
from backend import models


def get_first_function(request):
    book_id = request.POST.get('book_id', '')
    book_knowledge_set = models.Book_knowledge.object.filter(
        book_number=book_id)
    book_guide_set = models.Book_guide.object.filter(book_number=book_id)
    book_words_set = models.Book_words.object.filter(book_number=book_id)
    book_knowledge_dict = {}
    book_words_dict = {}
    book_guide_dict = {}
    for book_knowledge in book_knowledge_set:
        book_knowledge_dict[book_knowledge.knowledge_number] = book_knowledge.knowledge_text
    for book_guide in book_guide_set:
        book_guide_dict[book_guide.guide_number] = book_guide.guide_text
    for book_word in book_words_set:
        book_words_dict[book_word.word_number] = [
            book_word.word_content, book_word.word_sound]
    return JsonResponse({"knowledge": book_knowledge_dict, "guide": book_guide_dict, "words": book_words_dict})


def get_second_function(request):
    user_id = request.POST.get('user_id', '')
    book_id = request.POST.get('book_id', '')
    one_process = models.User_process.object.filter(
        user_number=user_id, book_number=book_id)
    one_book_words = models.Book_words.object.filter(book_number=book_id)


def get_third_function(request):
    user_id = request.POST.get('user_id', '')
    book_id = request.POST.get('book_id', '')
    one_process = models.User_process.object.filter(
        user_number=user_id, book_number=book_id)
    one_book_words = models.Book_words.object.filter(book_number=book_id)


def get_fourth_function(request):
    user_id = request.POST.get('user_id', '')
    book_id = request.POST.get('book_id', '')
    one_process = models.User_process.object.filter(
        user_number=user_id, book_number=book_id)
    one_book_words = models.Book_words.object.filter(book_number=book_id)


def get_fifth_function(request):
    user_id = request.POST.get('user_id', '')
    book_id = request.POST.get('book_id', '')
    one_process = models.User_process.object.filter(
        user_number=user_id, book_number=book_id)
    one_book_words = models.Book_words.object.filter(book_number=book_id)
