from django.db import models
from rrhh.models import Contrato
from marketing.models import CampaniaPublicitaria
from logistica.models import Proveedor

# Create your models here.

class InformeCuentas(models.Model):
    IdInforme = models.CharField(max_length=9, primary_key=True)
    Fecha_Informe = models.DateField()

class InformeCampania(models.Model):
    IdInforme = models.OneToOneField(InformeCuentas, on_delete=models.CASCADE, primary_key=True,)
    IdCampania = models.ForeignKey(CampaniaPublicitaria, on_delete=models.CASCADE)

class InformeSalarialEmpleado(models.Model):
    IdInforme = models.OneToOneField(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    DNI = models.ForeignKey(Contrato, on_delete=models.CASCADE)

class InformeProveedor(models.Model):
    IdInforme = models.OneToOneField(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    NumProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class InformeTributario(models.Model):
    IdInforme = models.OneToOneField(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    ImporteTributario = models.DecimalField(max_digits=10, decimal_places=2)

class InformePOS(models.Model):
    IdInforme = models.OneToOneField(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    BeneficiosPOS = models.DecimalField(max_digits=10, decimal_places=2)
    CodigoPOS = models.CharField(max_length=9, default="")