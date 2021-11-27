from django.db import models

# Create your models here.

class OfertaEmpleo(models.Model):
    IDOfertaEmpleo=models.CharField(max_length=9, primary_key=True)
    ListadoEmpleos=models.CharField(max_length=100)
    FechaIni_OferEmp=models.DateField()
    FechaFin_OferEmp=models.DateField()

class Contrato(models.Model):
    DNI=models.CharField(max_length=9, primary_key=True)
    IDOfertaEmpleo=models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE , max_length=9)
    Nombre_Empleado=models.CharField(max_length=30)
    Tlf_Empleado=models.IntegerField()
    NumSegSocial=models.IntegerField()
    Salario=models.DecimalField(decimal_places=2, max_digits=10)
