from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse('contato.html')


def sobre(request):
    return HttpResponse('sobre.html')
