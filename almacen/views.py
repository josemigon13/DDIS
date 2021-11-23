from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.base import is_valid_path
from .models import *
from .forms import *

# Create your views here.

def menu_almacen(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()
        if 'alta-lote-btn' in keys_request_POST:
            return redirect('alta_lote')
        elif 'baja-lote-btn' in keys_request_POST:
            return redirect('baja_lote')
        elif 'listar-lotes-btn' in keys_request_POST:
            return redirect('listar_lotes')
        elif 'alta-almacen-btn' in keys_request_POST:
            return redirect('alta_almacen')
        elif 'baja-almacen-btn' in keys_request_POST:
            return redirect('baja_almacen')
        elif 'listar-almacenes-btn' in keys_request_POST:
            return redirect('listar_almacenes')
    return render(request,"menu_almacen.html")

def alta_lote(request):
    form = LoteProductosAlmacenaForm()
    if request.method == 'POST' :
        form = LoteProductosAlmacenaForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('menu_almacen')
    return render(request,"alta_lote.html",{'form':form})

def baja_lote(request):
    return render(request,"baja_lote.html")

def listar_lotes(request):
    lotes = LoteProductosAlmacena.objects.all()
    return render(request,"listar_lotes.html",{'lotes': lotes})

def alta_almacen(request):
    form = AlmacenForm()
    if request.method == 'POST' :
        form = AlmacenForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('menu_almacen')
        else:
            error_message = "ERROR en los campos a rellenar del lote"
            return render(request,"alta_almacen.html", {"form": form, "error_message": error_message})
    return render(request,"alta_almacen.html",{'form':form})

def baja_almacen(request):
    return render(request,"baja_almacen.html")

def listar_almacenes(request):
    almacenes = Almacen.objects.all()
    return render(request,"listar_almacenes.html",{'almacenes':almacenes})
