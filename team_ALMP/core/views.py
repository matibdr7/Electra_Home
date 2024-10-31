from django.shortcuts import HttpResponse,render

def index(request):
    return render(request,"core/index.html")

# Create your views here.

def acercade(request):
    return render(request, 'core/acercade.html')

def contacto(request):
    return render(request, 'core/contacto.html')