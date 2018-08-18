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
from . import views, createstudent, userlevel, showbooks, \
    changepassword, setlevel, authmanager, authstudent,\
    getbookcontent, addmanager, changemanager, delmanager,\
    putmessage
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_student', createstudent.create_student),
    path('user_level', userlevel.show_level),
    path('get_books', showbooks.get_books),
    path('', views.main),
    path('auth_student', authstudent.auth_student),
    path('auth_manager', authmanager.auth_manager),
    path('find_books', showbooks.find_books),
    path('change_password', changepassword.change_password),
    path('set_level', setlevel.set_level),
    path('add_manager', addmanager.add_manager),
    path('change_manager', changemanager.change_manager),
    path('del_manager', delmanager.del_manager),
    path('get_first_function', getbookcontent.get_first_function),
    path('get_second_function', getbookcontent.get_second_function),
    path('get_third_function', getbookcontent.get_third_function),
    path('get_fourth_function', getbookcontent.get_fourth_function),
    path('get_fifth_function', getbookcontent.get_fifth_function),
    path('put_message', putmessage.put_message),
]
