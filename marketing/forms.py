from django import forms
from login_menu_pral.views import Conexion_BD
from operator import itemgetter
import re
from django.core.exceptions import ValidationError


class CampañaPublicitariaForm(forms.Form):
    IdCampaña = forms.CharField( max_length=10,
                                 label="Identificador de la Campaña Publicitaria", 
                                 widget=forms.TextInput(attrs={'placeholder': "Introduce identificador de campaña"}))
    Nombre_CampPub = forms.CharField( max_length=40,
                                      label="Nombre de la Campaña", 
                                      widget=forms.TextInput(attrs={'placeholder': "Introduce nombre de campaña"}))
    Descripcion_CampPub = forms.CharField(max_length=100,
                                      label="Descripción de la Campaña", 
                                      widget=forms.TextInput(attrs={'placeholder': "Introduce descripción de campaña"}))
    Precio_CampPub = forms.DecimalField( max_digits=10, decimal_places=2,
                                         label="Precio de la Campaña (en euros, €)", 
                                         widget=forms.TextInput(attrs={'placeholder': "Introduce el precio de campaña"}),
                                         error_messages={'invalid': 'ERROR: Valor NO flotante introducido.'})
    ListaMediosEmision = forms.CharField( max_length=100,
                                          label="Lista de medios de emisión de la Campaña", 
                                          widget=forms.TextInput(attrs={'placeholder': "Introduce los medios de emisión de la campaña"}))
    FechaIni_CampPub = forms.DateField( label="Fecha de Inicio de la Campaña Publitaria (en formato YYYY-MM-DD)",
                                        widget=forms.TextInput(attrs={'placeholder':  "Introduce fecha inicio de campaña"}),
                                        error_messages={'invalid': 'ERROR: Formato de fecha incorrecta. Recuerda que es "YYYY-MM-DD".'})
    FechaFin_CampPub = forms.DateField( label="Fecha de Fin de la Campaña Publitaria (en formato YYYY-MM-DD)",
                                        widget=forms.TextInput(attrs={'placeholder':  "Introduce fecha fin de campaña"}),
                                        error_messages={'invalid': 'ERROR: Formato de fecha incorrecta. Recuerda que es "YYYY-MM-DD".'})
    
    # redefinición de un método para comprobación de formato correcto de un atributo del form
    def clean_IdCampaña(self):
        IdCampaña_clean = self.cleaned_data['IdCampaña']
        patron = re.compile("CP-[1-9][0-9]*")
        if patron.fullmatch(str(IdCampaña_clean)) == None:
            raise ValidationError("ERROR: Formato de IdCampaña incorrecto. Recuerda el formato: 'CP-x', siendo x número natural")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return IdCampaña_clean

class OfertaProductosForm(forms.Form):
    IdOfertaProd = forms.CharField( max_length=10,
                                    label="Identificador de la Oferta de Productos", 
                                    widget=forms.TextInput(attrs={'placeholder': "Introduce identificador de oferta"}))
    Nombre_OferProd = forms.CharField( max_length=40,
                                       label="Nombre de la Oferta", 
                                       widget=forms.TextInput(attrs={'placeholder': "Introduce nombre de oferta"}))
    ListaProductos = forms.CharField( max_length=100,
                                      label="Lista de productos ofertados", 
                                      widget=forms.TextInput(attrs={'placeholder': "Introduce los medios de emisión de la campaña"}))
    Precio_OferProd = forms.DecimalField( max_digits=10, decimal_places=2,
                                         label="Precio de la Oferta (en euros, €)", 
                                         widget=forms.TextInput(attrs={'placeholder': "Introduce el precio de campaña"}),
                                         error_messages={'invalid': 'ERROR: Valor NO flotante introducido.'})
    FechaIni_OferProd = forms.DateField( label="Fecha de Inicio de la Oferta de productos (en formato YYYY-MM-DD)",
                                         widget=forms.TextInput(attrs={'placeholder':  "Introduce fecha inicio de oferta"}),
                                         error_messages={'invalid': 'ERROR: Formato de fecha incorrecta. Recuerda que es "YYYY-MM-DD".'})
    FechaFin_OferProd = forms.DateField( label="Fecha de Fin de la Oferta de productos (en formato YYYY-MM-DD)",
                                         widget=forms.TextInput(attrs={'placeholder':  "Introduce fecha fin de oferta"}),
                                         error_messages={'invalid': 'ERROR: Formato de fecha incorrecta. Recuerda que es "YYYY-MM-DD".'})

    # redefinición de un método para comprobación de formato correcto de un atributo del form
    def clean_IdOfertaProd(self):
        IdOfertaProd_clean = self.cleaned_data['IdOfertaProd']
        patron = re.compile("OP-[1-9][0-9]*")
        if patron.fullmatch(str(IdOfertaProd_clean)) == None: # Si no hay match entre la expr reg y el ID...
            raise ValidationError("ERROR: Formato de IdCampaña incorrecto. Recuerda el formato: 'OP-x', siendo x número natural")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return IdOfertaProd_clean

