# Generated by Django 5.0.7 on 2024-08-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_alter_menu_categoria_alter_menu_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['apellido', 'nombre'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['nombre'], 'verbose_name': 'Menú', 'verbose_name_plural': 'Menús'},
        ),
        migrations.AlterModelOptions(
            name='mesa',
            options={'ordering': ['numero'], 'verbose_name': 'Mesa', 'verbose_name_plural': 'Mesas'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ['fecha'], 'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AddField(
            model_name='menu',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero',
            field=models.IntegerField(unique=True),
        ),
    ]
