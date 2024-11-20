from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import ClienteCreate, ClienteUpdate

urlpatterns = [
    path('modelos/', views.modelos, name="modelos"),
    path('create/', ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='update'),
    path('buscar_cliente/', views.buscar_clientes, name='buscar_cliente')
]
