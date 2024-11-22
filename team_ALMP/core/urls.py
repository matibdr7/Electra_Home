from team_ALMP.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="home"),
    path('acerca-de/', views.acercade, name="acercade"),
    path('contacto/', views.contacto, name="contacto"),
    path('productos/', views.productos, name="productos"),
    path('register/', views.registro, name="register"),
    path('login/', views.signin, name="signin"),
    path('signout/', views.signout, name='signout'),
    path('', include('ventas.urls')),
]
