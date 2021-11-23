from django.db import models
from rrhh import models

# Create your models here.

class InformeCuentas(models.Model):
    idInforme = models.IntegerField(primary_key=True)
    fechaInforme = models.DateField()

class InformeCampaña(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    idCampaña = models.ForeignKey(CampañaPublicitaria, on_delete=models.CASCADE)

class InformeSalarialEmpleado(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    DNI = models.ForeignKey(Contrato, on_delete=models.CASCADE)

class InformeProveedor(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    numProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class InformeTributario(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    importeTributario = models.DecimalField(decimal_places=2)

class InformePOS(models.Model):
    idInforme = models.ForeignKey(InformeCuentas, on_delete=models.CASCADE, primary_key=True)
    beneficiosPOS = models.DecimalField(decimal_places=2)
