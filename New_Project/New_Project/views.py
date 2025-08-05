from django.http import HttpResponse

def Home(request):
    return HttpResponse("This is the HoMe PaGe!")

def Content(request):
    return HttpResponse("This is the ContenT PaGe!")
