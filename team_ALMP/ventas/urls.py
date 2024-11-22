from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import ClienteCreate, ClienteUpdate, ProveedorCreate, ProductoCreate, ProductoUpdate, CreateVenta

urlpatterns = [
    path('modelos/', views.modelos, name="modelos"),
    path('createCliente/', ClienteCreate.as_view(), name='createCliente'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='updateCliente'),
    path('buscar_cliente/', views.buscar_clientes, name='buscar_cliente'),
    path('buscar_proveedor/', views.buscar_proveedor, name='buscar_proveedor'),
    path('createProveedor/', ProveedorCreate.as_view(), name='createProveedor'),
    path('venta_search/', views.buscar_ventas, name="search_ventas"),
    path('venta_search_date/', views.buscar_ventas_por_fecha, name='search_ventas_fecha'),
    path('createProducto/', ProductoCreate.as_view(), name='createProducto'),
    path('buscar_producto/', views.buscar_productos, name='buscar_producto'),
    path('updateProducto/<int:pk>/', ProductoUpdate.as_view(), name='updateProducto'),
    path('createVenta/', CreateVenta.as_view(), name='create_venta'),
]
