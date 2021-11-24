from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import *
import cx_Oracle

# Create your views here.

def menu_rrhh(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()
            # Obtengo las claves del diccionario request.POST, que por ejemplo tiene el valor:
            # <QueryDict: {'csrfmiddlewaretoken': ['CHNZtCiLbU'], 'alamcen-btn': ['']}> 
            # Me quedo con las claves para coger "almacen-btn", que es la que me interesa 
            # coger (según el boton que pulse y se escoja hacer una acción u otra)
        if 'alta_contrato-btn' in keys_request_POST:
            pass # se pone cuando aun falta por implementar
            # return HttpResponseRedirect("menu/almacen")
        elif 'contabilidad-tablas-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("menu/contabilidad")
        elif 'logistica-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("menu/logistica")
        elif 'marketing-btn' in keys_request_POST:
            return HttpResponseRedirect("marketing")
        elif 'rrhh-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("menu/rrhh")
    
    return render(request,"menu_rrhh.html")
