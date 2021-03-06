from django import forms
import datetime

class InformeCuentasForm(forms.Form):
    IdInforme = forms.IntegerField(min_value=1, label="Identificador de Informe", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce identificador de informe"}))
    DATE_SELECTION = []
    for year in range(1999, (datetime.datetime.now().year+1)):
        for month in range (1, 12+1):
            DATE_SELECTION.append((str(month)+"/1/"+str(year), str(month)+"/1/"+str(year)))
    Fecha_Informe = forms.DateField(widget=forms.Select(choices=DATE_SELECTION))                     

class InformeSalarialEmpleadoForm(forms.Form):
    DNI = forms.CharField(max_length=10,
                                label="DNI de trabajador", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce DNI de trabajador"}))

class InformeCampañaForm(forms.Form):
    IdCampaña = forms.CharField( max_length=10,
                                 label="Identificador de Campaña Publicitaria", 
                                 widget=forms.TextInput(attrs={'placeholder': "Introduce identificador de campaña"}))

class InformeProveedorForm(forms.Form):
    NumProveedor = forms.IntegerField(label="Número de proveedor", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce Número de Proveedor"}))

class InformeTributarioForm(forms.Form):
    ImporteTributario = forms.FloatField(label="Importe tributario", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce cantidad"}))

class InformePOSForm(forms.Form):
    BeneficiosPOS = forms.FloatField(label="Beneficios POS", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce cantidad"}))
    CodigoPOS = forms.IntegerField(label="Código POS", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce código POS"}))