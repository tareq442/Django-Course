from django.shortcuts import render

def Print(request):
    return render(request,'home.html')
