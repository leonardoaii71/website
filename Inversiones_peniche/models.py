from django.db import models
import datetime
# from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateTimeField(blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True)
    correo = models.CharField(max_length=35, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    numero_telefono = models.IntegerField(null=True)
    numero_cel = models.IntegerField(null=True)


class Tipo(models.Model):
    tipo = models.CharField(max_length=50)


class Vehiculo(models.Model):
    tipo_vehiculo = (
        ('1',"Carro"),
        ('2','Camion'),
        ('3','Jeepeta/Suv'),
        ('4','Van')
    )

    matricula = models.CharField(unique=True, max_length=40, blank=True, null=True)
    modelo = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(default=1, max_length=2, blank=True, null=True,  choices=tipo_vehiculo)
    color = models.CharField(max_length=10, blank=True, null=True)
    condicion = models.CharField(max_length=10, blank=True, null=True)
    valor_mercado = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

class Rol(models.Model):
    nombre = models.CharField


class Operador(Persona):
    fecha_contratacion = models.DateField


class Cuota(models.Model):
    mora_acumulada = models.FloatField
    vencida = models.BooleanField


class Cliente(Persona):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
            return reverse('index', kwargs={'id': self.id})


class Prestamo(models.Model):

    tipoPres = (
        ('Normal', 'Normal'),
        ('Amortizado', 'Amortizado')
    )


    plazoMeses = (
        (12, '12 Meses'),
        (24, '24 Meses'),
        (36, '36 Meses'),
        (48, '48 Meses'),
        (60, '60 Meses'),
        (72, '72 Meses')
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    cuotas = models.ForeignKey(Cuota, on_delete=models.CASCADE, null=True, blank=True)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
    operador = models.OneToOneField(Operador, on_delete=models.CASCADE, null=True, blank=True)
    fecha_actual = models.DateTimeField(null=True, blank=True, default=timezone.now)
    fecha_primer_pago = models.DateTimeField(null=True, blank=True)
    monto_prestado = models.FloatField(null=True, blank=True)
    frecuencia_pago = models.CharField(max_length=30,  null=True, blank=True)
    tasa_interes = models.FloatField(null=True, blank=True)
    monto_capital = models.FloatField(null=True, blank=True)
    monto_interes = models.FloatField(null=True, blank=True)
    tipo_prestamo = models.CharField(max_length=30, null=True, blank=True, choices=tipoPres, default="Normal")
    estado = models.CharField(max_length=30, null=True, blank=True)
    monto_total = models.FloatField( null=True, blank=True)
    total_cuotas_pagadas = models.IntegerField(null=True, blank=True)
    fecha_ultimo_pago = models.DateTimeField(null=True, blank=True)
    monto_ultimo_pago = models.FloatField(null=True, blank=True)
    intereses_vencidos = models.FloatField(null=True, blank=True)
    plazo=models.IntegerField(null=True, blank=True, choices=plazoMeses, default="12")
    total_intereses = models.FloatField( null=True, blank=True)
    pago_mensual =  models.FloatField( null=True, blank=True)

class Factura (models.Model):
    tipo = models.CharField
    cliente = models.OneToOneField(Cliente)
    prestamo = models.OneToOneField(Prestamo)
    cuota = models.OneToOneField(Cuota)
    usuario = models.OneToOneField(Operador)
    nombre_usuario = models.CharField
    fecha = models.DateTimeField
    monto_total = models.FloatField
    balance_deudor = models.FloatField
    monto_capital = models.FloatField
    monto_interes = models.FloatField


class Usuario(Persona):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    password_salt = models.CharField(max_length=30)
    last_log = models.DateTimeField
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)




