# Estos son los urls para trabajar dentro de la app core

from team_ALMP.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('acerca-de', views.acercade, name="acercade"),
]
