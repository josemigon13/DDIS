from django.forms import ModelForm
from .models import *

class CampaniaPublicitariaForm(ModelForm):
    class Meta:
        model = CampaniaPublicitaria
        fields = '__all__'


class OfertaProductosForm(ModelForm):
    class Meta:
        model = OfertaProductos
        fields = '__all__'
