from django.db import models

# Create your models here.

class Almacen( models.Model ):
    IdAlmacen = models.CharField( max_length=20 , primary_key=True )
    Direccion_Alm = models.CharField( max_length=50 )
    Superficie = models.CharField( max_length=10 )
    FechaIniAlquiler_Alm = models.DateField()
    FechaFinAlquiler_Alm = models.DateField()

    def __str__(self):
        return self.IdAlmacén

class LoteProductos( models.Model ):
    IdLote = models.CharField( max_length=20 , primary_key=True )
    IdAlmacen = models.ForeignKey( Almacen, on_delete=models.CASCADE )
    Descripcion_Lote = models.TextField( null=True , blank=True )
    Unidad = models.CharField( max_length=20 )
    Cantidad_Lote = models.IntegerField()
    Coste_Lote = models.DecimalField( max_digits=10 , decimal_places=2 )

    def __str__(self):
        return self.IdLote
