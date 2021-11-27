from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField
from almacen.models import Almacen

# Create your models here.

class Proveedor( models.Model ):
    NumProveedor = models.IntegerField( primary_key=True )
    Nombre_Prov = models.CharField( max_length=40 )
    DireccionWeb_Prov = models.CharField( max_length=20 )
    Tlf_Prov = models.CharField( max_length=20 )

    def __str__(self):
        return str(self.NumProveedor)

class Pedido( models.Model ):
    NumPedido = models.IntegerField( primary_key=True )
    NumProveedor = models.ForeignKey( Proveedor , on_delete=CASCADE )
    IdAlmacen = models.ForeignKey( Almacen , on_delete=CASCADE )
    Articulos = models.CharField( max_length=200 )
    Fecha_Ped = models.DateField()
    Precio_Ped = models.DecimalField( max_digits=10 , decimal_places=2 )

    def __str__(self):
        return str(self.NumPedido)