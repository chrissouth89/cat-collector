from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Lolo', 'Tabby', 'Kinda Rude', 3),
    Cat('Sachi', 'Tortoiseshell', 'Looks like a turtle', 0),
    Cat('Fancy', 'Bombay', 'Happy fluff ball', 4),
    Cat('Bonk', 'Selkirk Rex', 'Meows loudly', 6),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    return render(request, 'cats/index.html', {'cats': cats})