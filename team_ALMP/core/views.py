from django.shortcuts import HttpResponse,render
from django.core.mail import send_mail
from django.conf import settings
from ventas.models import Producto

def index(request):
    return render(request, 'core/index.html')

# Create your views here.

def acercade(request):
    return render(request, 'core/acercade.html')

def contacto(request):
    if request.method == "POST":
        subject=request.POST["subject"]
        
        message=request.POST["message"] + "" + request.POST["email"]
        
        email_from=settings.EMAIL_HOST_USER
        
        recipient_list=["electrahome99@gmail.com"]
        
        send_mail(subject, message, email_from, recipient_list)
    
    return render(request, 'core/contacto.html')

def productos(request):
    productos = Producto.objects.all()
    lista_productos = {
        'productos': productos,
    }
    return render(request, 'core/productos.html', lista_productos)
