from django.db import models

# Create your models here.

class CampaniaPublicitaria(models.Model):
    IdCampania = models.CharField(max_length=10, primary_key=True)
    Nombre_CampPub = models.CharField(max_length=40)
    Descripcion_CampPub = models.CharField(max_length=100)
    Precio_CampPub = models.DecimalField(decimal_places=2)
    ListaMediosEmision = models.CharField(max_length=100)

class OfertaProductos(models.Model):
    IdOfertaProd = models.CharField(max_length=10, primary_key=True)
    Nombre_OferProd = models.CharField(max_length=40)
    ListaProductos = models.CharField(max_length=10)
    Precio_OferProd = models.DecimalField(decimal_places=2)
    FechaIni_OferProd = models.DateField()
    FechaFin_OferProd = models.DateField()

class Promociona(models.Model):
    IdCampania = models.ForeignKey(CampaniaPublicitaria, on_delete = models.CASCADE)
    IdOfertaProd = models.ForeignKey(OfertaProductos, on_delete = models.CASCADE)
