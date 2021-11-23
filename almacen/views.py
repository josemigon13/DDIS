from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls.base import is_valid_path
from almacen.models import Almacen
from almacen.models import LoteProductosAlmacena

# Create your views here.

def menu_almacen(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()
        if 'alta-lote-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("/almacen/alta_of_prod")
        elif 'baja-lote-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("/almacen/baja_of_prod")
        elif 'listar-lotes-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("/almacen/consular_of_prod")
        elif 'alta-almacen-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("/almacen/alta_camp_pub")
        elif 'baja-almacen-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("/almacen/baja_camp_pub")
        elif 'listar-almacenes-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("/almacen/consultar_camp_pub")
    return render(request,"menu_almacen.html")

def alta_lote(request):
    return render(request,"alta_lote.html")

def baja_lote(request):
    return render(request,"baja_lote.html")

def listar_lotes(request):
    return render(request,"listar_lotes.html")

def alta_almacen(request):
    return render(request,"alta_almacen.html")

def baja_almacen(request):
    return render(request,"baja_almacen.html")

def listar_almacenes(request):
    return render(request,"listar_almacenes.html")
