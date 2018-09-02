"""This module includes some functions of books."""
# coding=utf-8
from io import BytesIO
from PIL import Image
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from backend import models
from . import tools


def get_book_info(request):
    ##
    # Get a book information.
    # @param book_name tne name of one book
    # @param book_level the level of one book
    # @param book_introduction the introduction of one book
    # @param book_persual the persual of one book is intensive or extensive
    # @param book_num the number of all book which is filtered
    # @retval book one object has book information
    book_name = request.POST.get('bookname')
    book_level = request.POST.get('level')
    book_level = int(book_level) - 1
    book_introduction = request.POST.get('introduction')
    book_persual = request.POST.get('persual')
    book_persual = True if book_persual == 'persual' else False
    book_num = models.Book_info.objects.all().count()
    book_num += 1
    book = models.Book_info.objects.create(
        number=book_num,
        level=book_level,
        name=book_name,
        introduction=book_introduction,
        pages=0,
        is_persual=book_persual)
    book.save()
    return book


def put_guides(request, book):
    ##
    # Add the guide of one book.
    # @param book_guides tne guide text of one book
    # @param book_knowledges the knowledge of one book
    # @param word_texts the texts of one book words
    # @param word_audios the audios of one book words
    # @param book_guide the guide of one book
    # @param book_number the number of one book
    # @param word_content the content of a word
    # @param word_sound the sound of a word
    # @param word_number the number of a word in book words
    book_guides = request.POST.getlist('guides')
    book_knowledges = request.POST.getlist('knowledges')
    word_texts = request.POST.getlist('word_text')
    word_audios = request.FILES.getlist('word_audio')
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


def put_pages(request, book):
    ##
    # Add the pages of one book.
    # @param page_english_texts the text of every page English
    # @param page_chinese_texts the text of every page Chinese
    # @param page_audios the audios of every book
    # @param page_pictures the pictures of every book
    # @param book.pages the length of one book
    page_english_texts = request.POST.getlist('book_english_text')
    page_chinese_texts = request.POST.getlist('book_chinese_text')
    page_audios = request.FILES.getlist('book_audio')
    page_pictures = request.FILES.getlist('book_picture')
    book.pages = len(page_english_texts)
    book.save()
    for i in range(book.pages):
        page = models.Page_content.objects.create(
            number=book,
            page=i,
            image=page_pictures[i],
            audio=page_audios[i],
            english_text=page_english_texts[i],
            chinese_text=page_chinese_texts[i]
        )
        page.save()


def put_game1(request, book):
    ##
    # Add the first game of one book.
    # @param first_game_texts the text of the first game
    # @param first_game_pictures the picture of the first game
    # @param number the number of the book
    first_game_texts = request.POST.getlist('first_game_text')
    first_game_pictures = request.FILES.getlist('first_game_picture')
    for i in range(len(first_game_texts)):
        first_game = models.First_game.objects.create(
            number=book,
            key=first_game_texts[i],
            value=first_game_pictures[i]
        )
        first_game.save()


def put_game2(request, book):
    ##
    # Add the second game of one book.
    # @param second_game_text the text of the second game
    # @param true_value the true answer of the second game
    # @param false_value_one the first wrong answer of the second game
    # @param false_value_two the second wrong answer of the second game
    # @param false_value_three the third wrong answer of the second game
    second_game_text = request.POST.get('second_game_text')
    second_game_answer = int(request.POST.get('second_game_answer'))
    second_game_pictures = request.FILES.getlist('second_game_picture')
    second_game_selection = models.Second_game.objects.create(
        number=book,
        key=second_game_text,
        true_value=second_game_pictures[second_game_answer],
        false_value_one=second_game_pictures[1 ^ second_game_answer],
        false_value_two=second_game_pictures[2 ^ second_game_answer],
        false_value_three=second_game_pictures[3 ^ second_game_answer],
    )
    second_game_selection.save()


def put_game3(request, book):
    ##
    # Add the third game of one book.
    # @param third_game_text the text of the third game
    # @param third_game_splits the way to split the game
    # @param third_game_picture the picture of the third game
    # @param third_game_spliting_picture the picture of the third game
    # @param every_part_x the length of every splited pictures
    # @param every_part_y the height of every splited pictures
    # @param tmp_image the splited pictures of the third game
    # @param tmp_image_bytes the bytes file of the pictures
    # @param tmp_upload_file the file to upload the picture
    third_game_text = request.POST.get('third_game_text')
    third_game_splits = int(request.POST.get('third_game_splits'))
    third_game_picture = request.FILES.get('third_game_picture')
    third_game_spliting_picture = Image.open(third_game_picture)
    every_part_x = third_game_spliting_picture.size[0]/third_game_splits
    every_part_y = third_game_spliting_picture.size[1]/third_game_splits
    for i in range(third_game_splits):
        for j in range(third_game_splits):
            tmp_image = third_game_spliting_picture.crop(
                [int(every_part_x*j), int(every_part_y*i),
                 int(every_part_x*(j+1)), int(every_part_y*(i+1))])
            tmp_image_bytes = BytesIO()
            tmp_image.save(tmp_image_bytes, third_game_spliting_picture.format)
            tmp_upload_file = InMemoryUploadedFile(
                tmp_image_bytes,
                None,
                tools.random_string(5)+'.jpg',
                'image/jpeg',
                len(tmp_image_bytes.getvalue()),
                None)
            third_game_selection = models.Third_game.objects.create(
                number=book,
                key=third_game_text,
                value=tmp_upload_file,
                value_number=i*third_game_splits+j
            )
            third_game_selection.save()
    third_game_selection = models.Third_game.objects.create(
        number=book,
        key=third_game_text,
        value=third_game_picture,
        value_number=-1
    )
    third_game_selection.save()


