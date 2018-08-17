from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_manager(request):
    return render(request, 'login_manager.html')


@login_required
def main(request):
    return render(request, 'index.html')
