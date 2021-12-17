from django import forms

class AlmacenForm( forms.Form ):
    IdAlmacen = forms.CharField( 
                label="IdAlmacén",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador del almacén"}))
    Direccion_Alm = forms.CharField( 
                label="Dirección",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la dirección"}))
    Superficie = forms.FloatField( 
                label="Superficie (metros cuadrados)",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la superficie"}))
    FechaIniAlquiler_Alm = forms.DateField(
                label="Fecha de inicio de alquiler (formato YYYY-MM-DD)",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la fecha de inicio de alquiler"}))
    FechaFinAlquiler_Alm = forms.DateField(
                label="Fecha de fin de alquiler (formato YYYY-MM-DD)",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la fecha de fin de alquiler"})
    )

class LoteProductosAlmacenaForm( forms.Form ):
    IdLote = forms.CharField( 
                label="IdLote",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador del lote"}))
    IdAlmacen = forms.CharField( 
                label="IdAlmacén",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador del almacén"}))
    Descripcion_Lote = forms.CharField( 
                label="Descripción",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la descripción del lote"}))
    Unidad = forms.CharField( 
                label="Unidad",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la unidad de almacenamiento del lote"}))
    Cantidad_Lote = forms.IntegerField( 
                label="Cantidad",
                widget=forms.TextInput(attrs={'placeholder': "Introduce la cantidad de unidades"}))
    Coste_Lote = forms.DecimalField( 
                label="Coste",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el coste del lote"}),
                decimal_places=2)

class pkAlmacenForm( forms.Form ):
    IdLote = forms.CharField( 
                label="IdLote",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador del lote"}))
                
class pkLoteProductosAlmacenaForm( forms.Form ):
    IdAlmacen = forms.CharField( 
                label="IdAlmacén",
                widget=forms.TextInput(attrs={'placeholder': "Introduce el identificador del almacén"}))
