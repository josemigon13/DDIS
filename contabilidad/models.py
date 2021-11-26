from django.db import models
from rrhh.models import Contrato
from marketing.models import CampaniaPublicitaria
from logistica.models import Proveedor

# Create your models here.

class InformeCuentas(models.Model):
    idInforme = models.CharField(max_length=9, primary_key=True)
    fechaInforme = models.DateField()

class InformeCampania(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    IdCampania = models.ForeignKey(CampaniaPublicitaria, on_delete=models.CASCADE)

class InformeSalarialEmpleado(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    DNI = models.ForeignKey(Contrato, on_delete=models.CASCADE)

class InformeProveedor(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    NumProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class InformeTributario(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    importeTributario = models.DecimalField(decimal_places=2)

class InformePOS(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    idPOS = models.CharField(max_length=9)
    beneficiosPOS = models.DecimalField(decimal_places=2)
