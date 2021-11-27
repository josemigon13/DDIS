from django.forms import ModelForm
from .models import *

class AlmacenForm( ModelForm ):
    class Meta:
        model = Almacen
        fields = '__all__'
        
class LoteProductosAlmacenaForm( ModelForm ):
    class Meta:
        model = LoteProductos
        fields = '__all__'

class pkAlmacenForm( ModelForm ):
    class Meta:
        model = Almacen
        fields = ['IdAlmacen']
        
class pkLoteProductosAlmacenaForm( ModelForm ):
    class Meta:
        model = LoteProductos
        fields = ['IdLote']