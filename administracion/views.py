from django.shortcuts import render, redirect
from .models import Menu, Mesa, Empleado, Venta
from .forms import MenuForm, MesaForm, EmpleadoForm

def index(request):
    return render(request, 'administracion/index.html')

def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'administracion/menu_list.html', {'menus': menus})

def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'administracion/menu_form.html', {'form': form})

def mesa_list(request):
    mesas = Mesa.objects.all()
    return render(request, 'administracion/mesa_list.html', {'mesas': mesas})

def mesa_create(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm()
    return render(request, 'administracion/mesa_form.html', {'form': form})

def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'administracion/empleado_list.html', {'empleados': empleados})

def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'administracion/empleado_form.html', {'form': form})

def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'administracion/venta_list.html', {'ventas': ventas})