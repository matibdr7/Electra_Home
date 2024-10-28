# Estos son los urls para trabajar dentro de la app core

from team_ALMP.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('acercade/', views.acercade),
]
