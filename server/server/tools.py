"""This module include some tools that other modules will use."""
import random
import os
from . import settings


def random_string(num):
    ##
    # Create a random string, used in create password and file name.
    # @param rtn_string the string that created in random
    # @param max_len max length
    # @retval rtn_string
    candicate_chars = "0123456789abcdefghijklmnopqr" \
                      "stuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rtn_string = ''
    max_len = len(candicate_chars)
    for i in range(num):
        my_random = random.randint(0, max_len - 1)
        rtn_string += candicate_chars[my_random]
    return rtn_string


def book_page_audio(instance, filename):
    ##
    # Get the path of book page audio.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Book_Pages_Audios',
                        str(instance.number.number),
                        str(instance.page) + '-' + random_string(5) + filename)


def book_page_picture(instance, filename):
    ##
    # Get the path of book page picture.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Book_Pages_Pictures',
                        str(instance.number.number),
                        str(instance.page) + '-' + random_string(5) + filename)


def book_word_audio(instance, filename):
    ##
    # Get the path of book word audio.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Book_Words_Audios',
                        str(instance.book_number.number),
                        str(instance.word_number) + '-' +
                        random_string(5) + filename)


def first_game_image(instance, filename):
    ##
    # Get the path of the first game's image.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_First_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(5) + filename)


def second_game_image(instance, filename):
    ##
    # Get the path of the second game's image.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Second_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(5) + filename)


def third_game_image(instance, filename):
    ##
    # Get the path of the third game's image.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Third_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(5) + filename)


def fourth_game_image(instance, filename):
    ##
    # Get the path of the fourth game's image.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Fourth_Game_Pictures',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(8) + filename)


def fourth_game_audio(instance, filename):
    ##
    # Get the path of the first game's audio.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Boot_Fourth_Game_Audios',
                        str(instance.number.number),
                        str(instance.key) + '-' + random_string(8) + filename)


def function_video(instance, filename):
    ##
    # Get the path of the function introduction video.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Function_videos',
                        str(instance.function) + '-' +
                        random_string(8) + filename)


def punch_content(instance, filename):
    ##
    # Get the path of the punch files.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Punch_content',
                        str(instance.book_number.number),
                        str(instance.user_number) + '-' +
                        random_string(8) + filename)


def profile_photo(instance, filename):
    ##
    # Get the path of the profile photo of one user.
    # @retval path the file path
    return os.path.join(settings.MEDIA_ROOT,
                        'Profile_photo',
                        str(instance.number) + '-' +
                        random_string(8) + filename)
