from django.shortcuts import render
from django.http import HttpResponse

def About(request):
    return HttpResponse("This is the About PaGe")

def Phone(request):
    return HttpResponse("This is the Phone PaGe")
