from django import forms
from login_menu_pral.views import Conexion_BD
from operator import itemgetter
import re
from django.core.exceptions import ValidationError


class AltaContratoForm(forms.Form):
    DNI = forms.CharField( max_length=9,
                            label="Identificador de Contrato", 
                            widget=forms.TextInput(attrs={'placeholder': "Introduce el DNI del empleado"}))
    IDOfertaEmpleo = forms.CharField( max_length=9,
                                    label="ID oferta de empleo", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador de la oferta de empleo de la que deriva el contrato"}))
    Nombre_Empleado = forms.CharField(max_length=30,
                                    label="Nombre del empleado", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce el nombre del empleado"}))
    Tlf_Empleado = forms.IntegerField(label="Teléfono del empleado", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce el teléfono del empleado"}))
    NumSegSocial = forms.IntegerField(label="Número Seguridad Social", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce el número de la seguridad social del empleado"}))
    Salario = forms.DecimalField( max_digits=10, decimal_places=2,
                                        label="Salario Empleado", 
                                        widget=forms.TextInput(attrs={'placeholder':  "Introduce el salario del empleado"}))


class BajaContratoForm(forms.Form):
    #DNI = forms.CharField( max_length=9,
    #                       label="Identificador de Contrato", 
    #                        widget=forms.TextInput(attrs={'placeholder': "Introduce el DNI del empleado cuyo contrato quiere dar de baja"}))



    def __init__(self, *args, **kwargs):
        super(BajaContratoForm, self).__init__(*args, **kwargs)

        try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:

                baja_contr=[]
                cursor.execute("SELECT DNI, Nombre_Empleado FROM Contrato")
                for fila in cursor.fetchall():
                    print("prueba:", (str(fila[0]) + " ("+str(fila[1])+")"))
                    baja_contr.append( ((str(fila[0]), str(fila[0]) + " ("+str(fila[1])+")")))
                
        except:
            baja_contr = [('', 'No hay contratos disponibles en la BD. Vuelva atrás para continuar.')]

        # Aun no habiendo fallado las sentencias contra la base de datos pero no habiendo ninguna tupla:
        if len(baja_contr) == 0:
            baja_contr = [('', 'No hay contratos disponibles en la BD. Vuelva atrás para continuar.')]

        self.fields['ListaContrato'] = forms.ChoiceField(  
                    label="Elija un contrato de la lista de contratos para borrar",
                    widget=forms.RadioSelect,
                    choices=baja_contr
                )

class ConsultarContratoForm(forms.Form):
    DNI = forms.CharField( max_length=9,
                            label="Identificador de Contrato", 
                            widget=forms.TextInput(attrs={'placeholder': "Introduce el DNI del empleado cuyo contrato quiere consultar"}))


class AltaOfertaForm(forms.Form):
    IDOfertaEmpleo = forms.CharField( max_length=9,
                                    label="ID oferta de empleo", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador de la oferta de empleo a dar de alta"}))
    ListadoEmpleos = forms.CharField(max_length=100,
                                    label="Lista empleos", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce la lista de empleos"}))
    FechaIni_OferEmp = forms.DateField(label="Fecha de Inicio de la Oferta de empleo (en formato YYYY-MM-DD)",
                                    widget=forms.TextInput(attrs={'placeholder':  "Introduce la fecha de inicio de la oferta de empleo"}))
    FechaFin_OferEmp = forms.DateField(label="Fecha de Finalización de la Oferta de empleo (en formato YYYY-MM-DD)",
                                    widget=forms.TextInput(attrs={'placeholder':  "Introduce la fecha de final de la oferta de empleo"}))


class BajaOfertaForm(forms.Form):
    #IDOfertaEmpleo = forms.CharField( max_length=9,
    #                                label="ID oferta de empleo", 
    #                                widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador de la oferta de empleo a dar de baja"}))

    def __init__(self, *args, **kwargs):
        super(BajaOfertaForm, self).__init__(*args, **kwargs)

        try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:

                baja_ofer=[]
                cursor.execute("SELECT IDOfertaEmpleo, ListadoEmpleos FROM OfertaEmpleo")
                for fila in cursor.fetchall():
                    baja_ofer.append( ((str(fila[0]), str(fila[0]) + " ("+str(fila[1])+")")))
                
        except:
            baja_ofer = [('', 'No hay ofertas de empleo disponibles en la BD. Vuelva atrás para continuar.')]

        # Aun no habiendo fallado las sentencias contra la base de datos pero no habiendo ninguna tupla:
        if len(baja_ofer) == 0:
            baja_ofer = [('', 'No hay ofertas de empleo disponibles en la BD. Vuelva atrás para continuar.')]

        self.fields['ListaOfertas'] = forms.ChoiceField(  
                    label="Elija una oferta de empleos de la lista de ofertas para borrar",
                    widget=forms.RadioSelect,
                    choices=baja_ofer
                )