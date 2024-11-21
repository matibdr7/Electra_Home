from django.shortcuts import render
from .models import Venta, Cliente, Producto, Proveedor
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.utils import timezone
from django.db.models import Q
from datetime import datetime

from django.urls import reverse_lazy

def modelos(request):
    ventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    #clientes = Cliente.objects.filter(nombre__contains='fel')
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()

    contexto = {
        'ventas': ventas,
        'clientes': clientes,
        'productos': productos,
        'proveedores': proveedores,
    }
    
    return render(request, "ventas/modelos.html", contexto)
# Create your views here.
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    success_url = reverse_lazy('modelos')
    
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email', 'celular', 'foto']
    template_name_suffix = '_update_cliente'
    
    def get_success_url(self):
        return reverse_lazy('modelos')

def buscar_clientes(request):
    # Si hay un término de búsqueda en la solicitud
    busqueda = request.GET.get('search', '')  # 'search' es el nombre del parámetro de la barra de búsqueda
    clientes = Cliente.objects.filter(nombre__contains=busqueda)
    return render(request, 'ventas/buscar_cliente.html', {'clientes': clientes})

def buscar_proveedor(request):
    busqueda_proveedor = request.GET.get('busqueda_proveedor', '')
    if busqueda_proveedor:
        proveedores = Proveedor.objects.filter(nombre__contains=busqueda_proveedor)
    else:
        proveedores = Proveedor.objects.all()
    return render(request, 'ventas/buscar_proveedor.html', {'proveedores': proveedores})

class ProveedorCreate(CreateView):
    model = Proveedor
    fields = ['nombre', 'contacto', 'telefono', 'email', 'direccion']
    success_url = reverse_lazy('modelos')


def buscar_ventas(request):
    busqueda_venta = request.GET.get('q', '')  # Obtenemos el valor de la búsqueda
    if busqueda_venta:
        # Intentamos convertir el texto de búsqueda a una fecha si es posible
        try:
            fecha_busqueda = datetime.strptime(busqueda_venta, '%Y-%m-%d').date()
            # Si la conversión tiene éxito, usamos fecha como filtro
            ventas = Venta.objects.filter(
                Q(producto__nombre__icontains=busqueda_venta)
            )
        except ValueError:
            # Si no es una fecha válida, buscamos solo por nombre
            ventas = Venta.objects.filter(
                Q(producto__nombre__icontains=busqueda_venta)
            )
    else:
        ventas = Venta.objects.all()

    return render(request, 'ventas/venta_list.html', {'ventas': ventas})

def formatear_fecha_busqueda(fecha_str):
    # Lista de abreviaturas de los meses y meses completos
    meses_abreviados = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    
    meses_completos = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6,
        'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }

    # Limpiar la entrada de caracteres innecesarios (puntos, comas y espacios extra)
    fecha_str = fecha_str.replace('.', '').replace(',', '').strip().lower()

    # Intentar identificar el formato de la fecha
    try:
        # Intentar formato "Nov 15 2024" o "nov 15 2024"
        if len(fecha_str.split()) == 3:
            mes_abbr, dia, año = fecha_str.split()
            dia = int(dia)
            año = int(año)
            
            # Convertir el mes abreviado a número
            mes = meses_abreviados.get(mes_abbr.capitalize())
            if mes:
                return datetime(año, mes, dia).date()
        
        # Intentar formato "noviembre 14 2024"
        if len(fecha_str.split()) == 3:
            mes, dia, año = fecha_str.split()
            dia = int(dia)
            año = int(año)
            
            # Convertir el mes completo a número
            mes = meses_completos.get(mes)
            if mes:
                return datetime(año, mes, dia).date()

        # Intentar formato "15/11/24"
        if fecha_str.count('/') == 2:
            dia, mes, año = fecha_str.split('/')
            return datetime(2000 + int(año), int(mes), int(dia)).date()  # Asumimos que el año es 2000 + año proporcionado

    except ValueError:
        return None  # Si no se puede formatear correctamente, devolver None
    
    return None  # Si no coincide con ningún formato esperado

def buscar_ventas_por_fecha(request):
    fechas = []  # Inicializamos 'fechas' para que siempre tenga un valor
    busqueda_fecha = request.GET.get('q', '')  # Obtener el valor de la búsqueda, por defecto vacío
    
    if busqueda_fecha:
        # Asegúrate de usar la función para formatear correctamente la fecha
        fecha_formateada = formatear_fecha_busqueda(busqueda_fecha)
        
        if fecha_formateada:
            # Comparar solo la fecha, sin tener en cuenta las horas
            fechas = Venta.objects.filter(fecha__date=fecha_formateada)
        else:
            fechas = []  # Si la fecha no es válida, dejamos 'fechas' vacío
    else:
        # Si no hay búsqueda, mostramos todas las fechas
        fechas = Venta.objects.all()

    return render(request, 'ventas/venta_list_fecha.html', {'fechas': fechas})
