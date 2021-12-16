from django import forms
import datetime

class InformeCuentasForm(forms.Form):
    IdInforme = forms.CharField(max_length=10,
                                label="Identificador de Informe", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce identificador de informe"}))
    DATE_SELECTION = []
    for year in range(1999, (datetime.datetime.now().year+1)):
        for month in range (1, 12+1):
            DATE_SELECTION.append(("1/"+str(month)+"/"+str(year), "1/"+str(month)+"/"+str(year)))
    Fecha_Informe = forms.DateField(widget=forms.Select(choices=DATE_SELECTION))                       

class InformeSalarialEmpleadoForm(forms.Form):
    DNI = forms.CharField(max_length=10,
                                label="DNI de trabajador", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce DNI del trabajador"}))

class InformeCampañaForm(forms.Form):
    IdCampaña = forms.CharField( max_length=10,
                                 label="Identificador de Campaña Publicitaria", 
                                 widget=forms.TextInput(attrs={'placeholder': "Introduce identificador de campaña"}))

class InformeProveedorForm(forms.Form):
    NumProveedor = forms.IntegerField(label="Numero de proveedor", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce Numero de Proveedor"}))

class InformeTributarioForm(forms.Form):
    ImporteTributario = forms.FloatField(label="Importe tributario", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce cantidad"}))

class InformePOSForm(forms.Form):
    BeneficiosPOS = forms.FloatField(label="Beneficios POS", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce cantidad"}))
    CodigoPOS = forms.CharField(max_length=10,
                                label="Codigo POS", 
                                widget=forms.TextInput(attrs={'placeholder': "Introduce codigo POS"}))