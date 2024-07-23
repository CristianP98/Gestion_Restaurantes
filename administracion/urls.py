from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menus/', views.menu_list, name='menu_list'),
    path('mesas/', views.mesa_list, name='mesa_list'),
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('ventas/', views.venta_list, name='venta_list'),

    path('menus/nuevo/', views.menu_create, name='menu_create'),
    path('mesas/nueva/', views.mesa_create, name='mesa_create'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
]