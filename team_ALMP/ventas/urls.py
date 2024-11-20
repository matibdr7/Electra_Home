from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import ClienteCreate, ClienteUpdate

urlpatterns = [
    path('modelos/', views.modelos, name="modelos"),
    path('create/', ClienteCreate.as_view(), name='create'),
    path('update/<int:celular>/', ClienteUpdate.as_view(), name='update'),
]
