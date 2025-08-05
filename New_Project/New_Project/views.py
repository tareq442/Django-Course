from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("This is the HoMe PaGe!")

def Content(request):
    return HttpResponse("This is the ContenT PaGe!")

def index(request):
    return render(request, 'index.html')
