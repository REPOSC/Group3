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
from . import views, back_createstudent, front_userlevel, front_showbooks, back_changepassword, back_setlevel, \
    back_authmanager, front_authstudent, front_getbookcontent, back_addmanager, back_changemanager, back_delmanager, \
    back_putmessage, back_getmanagers, back_getbook, back_allstudent, back_getstudent, front_changeprocess, \
    front_getprocess, front_getuserimage, front_getusernickname, front_changeusernickname, front_changeuserpassword,\
    front_changeuserimage, logout
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_student', front_authstudent.auth_student),
    path('user_level', front_userlevel.show_level),
    path('change_last_level', front_userlevel.change_last_level),
    path('get_books', front_showbooks.get_books),
    path('find_books', front_showbooks.find_books),
    path('get_first_function', front_getbookcontent.get_first_function),
    path('get_second_function', front_getbookcontent.get_second_function),
    path('', views.main),
    path('all_student', back_allstudent.all_student),
    path('get_student', back_getstudent.get_student),
    path('create_student', back_createstudent.create_student),
    path('auth_manager', back_authmanager.auth_manager),
    path('change_password', back_changepassword.change_password),
    path('set_level', back_setlevel.set_level),
    path('add_manager', back_addmanager.add_manager),
    path('change_manager', back_changemanager.change_manager),
    path('del_manager', back_delmanager.del_manager),
    path('put_message', back_putmessage.put_message),
    path('get_book', back_getbook.get_book),
    path('get_managers', back_getmanagers.get_managers),
    path('get_word_audio', front_getbookcontent.get_word_audio),
    path('get_page_audio', front_getbookcontent.get_page_audio),
    path('get_page_image', front_getbookcontent.get_page_image),
    path('get_page_texts', front_getbookcontent.get_page_texts),
    path('change_process', front_changeprocess.change_process),
    path('get_process', front_getprocess.get_process),
    path('get_first_game_image', front_getbookcontent.get_first_game_image),
    path('get_first_game_texts', front_getbookcontent.get_first_game_texts),
    path('get_second_game_image', front_getbookcontent.get_second_game_image),
    path('get_second_game_text', front_getbookcontent.get_second_game_text),
    path('get_third_game_image', front_getbookcontent.get_third_game_image),
    path('get_third_game_number', front_getbookcontent.get_third_game_number),
    path('get_third_game_text', front_getbookcontent.get_third_game_text),
    path('get_fourth_game_image', front_getbookcontent.get_fourth_game_image),
    path('get_fourth_game_text', front_getbookcontent.get_fourth_game_text),
    path('get_fourth_game_audio', front_getbookcontent.get_fourth_game_audio),
    path('get_user_image', front_getuserimage.get_user_image),
    path('get_user_nickname', front_getusernickname.get_user_nickname),
    path('change_user_image', front_changeuserimage.change_user_image),
    path('change_user_nickname', front_changeusernickname.change_user_nickname),
    path('change_user_password', front_changeuserpassword.change_user_password),
    path('log_out', logout.log_out)
]
