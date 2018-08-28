import sys
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
sys.path.append("..")
from server import tools

# Create your models here.


class User_info(AbstractUser):
    number = models.IntegerField(unique=True, null=True)
    nickname = models.CharField(max_length=50)
    lasttime_level = models.IntegerField(default=0)
    is_manager = models.BooleanField(default=False)
    image = models.ImageField(null=True)


class User_level(models.Model):
    number = models.ForeignKey(
        'User_info', to_field='number', on_delete=models.CASCADE, unique=False)
    level = models.IntegerField()
    lasttime_book = models.ForeignKey(
        'Book_info', to_field='number', null=True, on_delete=None)


class Book_info(models.Model):
    number = models.IntegerField(unique=True)
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    introduction = models.TextField()
    pages = models.IntegerField()
    is_persual = models.BooleanField()


class User_process(models.Model):
    user_number = models.ForeignKey(
        'User_info', to_field='number', on_delete=models.CASCADE)
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    process = models.DecimalField(max_digits=6, decimal_places=2)


class Page_content(models.Model):
    number = models.ForeignKey(
        'Book_info',
        to_field='number',
        on_delete=models.CASCADE,)
    page = models.IntegerField()
    image = models.ImageField(upload_to=tools.book_page_picture)
    audio = models.FileField(upload_to=tools.book_page_audio)
    english_text = models.TextField()
    chinese_text = models.TextField()


class Book_words(models.Model):
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    word_number = models.IntegerField()
    word_content = models.CharField(max_length=50)
    word_sound = models.FileField(upload_to=tools.book_word_audio)


class Book_knowledge(models.Model):
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    knowledge_number = models.IntegerField()
    knowledge_text = models.TextField()


class Book_guide(models.Model):
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    guide_number = models.IntegerField()
    guide_text = models.TextField()


class User_punch(models.Model):
    user_number = models.ForeignKey(
        'User_info', to_field='number', on_delete=models.CASCADE)
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    punch_text = models.TextField()
    is_punched = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)
    like_number = models.IntegerField(default=0)


class Book_punch_requirement(models.Model):
    number = models.OneToOneField(
        'Book_info',
        to_field='number',
        on_delete=models.CASCADE,
        primary_key=True)
    requirement = models.TextField()


class User_like(models.Model):
    user_number = models.ForeignKey(
        'User_info',
        to_field='number',
        on_delete=models.CASCADE,
        related_name='_user_like_usernumber')
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    like_user_number = models.ForeignKey(
        'User_info',
        to_field='number',
        on_delete=models.CASCADE,
        related_name='_user_like_likeusernumber')


class User_comment(models.Model):
    user_number = models.ForeignKey(
        'User_info',
        to_field='number',
        on_delete=models.CASCADE,
        related_name='_user_comment_usernumber')
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    comment_user_number = models.ForeignKey(
        'User_info',
        to_field='number',
        on_delete=models.CASCADE,
        related_name='_user_comment_commentusernumber')
    comment = models.TextField()


class Message(models.Model):
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now)


class Message_user(models.Model):
    message = models.ForeignKey(
        'Message', to_field='id', on_delete=models.CASCADE)
    number = models.ForeignKey(
        'User_info', to_field='number', on_delete=models.CASCADE)
    del_status = models.BooleanField()


class First_game(models.Model):
    number = models.ForeignKey(
        'Book_info',
        to_field='number',
        on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.ImageField(upload_to=tools.first_game_image)


class Second_game(models.Model):
    number = models.ForeignKey(
        'Book_info',
        to_field='number',
        on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    true_value = models.ImageField(
        null=True, upload_to=tools.second_game_image)
    false_value_one = models.ImageField(
        null=True, upload_to=tools.second_game_image)
    false_value_two = models.ImageField(
        null=True, upload_to=tools.second_game_image)
    false_value_three = models.ImageField(
        null=True, upload_to=tools.second_game_image)


class Third_game(models.Model):
    number = models.ForeignKey(
        'Book_info',
        to_field='number',
        on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.ImageField(upload_to=tools.third_game_image)
    value_number = models.IntegerField()


class Fourth_game(models.Model):
    number = models.ForeignKey(
        'Book_info',
        to_field='number',
        on_delete=models.CASCADE)
    key = models.FileField(upload_to=tools.fourth_game_audio)
    true_value = models.ImageField(
        null=True, upload_to=tools.fourth_game_image)
    false_value_one = models.ImageField(
        null=True, upload_to=tools.fourth_game_image)
    false_value_two = models.ImageField(
        null=True, upload_to=tools.fourth_game_image)
    false_value_three = models.ImageField(
        null=True, upload_to=tools.fourth_game_image)
    text = models.CharField(max_length=50)


class User_game(models.Model):
    user_number = models.ForeignKey(
        'User_info',
        to_field='number',
        on_delete=models.CASCADE)
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    firstgame = models.BooleanField(default=False)
    secondgame = models.BooleanField(default=False)
    thirdgame = models.BooleanField(default=False)
    forthgame = models.BooleanField(default=False)


class Function_video(models.Model):
    function = models.CharField(max_length=50)
    video = models.FileField(upload_to=tools.function_video)


class Punch_content(models. Model):
    user_number = models.ForeignKey(
        'User_info',
        to_field='number',
        on_delete=models.CASCADE)
    book_number = models.ForeignKey(
        'Book_info', to_field='number', on_delete=models.CASCADE)
    content_number = models.IntegerField(default=0)
    content = models.FileField(upload_to=tools.punch_content)
