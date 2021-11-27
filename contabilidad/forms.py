from django.forms.fields import DateTimeField
from django.forms import ModelForm
from .models import *

class InformeForm( ModelForm ):
    fechaInforme = DateTimeField(input_formats=['%MM-%YY'])
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
        fields = ['ImporteTributario']

class InformePOSForm( ModelForm ):
    class meta:
        model = InformePOS
        fields = ['IdPOS','BeneficiosPOS']