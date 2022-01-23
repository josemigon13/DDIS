from django import forms
from login_menu_pral.views import Conexion_BD
from operator import itemgetter
#import re
#from django.core.exceptions import ValidationError



class ProveedorForm( forms.Form ):
	NumProveedor = forms.IntegerField(  label="Número identificativo del proveedor", 
										widget=forms.TextInput( attrs={'placeholder': "Introduce número de proveedor"} ),
										error_messages={'invalid': 'ERROR: Valor NO entero introducido.'})

	Nombre_Prov = forms.CharField( max_length=40,
								   label="Nombre de la empresa proveedora", 
								   widget=forms.TextInput( attrs={'placeholder': "Introduce nombre del proveedor"} ) )

	DireccionWeb_Prov = forms.CharField( max_length=20,
										 label="Dirección web del proveedor", 
										 widget=forms.TextInput( attrs={'placeholder': "Introduce dirección web del proveedor"} ) )
 
	Tlf_Prov = forms.CharField( max_length=20,
								label="Teléfono del proveedor", 
								widget=forms.TextInput( attrs={'placeholder': "Introduce teléfono del proveedor"} ) )



class PedidoForm( forms.Form ):
    NumPedido = forms.IntegerField( label="Número identificativo del pedido", 
									widget=forms.TextInput( attrs={'placeholder': "Introduce número del pedido"} ),
									error_messages={'invalid': 'ERROR: Valor NO entero introducido.'})
                                    
    NumProveedor = forms.IntegerField(  label="Número identificativo del proveedor", 
										widget=forms.TextInput( attrs={'placeholder': "Introduce número de proveedor"} ),
										error_messages={'invalid': 'ERROR: Valor NO entero introducido.'})
    
    IdAlmacen = forms.CharField( label="IdAlmacén",
								 widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador del almacén"}))
                                 
    Articulos = forms.CharField( max_length=200,
								 label="Artículos del pedido", 
								 widget=forms.TextInput( attrs={'placeholder': "Introduce artículos del pedido"} ) )
                                 
    Fecha_Ped = forms.DateField( label="Fecha de la realización del pedido (en formato YYYY-MM-DD)",
									widget=forms.TextInput( attrs={'placeholder': "Introduce fecha del pedido"} ),
									error_messages={'invalid': 'ERROR: Formato de fecha incorrecta. Recuerda que es "YYYY-MM-DD".'} )
    
    Precio_Ped = forms.DecimalField( max_digits=10, decimal_places=2,
										label="Precio del pedido (en euros, €)", 
										widget=forms.TextInput( attrs={'placeholder': "Introduce el precio del pedido"} ),
										error_messages={'invalid': 'ERROR: Valor NO flotante introducido.'} )
 

class pkProveedorForm( forms.Form ):
    NumProveedor = forms.CharField( 
                label="Número de Proveedor",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el número de proveedor"}))
                
class pkPedidoForm( forms.Form ):
    NumPedido = forms.CharField( 
                label="Número de pedido:",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el número de pedido"}))
