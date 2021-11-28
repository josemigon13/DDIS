from django import forms
from django.forms import ModelForm
from .models import *
import datetime

class InformeForm( forms.ModelForm ):
    DATE_SELECTION = []
    for year in range(1999, (datetime.datetime.now().year+1)):
        for month in range (1, 12+1):
            DATE_SELECTION.append(("1/"+str(month)+"/"+str(year), "1/"+str(month)+"/"+str(year)))
    Fecha_Informe = forms.DateField(widget=forms.Select(choices=DATE_SELECTION))
    class Meta:
        model = InformeCuentas
        fields = ['IdInforme']

class InformeSalarialForm( ModelForm ):
    class Meta:
        model = InformeSalarialEmpleado
        fields = ['DNI']

class InformeCampaniaForm( ModelForm ):
    class Meta:
        model = InformeCampania
        fields = ['IdCampania']

class InformeProveedorForm( ModelForm ):
    class Meta:
        model = InformeProveedor
        fields = ['NumProveedor']

class InformeTributarioForm( ModelForm ):
    class Meta:
        model = InformeTributario
        fields = ['ImporteTributario']

class InformePOSForm( ModelForm ):
    class Meta:
        model = InformePOS
        fields = ['CodigoPOS','BeneficiosPOS']