import random
import os
from . import settings


def random_string(num):
    candicate_chars = "0123456789abcdefghijklmnopqr" \
                      "stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rtn_string = ''
    max_len = len(candicate_chars)
    for i in range(num):
        my_random = random.randint(0, max_len - 1)
        rtn_string += candicate_chars[my_random]
    return rtn_string


def book_page_audio(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Book_Pages_Audios',
                        str(instance.number.number),
                        str(instance.page) + '-' + random_string(5) + filename)


def book_page_picture(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Book_Pages_Pictures',
                        str(instance.number.number),
                        str(instance.page) + '-' + random_string(5) + filename)


def book_word_audio(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Book_Words_Audios',
                        str(instance.book_number.number),
                        str(instance.word_number) + '-' +
                        random_string(5) + filename)


def first_game_image(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_First_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(5) + filename)


def second_game_image(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Second_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(5) + filename)


def third_game_image(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Third_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(5) + filename)


def fourth_game_image(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Fourth_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(8) + filename)


def fourth_game_audio(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Fourth_Game_Audios',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(8) + filename)


def function_video(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Function_videos',
                        str(instance.function) + '-' +
                        random_string(8) + filename)


def punch_content(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Punch_content',
                        str(instance.book_number.number),
                        str(instance.user_number) + '-' +
                        random_string(8) + filename)


def profile_photo(instance, filename):
    return os.path.join(settings.MEDIA_ROOT,
                        'Profile_photo',
                        str(instance.user_number.number) + '-' +
                        random_string(8) + filename)
