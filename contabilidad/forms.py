from django.forms import ModelForm
from .models import *

class InformeForm( ModelForm ):
    class Meta:
        model = InformeCuentas
        fields = '__all__'

class InformeSalarialForm( ModelForm ):
    class Meta:
        model = InformeSalarialEmpleado
        fields = ['DNI']

class InformeCampaniaForm( ModelForm ):
    class Meta:
        model = InformeCampania
        fields = ['IdCampania']

class InformeProveedorForm( ModelForm ):
    class meta:
        model = InformeProveedor
        fields = ['NumProveedor']

class InformeTributarioForm( ModelForm ):
    class meta:
        model = InformeTributario
        fields = ['importeTributario']

class InformePOSForm( ModelForm ):
    class meta:
        model = InformeTributario
        fields = ['idPOS','beneficiosPOS']