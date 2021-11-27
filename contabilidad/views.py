from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls.base import is_valid_path
from .models import *
from .forms import *

# Create your views here.

def menu_contabilidad(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()

        if 'computar-salario-btn' in keys_request_POST:
            return HttpResponseRedirect('computar_salario')

        elif 'computar-pagoProveedor-btn' in keys_request_POST:
            return HttpResponseRedirect('computar_pagoProveedor')

        elif 'computar-beneficiosPOS-btn' in keys_request_POST:
            return HttpResponseRedirect('computar_beneficiosPOS')

        elif 'computar-impuestos-btn' in keys_request_POST:
            return HttpResponseRedirect('computar_impuestos')

        elif 'computar-costeCampania-btn' in keys_request_POST:
            return HttpResponseRedirect('computar_costeCampania')
        
        elif 'listar-informes-btn' in keys_request_POST:
            return HttpResponseRedirect('listar_informes')

    return render(request,"menu_contabilidad.html")

def computar_salario(request):
    form1 = InformeForm()
    form2 = InformeSalarialForm()
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeSalarialForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            exit = True
            DNIs = list(Contrato.objects.values_list('DNI', flat=True))
            try:
                DNIs.index(form2.cleaned_data)
                DNIs = list(InformeSalarialEmpleado.objects.values_list('DNI', flat=True))
                try:
                    DNIs.index(form2.cleaned_data)
                    IDs = list(InformeSalarialEmpleado.objects.filter(DNI = form2.cleaned_data).values_list('IdInforme', flat=True))
                    Fechas = []
                    for id in IDs:
                        Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_informe'))
                    try:
                        Fechas.index(form1.cleaned_data["Fecha_informe"])
                        exit = False
                    except:
                        error_message = "ERROR: Ya existe un informe salarial en\
                        correspondencia con los datos de entrada"
                        return render( request, "menu_contabilidad.html" , {"error_message": error_message})
                except:
                    exit = False
            except:
                error_message = "ERROR: El DNI proporcionado no identifica a\
                ningún empleado de la BD"
                return render( request, "menu_contabilidad.html" , {"error_message": error_message})
              
            if exit==False :
                form1.save()
                id = form1.cleaned_data["IdInforme"]
                obj = InformeSalarialEmpleado(IdInforme=id, DNI=form2.cleaned_data)
                obj.save()
                return HttpResponseRedirect('menu_contabilidad')
    return render(request,"computar_salario.html",{'form1':form1, 'form2':form2})

def computar_costeCampania(request):
    form1 = InformeForm()
    form2 = InformeCampaniaForm()
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeCampaniaForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            IDsCampanias = list(CampaniaPublicitaria.objects.values_list('IdCampania', flat=True))
            try:
                IDsCampanias.index(form2.cleaned_data)
                form1.save()
                id = form1.cleaned_data["IdInforme"]
                obj = InformeSalarialEmpleado(IdInforme=id, IdCampania=form2.cleaned_data)
                obj.save()
                return HttpResponseRedirect('menu_contabilidad')
            except:
                error_message = "ERROR: No existe la campaña publicitaria proporcionada en la BD"
                return render( request, "menu_contabilidad.html" , {"error_message": error_message})
    return render(request,"computar_costeCampania.html",{'form1':form1, 'form2':form2})

def computar_pagoProveedor(request):
    form1 = InformeForm()
    form2 = InformeProveedorForm()
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeProveedorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            exit = True
            Proveedores = list(Proveedor.objects.values_list('NumProveedor', flat=True))
            try:
                Proveedores.index(form2.cleaned_data)
                Proveedores = list(InformeProveedor.objects.values_list('NumProveedor', flat=True))
                try:
                    Proveedores.index(form2.cleaned_data)
                    IDs = list(InformeProveedor.objects.filter(NumProveedor = form2.cleaned_data).values_list('IdInforme', flat=True))
                    Fechas = []
                    for id in IDs:
                        Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_informe'))
                    try:
                        Fechas.index(form1.cleaned_data["Fecha_informe"])
                        exit = False
                    except:
                        error_message = "ERROR: Ya existe un informe de proveedor en\
                        correspondencia con los datos de entrada"
                        return render( request, "menu_contabilidad.html" , {"error_message": error_message})
                except:
                    exit = False
            except:
                error_message="ERROR: No existe el proveedor proporcionado en la BD"
                return render( request, "menu_contabilidad.html" , {"error_message": error_message})
            
            if exit == False:
                form1.save()
                id = form1.cleaned_data["IdInforme"]
                obj = InformeSalarialEmpleado(IdInforme=id, NumProveedor=form2.cleaned_data)
                obj.save()
                return HttpResponseRedirect('menu_contabilidad')
    return render(request,"computar_pagoProveedor.html",{'form1':form1, 'form2':form2})

def computar_impuestos(request):
    form1 = InformeForm()
    form2 = InformeTributarioForm()
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeTributarioForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            IDs = list(InformeTributario.objects.values_list('IdInforme', flat=True))
            Fechas = []
            for id in IDs:
                Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_informe'))
            try:
                Fechas.index(form1.cleaned_data["Fecha_informe"])
                form1.save()
                id = form1.cleaned_data["IdInforme"]
                obj = InformeSalarialEmpleado(IdInforme=id, importeTributario=form2.cleaned_data)
                obj.save()
                return HttpResponseRedirect('menu_contabilidad')
            except:
                error_message="ERROR: Ya existe un informe tributario para la fecha proporcionada en la BD"
                return render( request, "menu_contabilidad.html" , {"error_message": error_message})
    return render(request,"computar_impuestos.html",{'form1':form1, 'form2':form2})

def computar_beneficiosPOS(request):
    form1 = InformeForm()
    form2 = InformePOSForm()
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformePOSForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            exit = True
            IDs = list(InformePOS.objects.values_list('IdPOS', flat=True))
            try:
                IDs.index(form2.cleaned_data["IdPOS"])
                IDs = list(InformePOS.objects.filter(IdPOS = form2.cleaned_data["IdPOS"]).values_list('IdInforme', flat=True))
                Fechas = []
                for id in IDs:
                    Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_informe'))
                try:
                    Fechas.index(form1.cleaned_data["Fecha_informe"])
                    exit = False
                except:
                    error_message = "ERROR: Ya existe un informe de punto de venta en\
                    correspondencia con los datos de entrada"
                    return render( request, "menu_contabilidad.html" , {"error_message": error_message})
            except:
                exit = False
            
            if exit == False:
                form1.save()
                id = form1.cleaned_data["IdInforme"]
                obj = InformeSalarialEmpleado(IdInforme=id, beneficiosPOS=form2.cleaned_data)
                obj.save()
                return HttpResponseRedirect('menu_contabilidad')
    return render(request,"computar_beneficiosPOS.html",{'form1':form1, 'form2':form2})

def listar_informes(request) : 
    informe_cuentas = InformeCuentas.objects.all()
    informe_salarial = InformeSalarialEmpleado.objects.all()
    informe_tributario = InformeTributario.objects.all()
    informe_POS = InformePOS.objects.all()
    informe_proveedor = InformeProveedor.objects.all()
    informe_campania = InformeCampania.objects.all()
    return render(request,"listar_informes.html",{ 'informe_cuentas':informe_cuentas,
    'informe_salarial':informe_salarial, 'informe_tributario':informe_tributario,
    'informe_POS':informe_POS, 'informe_proveedor':informe_proveedor,
    'informe_campania': informe_campania })