from django.db import models

class Menu(models.Model):
    CATEGORIAS = [
        ('entrante', 'Entrante'),
        ('plato', 'Plato Principal'),
        ('bebida', 'Bebida'),
        ('postre', 'Postre'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()

    def __str__(self):
        return f'Mesa {self.numero} (Capacidad: {self.capacidad})'

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'Venta de {self.cantidad} {self.item.nombre} el {self.fecha}'
