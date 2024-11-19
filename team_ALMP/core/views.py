from django.shortcuts import HttpResponse,render
from django.core.mail import send_mail
from django.conf import settings
from ventas.models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

def registro(request):
    if request.method =='GET':
        return render(request, 'core/register.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST ['password1'] == request.POST ['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creaado satisfactoriamente')
            except:
                return HttpResponse(' Usuario ya existente')
        return HttpResponse ('Passwords no coinciden')