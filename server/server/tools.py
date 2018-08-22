import random
import os
from . import settings
from . import debug

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
    return os.path.join(settings.MEDIA_ROOT, 'Book_Pages_Audios', str(instance.number.number), str(instance.page) + '-' + random_string(5) + filename)


def book_page_picture(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, 'Book_Pages_Pictures', str(instance.number.number), str(instance.page) + '-' + random_string(5) + filename)


def book_word_audio(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, 'Book_Words_Audios', str(instance.book_number.number), str(instance.word_number) + '-' + random_string(5) + filename)