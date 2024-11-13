from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modelos/', views.modelos, name="modelos")
]
