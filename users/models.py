from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    rut = models.CharField(max_length=20)
    persona_contacto = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    rubro = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
        
class Cliente(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    descripcion = models.CharField(max_length=20)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    precio = models.IntegerField()
    marca = models.CharField(max_length=20)
    existencia_actual = models.IntegerField()
    cod_familia = models.IntegerField()
    fecha_vencimiento = models.IntegerField()
    def __str__(self):
        return self.descripcion

class Credito(models.Model):
    deudor = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    monto_pago = models.IntegerField()
    ESTADO = (
        ('CANCELADA','CANCELADA'),
        ('PENDIENTE','PENDIENTE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    detalle_venta = models.TextField()
    def __str__(self):
        return self.pk

class Venta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    monto_pago = models.IntegerField()
    detalle_venta = models.TextField()
    def __str__(self):
        return self.pk

class Pedido(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    detalle_pedido = models.TextField()
    def __str__(self):
        return self.pk