from django.shortcuts import HttpResponse,render

def home(request):
    return render(request,"core/home.html")

# Create your views here.

def acercade(request):
    return render(request, "core/acercade.html")