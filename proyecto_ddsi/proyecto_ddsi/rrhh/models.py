from django.db import models

# Create your models here.

class OfertaEmpleo(models.Model):
    IDOfertaEmpleo=models.CharField(max_length=9, primary_key=True)
    ListaEmpleos=models.CharField(max_length=100)
    FechaInicio=models.DateField()
    FechaFin=models.DateField()

class ContratoImplicado(models.Model):
    DNI=models.CharField(max_length=9, primary_key=True)
    IDOfertaEmpleo=models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE , max_length=9)
    NombreEmpleado=models.CharField(max_length=30)
    Telefono=models.IntegerField(max_length=9)
    NumeroSeguridadSocial=models.IntegerField(max_length=12)
    Salario=models.DecimalField(decimal_places=2)



