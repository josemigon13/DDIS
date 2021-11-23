from django.db import models

# Create your models here.

class Almacen( models.Model ):
    IdAlmacén = models.CharField( max_length=20 , primary_key=True )
    Dirección = models.CharField( max_length=50 )
    Superficie = models.CharField( max_length=10 )
    FechaInicioAlquiler = models.DateField()
    FechaFinAlquiler = models.DateField()

    def __str__(self):
        return self.IdAlmacén

class LoteProductosAlmacena( models.Model ):
    IdLote = models.CharField( max_length=20 , primary_key=True )
    IdAlmacen = models.ForeignKey( Almacen, on_delete=models.CASCADE )
    Descripción = models.TextField( null=True , blank=True )
    Unidad = models.CharField( max_length=20 )
    Cantidad = models.IntegerField()
    Coste = models.DecimalField( max_digits=10 , decimal_places=2 )

    def __str__(self):
        return self.IdLote
