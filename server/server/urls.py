"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views, back_student, back_manager, back_message, back_book, \
    front_book, front_student, front_forum, back_forum, back_introduction,\
    front_message
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_student', front_student.auth_student),
    path('user_level', front_student.show_level),
    path('change_last_level', front_student.change_last_level),
    path('change_process', front_student.change_process),
    path('get_process', front_student.get_process),
    path('get_user_image', front_student.get_user_image),
    path('get_user_nickname', front_student.get_user_nickname),
    path('change_user_image', front_student.change_user_image),
    path('change_user_nickname', front_student.change_user_nickname),
    path('change_user_password', front_student.change_user_password),
    path('log_out', front_student.log_out),
    path('get_books', front_book.get_books),
    path('get_first_function', front_book.get_first_function),
    path('get_second_function', front_book.get_second_function),
    path('get_word_audio', front_book.get_word_audio),
    path('get_page_audio', front_book.get_page_audio),
    path('get_page_image', front_book.get_page_image),
    path('get_page_texts', front_book.get_page_texts),
    path('get_first_game_image', front_book.get_first_game_image),
    path('get_first_game_texts', front_book.get_first_game_texts),
    path('get_second_game_image', front_book.get_second_game_image),
    path('get_second_game_text', front_book.get_second_game_text),
    path('get_third_game_image', front_book.get_third_game_image),
    path('get_third_game_number', front_book.get_third_game_number),
    path('get_third_game_text', front_book.get_third_game_text),
    path('get_fourth_game_image', front_book.get_fourth_game_image),
    path('get_fourth_game_text', front_book.get_fourth_game_text),
    path('get_fourth_game_audio', front_book.get_fourth_game_audio),
    path('get_book_persual', front_book.get_book_persual),
    path('get_message', front_message.get_message),
    path('read_message', front_message.read_message),
    path('unread_message', front_message.unread_message),
    path('delete_message', front_message.delete_message),
    path('', views.main),
    path('all_student', back_student.all_student),
    path('get_student', back_student.get_student),
    path('create_student', back_student.create_student),
    path('change_password', back_student.change_password),
    path('set_level', back_student.set_level),
    path('auth_manager', back_manager.auth_manager),
    path('add_manager', back_manager.add_manager),
    path('change_manager', back_manager.change_manager),
    path('del_manager', back_manager.del_manager),
    path('get_managers', back_manager.get_managers),
    path('change_selfpassword', back_manager.change_selfpassword),
    path('get_manager_info', back_manager.get_manager_info),
    path('put_message', back_message.put_message),
    path('get_book', back_book.get_book),
    path('all_book', back_book.all_book),
    path('get_punch_info', front_forum.get_punch_info),
    path('upload_homework', front_forum.upload_homework),
    path('all_daka', back_forum.all_daka),
    path('daka_comment', back_forum.daka_comment),
    path('daka_like', back_forum.daka_like),
    path('del_comment', back_forum.del_comment),
    path('del_punch', back_forum.del_punch),
    path('add_introduction_video', back_introduction.add_introduction_video)]
