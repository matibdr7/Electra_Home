from django.shortcuts import HttpResponse, redirect,render
from django.core.mail import send_mail
from django.conf import settings
from ventas.models import Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

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
                login (request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'register.html', {
                    'form':UserCreationForm,
                    'error': 'Usuario ya existente'
                })
        return render (request, 'register.html',{
           'form': UserCreationForm,
           'error': 'Contraseñas no coincidentes'})
    
def signin(request):
   if request.method == "GET":
       return render (request, 'signin.html', {
           'form': AuthenticationForm
       })
   else: 
       user = authenticate(
                      request, username = request.POST ['username'], password = request.POST ['password'])