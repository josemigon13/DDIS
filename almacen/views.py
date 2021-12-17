from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.base import is_valid_path
from .models import *
from .forms import *
from login_menu_pral.views import conexion_BD
import cx_Oracle

# Create your views here.

def menu_almacen(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()
        if 'alta-lote-btn' in keys_request_POST:
            return HttpResponseRedirect('alta_lote')
        elif 'baja-lote-btn' in keys_request_POST:
            return HttpResponseRedirect('baja_lote')
        elif 'listar-lotes-btn' in keys_request_POST:
            return HttpResponseRedirect('listar_lotes')
        elif 'alta-almacen-btn' in keys_request_POST:
            return HttpResponseRedirect('alta_almacen')
        elif 'baja-almacen-btn' in keys_request_POST:
            return HttpResponseRedirect('baja_almacen')
        elif 'listar-almacenes-btn' in keys_request_POST:
            return HttpResponseRedirect('listar_almacenes')
    return render(request,"menu_almacen.html")

def alta_lote(request):
    form = LoteProductosAlmacenaForm()
    if request.method == 'POST' :
        form = LoteProductosAlmacenaForm( request.POST )
        if form.is_valid():
            IdLote = form.cleaned_data["IdLote"]
            IdAlmacen = form.cleaned_data["IdAlmacen"]
            Descripcion_Lote = form.cleaned_data["Descripcion_Lote"]
            Unidad = form.cleaned_data["Unidad"]
            Cantidad_Lote = form.cleaned_data["Cantidad_Lote"]
            Coste_Lote = form.cleaned_data["Coste_Lote"]
            try:
                with conexion_BD.cursor() as cursor:
                    cursor.callproc("dbms_output.enable")
                    cursor.execute(f"""INSERT INTO LoteProductosAlmacena (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad_Lote, Coste_Lote)
                                    VALUES ({str(IdLote)}, {str(IdAlmacen)}, {str(Descripcion_Lote)}, {str(Unidad)}, {str(Cantidad_Lote)}, {str(Coste_Lote)})""")
                    statusVar = cursor.var(cx_Oracle.NUMBER)
                    lineVar = cursor.var(cx_Oracle.STRING)
                    errorInsert = ''
                    while True:
                        errorInsert += cursor.callproc("dbms_output.get_line", (lineVar, statusVar))
                        if statusVar.getvalue() != 0:
                            break
                return HttpResponseRedirect('/menu_almacen')
            except:
                error_message="ERROR en la inserción a la Base de Datos de la información del lote"
                return render(request,"alta_lote.html",{'form':form, 'error_message':error_message})
        else:
            error_message="ERROR en los campos a rellenar del lote"
            return render(request,"alta_lote.html",{'form':form, 'error_message':error_message})
    return render(request,"alta_lote.html",{'form':form})

def baja_lote(request):
    form = LoteProductosAlmacenaForm()
    if request.method == 'POST' :
        form = LoteProductosAlmacenaForm( request.POST )
        if form.is_valid():
            IdLote = form.cleaned_data["IdLote"]

            try:
                with conexion_BD.cursor() as cursor:
                    cursor.callproc(f"""lote_borrado({str(IdLote)}""")
                    cursor.execute(f"""DELETE FROM LoteProductosAlmacena
                                    WHERE IdLote = '{str(IdLote)}'""")
                return HttpResponseRedirect('/menu_almacen')
            except:
                error_message="ERROR en el borrado del lote"
                return render(request,"baja_lote.html",{'form':form, 'error_message':error_message})
        else:
            error_message="ERROR en el identificador del lote"
            return render(request,"baja_lote.html",{'form':form, 'error_message':error_message})
    return render(request,"baja_lote.html",{'form':form})

def listar_lotes(request):
    try:
        lotes = []
        with conexion_BD.cursor() as cursor:
            cursor.execute("SELECT * FROM LoteProductosAlmacena")
            lotes = [ {'IdLote':fila[0], 'IdAlmacen':fila[1], 'Descripcion_Lote':fila[2], 'Unidad':fila[3], 'Cantidad_Lote':fila[4], 'Coste_Lote':fila[5]} for fila in cursor.fetchall() ]

        tabla_vacia = len(lotes)==0
        return render(request, "listar_lotes.html", {'lotes':lotes, 'tabla_vacia':tabla_vacia})
    except:
        error_message="ERROR. Las tablas no se han podido mostrar"
        return render(request, "menu_almacen.html", {'error_message':error_message})

def alta_almacen(request):
    form = AlmacenForm()
    if request.method == 'POST' :
        form = AlmacenForm( request.POST )
        if form.is_valid():
            IdAlmacen = form.cleaned_data["IdAlmacen"]
            Direccion_Alm = form.cleaned_data["Direccion_Alm"]
            Superficie = form.cleaned_data["Superficie"]
            FechaIniAlquiler_Alm = form.cleaned_data["FechaIniAlquiler_Alm"]
            FechaFinAlquiler_Alm = form.cleaned_data["FechaFinAlquiler_Alm"]

            try:
                with conexion_BD.cursor() as cursor:
                    cursor.callproc("dbms_output.enable")
                    cursor.execute(f"""INSERT INTO LoteProductosAlmacena (IdAlmacen, Direccion_Alm, Superficie, FechaIniAlquiler_Alm, FechaFinAlquiler_Alm)
                                    VALUES ({str(IdAlmacen)}, {str(Direccion_Alm)}, {str(Superficie)}, {str(FechaIniAlquiler_Alm)}, {str(FechaFinAlquiler_Alm)})""")
                    statusVar = cursor.var(cx_Oracle.NUMBER)
                    lineVar = cursor.var(cx_Oracle.STRING)
                    errorInsert = ''
                    while True:
                        errorInsert += cursor.callproc("dbms_output.get_line", (lineVar, statusVar))
                        if statusVar.getvalue() != 0:
                            break
                return HttpResponseRedirect('/menu_almacen')
            except:
                error_message="ERROR en la inserción a la Base de Datos de la información del almacen"
                return render(request,"alta_almacen.html",{'form':form, 'error_message':error_message})
        else:
            error_message="ERROR en los campos a rellenar del almacen"
            return render(request,"alta_almacen.html",{'form':form, 'error_message':error_message})
    return render(request,"alta_almacen.html",{'form':form})

def baja_almacen(request):
    form = pkAlmacenForm()
    if request.method == 'POST' :
        form = pkAlmacenForm( request.POST )
        if form.is_valid():
            IdAlmacen = form.cleaned_data["IdAlmacen"]

            try:
                with conexion_BD.cursor() as cursor:
                    cursor.callproc(f"""almacen_borrado({str(IdAlmacen)}""")
                    cursor.execute(f"""DELETE FROM Almacen
                                    WHERE IdAlmacen = '{str(IdAlmacen)}'""")
                return HttpResponseRedirect('/menu_almacen')
            except:
                error_message="ERROR en el borrado del almacen"
                return render(request,"baja_lote.html",{'form':form, 'error_message':error_message})
        else:
            error_message="ERROR en el identificador del almacen"
            return render(request,"baja_lote.html",{'form':form, 'error_message':error_message})
    return render(request,"baja_lote.html",{'form':form})

def listar_almacenes(request):
    try:
        almacenes = []
        with conexion_BD.cursor() as cursor:
            cursor.execute("SELECT * FROM Almacen")
            almacenes = [ {'IdAlmacen':fila[0], 'Direccion_Alm':fila[1], 'Superficie':fila[2], 'FechaIniAlquiler_Alm':fila[3], 'FechaFinAlquiler_Alm':fila[4]} for fila in cursor.fetchall() ]

        tabla_vacia = len(almacenes)==0
        return render(request, "listar_almacenes.html", {'almacenes':almacenes, 'tabla_vacia':tabla_vacia})
    except:
        error_message="ERROR. Las tablas no se han podido mostrar"
        return render(request, "menu_almacen.html", {'error_message':error_message})