def put_game4(request, book):
    ##
    # Add the fourth game of one book.
    # @param fourth_game_text the text of the fourth game
    # @param fourth_game_audio the audio of the fourth game
    # @param fourth_game_answer the answer of the fourth game
    # @param fourth_game_selection the selection of the fourth game
    # @param number the number of the book
    # @param true_value the true answer of the fourth game
    # @param false_value_one the first wrong answer of the fourth game
    # @param false_value_two the second wrong answer of the fourth game
    # @param false_value_three the third wrong answer of the fourth game
    fourth_game_text = request.POST.get('fourth_game_text')
    fourth_game_audio = request.FILES.get('fourth_game_audio')
    fourth_game_answer = int(request.POST.get('fourth_game_answer'))
    fourth_game_pictures = request.FILES.getlist('fourth_game_picture')
    fourth_game_selection = models.Fourth_game.objects.create(
        number=book,
        key=fourth_game_audio,
        text=fourth_game_text,
        true_value=fourth_game_pictures[fourth_game_answer],
        false_value_one=fourth_game_pictures[1 ^ fourth_game_answer],
        false_value_two=fourth_game_pictures[2 ^ fourth_game_answer],
        false_value_three=fourth_game_pictures[3 ^ fourth_game_answer],
    )
    fourth_game_selection.save()


def put_expands(request, book):
    ##
    # Add the punch requirements of one book.
    # @param expand_text the text of the one book punch requirements
    # @number the number of one book
    expand_text = request.POST.get('expand')
    if expand_text != '':
        expand = models.Book_punch_requirement.objects.create(
            number=book,
            requirement=expand_text
        )
        expand.save()


def get_book(request):
    ##
    # Get the book we wanted.
    # @param book an object including all information of one book
    # @retval booknumber the number of one book
    try:
        book = get_book_info(request)
        put_guides(request, book)
        put_pages(request, book)
        if book.is_persual:
            put_game1(request, book)
            put_game2(request, book)
            put_game3(request, book)
            put_game4(request, book)
        put_expands(request, book)
    except:
        return JsonResponse({"booknumber": None})
    return JsonResponse({"booknumber": book.number})


def all_book(request):
    ##
    # Get all books we owned.
    # @param books objects including all information of one book
    # @param book_names all names of every book
    # @param book_numbers the number of every book
    # @param levels the level of every book
    # @param persuals the persual of every book is intensive or extensive
    # @param readings the number of persons who have read every book
    # @param readeds the number of persons who have finished  every book
    # @retval book_name book_names
    # @retval book_number book_numbers
    # @retval levels
    # @retval persuals
    # @retval readings
    # @retval readeds
    books = models.Book_info.objects.all()
    book_names = []
    book_numbers = []
    levels = []
    persuals = []
    readings = []
    readeds = []
    for i in books:
        readingnum = models.User_process.objects.filter(
            book_number=i.number).count()
        readednum = models.User_process.objects.filter(
            book_number=i.number, process=1).count()
        readings.append(readingnum)
        readeds.append(readednum)
        book_names.append(i.name)
        book_numbers.append(i.number)
        levels.append(i.level)
        if i.is_persual:
            persuals.append('精读')
        else:
            persuals.append('泛读')
    return JsonResponse({
        'book_name': book_names,
        'book_number': book_numbers,
        'level': levels,
        'persual': persuals,
        'reading': readings,
        'readed': readeds
    })


def del_book(request):
    ##
    # Delete one book.
    # @param booknumber the number of one book
    # @revatl success whether successfully delete the book
    booknumber = request.POST.get('book_number')
    book = models.Book_info.objects.get(number=booknumber)
    models.Punch_content.objects.filter(book_number=book).delete()
    models.User_game.objects.filter(book_number=book).delete()
    models.First_game.objects.filter(number=book).delete()
    models.Second_game.objects.filter(number=book).delete()
    models.Third_game.objects.filter(number=book).delete()
    models.Fourth_game.objects.filter(number=book).delete()
    models.User_comment.objects.filter(book_number=book).delete()
    models.User_like.objects.filter(book_number=book).delete()
    models.Book_punch_requirement.objects.filter(number=book).delete()
    models.User_punch.objects.filter(book_number=book).delete()
    models.Book_guide.objects.filter(book_number=book).delete()
    models.Book_knowledge.objects.filter(book_number=book).delete()
    models.Book_words.objects.filter(book_number=book).delete()
    models.Page_content.objects.filter(number=book).delete()
    models.User_process.objects.filter(book_number=book).delete()
    models.Book_info.objects.filter(number=booknumber).delete()
    return JsonResponse({'success': 'true'})
