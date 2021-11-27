from django.forms import ModelForm, MultipleChoiceField, CheckboxSelectMultiple
from .models import *

class CampaniaPublicitariaForm(ModelForm):
    class Meta:
        model = CampaniaPublicitaria
        fields = '__all__'

class OpcionesOferProdForm(ModelForm):
    # Daba fallo esto de abajo -----vvv
    # opcionesOferProd = list(OfertaProductos.objects.values_list('IdOfertaProd', 'Nombre_OferProd'))
    try:
        opcionesOferProd = list(OfertaProductos.objects.all())
        ListaOfertaProductos = MultipleChoiceField( widget=CheckboxSelectMultiple,
                                                choices=opcionesOferProd   )
    except:
        print("NO hay elementos en la tabla OfertaProductos")

class OfertaProductosForm(ModelForm):
    class Meta:
        model = OfertaProductos
        fields = '__all__'


class pkCampaniaPublicitariaForm(ModelForm):
    class Meta:
        model = CampaniaPublicitaria
        fields = ['IdCampania']
        
class pkOfertaProductosForm(ModelForm):
    class Meta:
        model = OfertaProductos
        fields = ['IdOfertaProd']