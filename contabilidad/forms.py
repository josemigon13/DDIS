from django import forms
from django.forms import ModelForm
from .models import *

# class InformeForm( forms.Form ):
#     # IdInforme = forms.CharField(label="Identificador del Informe:",
#     #                                 widget=forms.TextInput(attrs={'placeholder':  "Introduce identificador"}))
#     # Fecha_Informe = forms.DateField(  label="Fecha del Informe (en formato MM-YYYY)",
#     #                                 widget=forms.TextInput(attrs={'placeholder':  "Introduce fecha de informe"}), 
#     #                                 input_formats=['%MM-%YYYY'])
class InformeForm( ModelForm ):
    #fechaInforme = DateTimeField(input_formats=['%MM-%YYYY']) # daba fallo al migrar
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
        fields = ['CodigoPOS','BeneficiosPOS']