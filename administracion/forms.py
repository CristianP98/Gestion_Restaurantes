# forms.py
from django import forms
from .models import Menu, Mesa, Empleado, Venta

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['nombre', 'precio', 'descripcion', 'categoria', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'imagen': forms.ClearableFileInput(attrs={'multiple': False}),
        }

class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidad']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'puesto', 'fecha_contratacion']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['item', 'cantidad']
        widgets = {
            'item': forms.Select(),
            'cantidad': forms.NumberInput(attrs={'min': 1}),
        }
