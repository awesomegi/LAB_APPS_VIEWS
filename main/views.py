from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string


# Create your views here.

def main_view(request : HttpRequest):
    return render(request, 'main/home.html')

def about_view(request: HttpRequest):
    return render(request, 'main/about.html')

def password_generator(request: HttpRequest):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    context = {
        'generated_password': password
    }
    return render(request, 'main/password.html', context)