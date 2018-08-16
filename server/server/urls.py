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
from . import views,createstudent,userlevel,showbooks,showbooks,\
              changepassword,setlevel,authmanager,authstudent
from django.contrib import admin

urlpatterns = [
  path('admin/', admin.site.urls),
  path('create_student', createstudent.create_student),
  path('user_level', userlevel.show_level),
  path('get_books', showbooks.get_books),
  path('',views.main),
  path('auth_student', authstudent.auth_student),
  path('auth_manager', authmanager.auth_manager),
  path('find_books', showbooks.find_books),
  path('change_password',changepassword.change_password),
  path('set_level',setlevel.set_level),
]
