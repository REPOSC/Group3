from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User_info(AbstractUser):
  number = models.IntegerField(unique=True, null=True)
  nickname = models.CharField(max_length=50)
  lasttime_level = models.IntegerField(default=0)
  is_manager = models.BooleanField(default=False)


class User_level(models.Model):
  number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE, unique=False)
  level = models.IntegerField()
  lasttime_book = models.ForeignKey('Book_info', to_field='number', null=True, on_delete=None)


class Book_info(models.Model):
  number = models.IntegerField(unique=True)
  level = models.IntegerField()
  name = models.CharField(max_length=50)
  introduction = models.TextField()
  pages = models.IntegerField()
  is_persual = models.BooleanField()


class User_process(models.Model):
  user_number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE)
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  process = models.DecimalField(max_digits=6, decimal_places=2)


class Page_content(models.Model):
  number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  page = models.IntegerField()
  image = models.ImageField()
  sound = models.FileField()
  english_text = models.TextField()
  chinese_text = models.TextField()


class Book_words(models.Model):
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  word_number = models.IntegerField()
  word_content = models.CharField(max_length=50)
  word_sound = models.FileField()


class Book_knowledge(models.Model):
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  knowledge_number = models.IntegerField()
  knowledge_text = models.TextField()


class Book_guide(models.Model):
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  guide_number = models.IntegerField()
  guide_text = models.TextField()


class User_punch(models.Model):
  user_number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE)
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  is_punched = models.BooleanField(default=False)
  time = models.DateTimeField(default=timezone.now)
  like_number = models.IntegerField(default=0)


class Book_punch_requirement(models.Model):
  number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  requirement = models.TextField()


class User_like(models.Model):
  user_number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE, related_name='_user_like_usernumber')
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  like_user_number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE, related_name='_user_like_likeusernumber')


class User_comment(models.Model):
  user_number = models.ForeignKey('User_info', to_field='number',on_delete=models.CASCADE, related_name='_user_comment_usernumber')
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  comment_user_number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE, related_name='_user_comment_commentusernumber')
  comment = models.TextField()


class Message(models.Model):
  message = models.TextField()
  time = models.DateTimeField(default=timezone.now)


class Firstgame(models.Model):
  number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class Secondgame(models.Model):
  number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class Thirdgame(models.Model):
  number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class Forthgame(models.Model):
  number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class User_game(models.Model):
  user_number = models.ForeignKey('User_info', to_field='number', on_delete=models.CASCADE)
  book_number = models.ForeignKey('Book_info', to_field='number', on_delete=models.CASCADE)
  firstgame = models.BooleanField(default=False)
  secondgame = models.BooleanField(default=False)
  thirdgame = models.BooleanField(default=False)
  forthgame = models.BooleanField(default=False)


class Function_video(models.Model):
  function = models.CharField(max_length=50)
  video = models.FileField()
