from io import BytesIO
from PIL import Image
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from backend import models
from . import tools


def get_book_info(request):
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
    third_game_text = request.POST.get('third_game_text')
    third_game_splits = int(request.POST.get('third_game_splits'))
    third_game_picture = request.FILES.get('third_game_picture')
    third_game_spliting_picture = Image.open(third_game_picture)
    every_part_x = third_game_spliting_picture.size[0]/third_game_splits
    every_part_y = third_game_spliting_picture.size[1]/third_game_splits
    for i in range(third_game_splits):
        for j in range(third_game_splits):
            tmp_image = third_game_spliting_picture.crop([int(every_part_x*j), int(every_part_y*i),
                                                          int(every_part_x*(j+1)), int(every_part_y*(i+1))])
            tmp_image_bytes = BytesIO()
            tmp_image.save(tmp_image_bytes, third_game_spliting_picture.format)
            tmp_upload_file = InMemoryUploadedFile(tmp_image_bytes, None, tools.random_string(5)+'.jpg', 'image/jpeg',
                                                   len(tmp_image_bytes.getvalue()), None)
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
    expand_text = request.POST.get('expand')
    if expand_text != '':
        expand = models.Book_punch_requirement.objects.create(
            number=book,
            requirement=expand_text
        )
        expand.save()


def get_book(request):
    try:
        book = get_book_info(request)
        put_guides(request, book)
        put_pages(request, book)
        if book.is_persual == True:
            put_game1(request, book)
            put_game2(request, book)
            put_game3(request, book)
            put_game4(request, book)
        put_expands(request, book)
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