class pkCampañaPublicitariaForm(forms.Form):
    # Se redefine el constructor, para poder actualizar el formulario al borrar una
    # campaña, en el momento de renderizar la página pasando un objeto nuevo por constructor
    def __init__(self, *args, **kwargs):
        super(pkCampañaPublicitariaForm, self).__init__(*args, **kwargs)

        try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:
                cursor.execute("SELECT IdCampaña, Nombre_CampPub FROM CampañaPublicitaria")
                # Separo la parte primera de la PK, (CP-), en el primer valor de cada "2-upla" que voy añadiendo
                # a las opciones del RadioSelect, para que luego aplicando ordenado por esa componente, obtenga tuplas en orden según número del ID
                # y no como orden lexicográfico (OP-1 , OP-10, OP-2) sino numéricamente ascendente (OP-1 , OP-2, OP-10)
                pk_camp_pubs = [ ( int (str(fila[0]).split("CP-")[1]) , str(fila[0]) + " ("+str(fila[1])+")") for fila in cursor.fetchall()]
                pk_camp_pubs_sort = sorted(pk_camp_pubs, key=itemgetter(0)) # se ordena según el primer item del par (el codigo numerico entero en realidad)
        except:
            pk_camp_pubs_sort = [('', 'No hay Campañas Publicitarias disponibles en la BD. Vuelva atrás para continuar.')]
        
        # Aun no habiendo fallado las sentencias contra la base de datos pero no habiendo ninguna tupla:
        if len(pk_camp_pubs_sort) == 0:
            pk_camp_pubs_sort = [('', 'No hay Campañas Publicitarias disponibles en la BD. Vuelva atrás para continuar.')]
        
        self.fields['ListaCampañaPublicitarias'] = forms.ChoiceField(  
                    label="Elija una Campaña Publicitaria de la lista actual de campañas para realizar la operación",
                    widget=forms.RadioSelect,
                    choices=pk_camp_pubs_sort
                )
   

class pkOfertaProductosForm(forms.Form):
    # Se redefine el constructor, para poder actualizar el formulario al borrar una
    # oferta, en el momento de renderizar la página pasando un objeto nuevo por constructor
    def __init__(self, *args, **kwargs):
        super(pkOfertaProductosForm, self).__init__(*args, **kwargs)

        try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:
                cursor.execute("SELECT IdOfertaProd, Nombre_OferProd FROM OfertaProductos")
                # Separo la parte primera de la PK, (OP-), en el primer valor de cada "2-upla" que voy añadiendo
                # a las opciones del RadioSelect, para que luego aplicando ordenado por esa componente, obtenga tuplas en orden según número del ID
                # y no como orden lexicográfico (OP-1 , OP-10, OP-2) sino numéricamente ascendente (OP-1 , OP-2, OP-10)
                pk_ofer_prods = [ ( int (str(fila[0]).split("OP-")[1]) , str(fila[0]) + " ("+str(fila[1])+")") for fila in cursor.fetchall()]
                # se ordena según el primer item del par (el codigo numerico entero en realidad)
                pk_ofer_prods_sort = sorted(pk_ofer_prods, key=itemgetter(0))
        except:
            pk_ofer_prods_sort = [('', 'No hay Ofertas de Productos disponibles en la BD. Vuelva atrás para continuar.')]

        # Aun no habiendo fallado las sentencias contra la base de datos pero no habiendo ninguna tupla:
        if len(pk_ofer_prods_sort) == 0:
            pk_ofer_prods_sort = [('', 'No hay Ofertas de Productos disponibles en la BD. Vuelva atrás para continuar.')]

        self.fields['ListaOfertaProductos'] = forms.ChoiceField(  
                    label="Elija una Oferta de Productos de la lista actual de ofertas para realizar la operación",
                    widget=forms.RadioSelect,
                    choices=pk_ofer_prods_sort
                )

# Para crear un Form donde no aparezcan las ofertas que ya están promocionadas (escogidas previamente) en la campaña actual a dar de alta
class pkOfertaProductosNoPromocionadosForm(forms.Form):
    # Se redefine el constructor, para poder actualizar el formulario al borrar una
    # oferta, en el momento de renderizar la página pasando un objeto nuevo por constructor
    def __init__(self, IdCampaña, *args, **kwargs):
        super(pkOfertaProductosNoPromocionadosForm, self).__init__(*args, **kwargs)

        try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:
                cursor.execute( f"""SELECT IdOfertaProd, Nombre_OferProd FROM OfertaProductos""")
                # Separo la parte primera de la PK, (OP-), en el primer valor de cada "2-upla" que voy añadiendo
                # a las opciones del RadioSelect, para que luego aplicando ordenado por esa componente,
                #  obtenga tuplas en orden según número del ID
                pk_ofer_prods_all = [ ( int (str(fila[0]).split("OP-")[1]) , str(fila[0]) + " ("+str(fila[1])+")") for fila in cursor.fetchall()]

                cursor.execute( f"""SELECT IdOfertaProd FROM Promociona WHERE IdCampaña = '{IdCampaña}'""")
                # Igual que antes pero ahora para seleccionar las ofertas que ya están siendo promocionados por la Campaña actual
                # (ya han sido previamente seleccionadas en el menú)
                pk_ofer_prods_en_promocion_campaña = [ int (str(fila[0]).split("OP-")[1]) for fila in cursor.fetchall()]

                # Me quedo con la diferencia de las 2 listas anteriores, que será lo que se muestre para poder escoger lo restante:
                pk_ofer_prods = [x for x in pk_ofer_prods_all if x[0] not in pk_ofer_prods_en_promocion_campaña]
                # se ordena según el primer item del par (el codigo numerico entero en realidad)
                pk_ofer_prods_sort = sorted(pk_ofer_prods, key=itemgetter(0)) 
        except:
            pk_ofer_prods_sort = [('', 'No hay Ofertas de Productos disponibles en la BD. Vuelva atrás para continuar.')]

        # Aun no habiendo fallado las sentencias contra la base de datos pero no habiendo ninguna tupla:
        if len(pk_ofer_prods_sort) == 0:
            pk_ofer_prods_sort = [('', 'No hay Ofertas de Productos disponibles en la BD. Vuelva atrás para continuar.')]

        self.fields['ListaOfertaProductos'] = forms.ChoiceField(  
                    label="Elija una Oferta de Productos de la lista actual de ofertas para realizar la operación",
                    widget=forms.RadioSelect,
                    choices=pk_ofer_prods_sort
                )