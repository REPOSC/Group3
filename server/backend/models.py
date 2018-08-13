from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User_info(AbstractUser):
  nickname = models.CharField(max_length=50)
  lasttime_level = models.IntegerField()
  type = models.BooleanField()
  stu_num = models.IntegerField(default=-1)
  mgr_num = models.IntegerField(default=-1)


class User_level(models.Model):
  id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  level = models.IntegerField()
  lasttime_book = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)


class Book_info(models.Model):
  id = models.IntegerField(primary_key=True)
  level = models.IntegerField()
  name = models.CharField(max_length=50)
  introduction = models.TextField()
  pages = models.IntegerField()
  is_persual = models.BooleanField()


class User_process(models.Model):
  user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE)
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  process = models.DecimalField(max_digits=6, decimal_places=2)


class Page_content(models.Model):
  id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  page = models.IntegerField()
  image = models.ImageField()
  sound = models.FileField()
  english_text = models.TextField()
  chinese_text = models.TextField()


class Book_words(models.Model):
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  word_id = models.IntegerField()
  word_content = models.CharField(max_length=50)
  word_sound = models.FileField()


class Book_knowledge(models.Model):
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  knowledge_id = models.IntegerField()
  knowledge_text = models.TextField()


class Book_guide(models.Model):
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  guide_id = models.IntegerField()
  guide_text = models.TextField()


class User_punch(models.Model):
  user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE)
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  is_punched = models.BooleanField(default=False)
  time = models.DateTimeField(default=timezone.now)
  like_number = models.IntegerField(default=0)


class Book_punch_requirement(models.Model):
  id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  requirement = models.TextField()


class User_like(models.Model):
  user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE, related_name='_user_like_userid')
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  like_user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE, related_name='_user_like_likeuserid')


class User_comment(models.Model):
  user_id = models.OneToOneField('User_info', to_field='id',on_delete=models.CASCADE, related_name='_user_comment_userid')
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  comment_user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE, related_name='_user_comment_commentuserid')
  comment = models.TextField()


class Message(models.Model):
  user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE)
  message = models.TextField()
  time = models.DateTimeField(default=timezone.now)


class Firstgame(models.Model):
  id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class Secondgame(models.Model):
  id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class Thirdgame(models.Model):
  id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class Forthgame(models.Model):
  id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE, primary_key=True)
  key = models.CharField(max_length=50)
  value = models.CharField(max_length=50)


class User_game(models.Model):
  user_id = models.OneToOneField('User_info', to_field='id', on_delete=models.CASCADE)
  book_id = models.OneToOneField('Book_info', to_field='id', on_delete=models.CASCADE)
  firstgame = models.BooleanField(default=False)
  secondgame = models.BooleanField(default=False)
  thirdgame = models.BooleanField(default=False)
  forthgame = models.BooleanField(default=False)


class Function_video(models.Model):
  function = models.CharField(max_length=50)
  video = models.FileField()
