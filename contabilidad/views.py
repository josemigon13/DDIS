from django.shortcuts import render
from django.http import HttpResponseRedirect
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
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeSalarialForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            exit = True
            DNIs = list(InformeSalarialEmpleado.objects.values_list('DNI', flat=True))
            try:
                DNIs.index(list(InformeSalarialEmpleado.objects.filter(DNI = form2.cleaned_data["DNI"]).values_list('DNI', flat=True))[0])
                IDs = list(InformeSalarialEmpleado.objects.filter(DNI = form2.cleaned_data["DNI"]).values_list('IdInforme', flat=True))
                Fechas = []
                for id in IDs:
                    Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_Informe'))
                try:
                    Fechas.index(form1.cleaned_data["Fecha_Informe"])
                    error_message = "ERROR: Ya existe un informe salarial para el\
                    empleado en la fecha proporcionada en la BD"
                    return render( request, "computar_salario.html" , {'form1':InformeForm(), 'form2':InformeSalarialForm(), 'error_message': error_message}) 
                except:
                    exit = False
            except:
                exit = False
              
            if exit==False :
                obj = InformeCuentas(IdInforme=form1.cleaned_data["IdInforme"], Fecha_Informe=form1.cleaned_data["Fecha_Informe"])
                obj.save()
                obj = InformeSalarialEmpleado(IdInforme=InformeCuentas.objects.get(IdInforme = form1.cleaned_data["IdInforme"]), DNI=form2.cleaned_data["DNI"])
                obj.save()
                return HttpResponseRedirect('../')
    return render(request,"computar_salario.html",{'form1':InformeForm(), 'form2':InformeSalarialForm()})

def computar_costeCampania(request):
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeCampaniaForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            IDsCampanias = list(InformeCampania.objects.values_list('IdCampania', flat=True))
            try:
                IDsCampanias.index(list(InformeCampania.objects.filter(IdCampania = form2.cleaned_data["IdCampania"]).values_list('IdCampania', flat=True))[0])
                error_message = "ERROR: Ya existe un informe para la campaña publicitaria proporcionada en la BD"
                return render( request, "computar_costeCampania.html" , {'form1':InformeForm(), 'form2':InformeCampaniaForm(), 'error_message': error_message})
            except:
                obj = InformeCuentas(IdInforme=form1.cleaned_data["IdInforme"], Fecha_Informe=form1.cleaned_data["Fecha_Informe"])
                obj.save()
                obj = InformeCampania(IdInforme=InformeCuentas.objects.get(IdInforme = form1.cleaned_data["IdInforme"]), IdCampania=form2.cleaned_data["IdCampania"])
                obj.save()
                return HttpResponseRedirect('../')
    return render(request,"computar_costeCampania.html",{'form1':InformeForm(), 'form2':InformeCampaniaForm()})

def computar_pagoProveedor(request):
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeProveedorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            exit = True
            Proveedores = list(InformeProveedor.objects.values_list('NumProveedor', flat=True))
            try:
                Proveedores.index(list(InformeProveedor.objects.filter(NumProveedor = form2.cleaned_data["NumProveedor"]).values_list('NumProveedor', flat=True))[0])
                IDs = list(InformeProveedor.objects.filter(NumProveedor = form2.cleaned_data["NumProveedor"]).values_list('IdInforme', flat=True))
                Fechas = []
                for id in IDs:
                    Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_Informe'))
                try:
                    Fechas.index(form1.cleaned_data["Fecha_Informe"])
                    error_message = "ERROR: Ya existe un informe de proveedor para\
                    la fecha proporcionada en la BD"
                    return render( request, "computar_pagoProveedor.html" , {'form1':InformeForm(), 'form2':InformeProveedorForm(), 'error_message': error_message})
                except:
                    exit = False
            except:
                exit = False
            
            if exit == False:
                obj = InformeCuentas(IdInforme=form1.cleaned_data["IdInforme"], Fecha_Informe=form1.cleaned_data["Fecha_Informe"])
                obj.save()
                obj = InformeProveedor(IdInforme=InformeCuentas.objects.get(IdInforme = form1.cleaned_data["IdInforme"]), NumProveedor=form2.cleaned_data["NumProveedor"])
                obj.save()
                return HttpResponseRedirect('../')
    return render(request,"computar_pagoProveedor.html",{'form1':InformeForm(), 'form2':InformeProveedorForm()})

def computar_impuestos(request):
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformeTributarioForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            IDs = list(InformeTributario.objects.values_list('IdInforme', flat=True))
            Fechas = []
            for id in IDs:
                Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_Informe'))
            try:
                Fechas.index(form1.cleaned_data["Fecha_Informe"])
                error_message="ERROR: Ya existe un informe tributario para la fecha proporcionada en la BD"
                return render( request, "computar_impuestos.html" , {'form1':InformeForm(), 'form2':InformeTributarioForm(), 'error_message': error_message})
            except:
                obj = InformeCuentas(IdInforme=form1.cleaned_data["IdInforme"], Fecha_Informe=form1.cleaned_data["Fecha_Informe"])
                obj.save()
                obj = InformeTributario(IdInforme=InformeCuentas.objects.get(IdInforme = form1.cleaned_data["IdInforme"]), ImporteTributario=form2.cleaned_data["ImporteTributario"])
                obj.save()
                return HttpResponseRedirect('../')
    return render(request,"computar_impuestos.html",{'form1':InformeForm(), 'form2':InformeTributarioForm()})

def computar_beneficiosPOS(request):
    if request.method == 'POST' :
        form1 = InformeForm(request.POST)
        form2 = InformePOSForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            exit = True
            IDs = list(InformePOS.objects.values_list('CodigoPOS', flat=True))
            try:
                IDs.index(form2.cleaned_data["CodigoPOS"])
                IDs = list(InformePOS.objects.filter(CodigoPOS = form2.cleaned_data["CodigoPOS"]).values_list('IdInforme', flat=True))
                Fechas = []
                for id in IDs:
                    Fechas.append(getattr(InformeCuentas.objects.get(IdInforme = id), 'Fecha_Informe'))
                try:
                    Fechas.index(form1.cleaned_data["Fecha_Informe"])
                    error_message = "ERROR: Ya existe un informe para el punto de venta en\
                    la fecha proporcionada en la BD"
                    return render( request, "computar_beneficiosPOS.html" , {'form1':InformeForm(), 'form2':InformePOSForm(), 'error_message': error_message})
                except:
                    exit = False
            except:
                exit = False
            
            if exit == False:
                obj = InformeCuentas(IdInforme=form1.cleaned_data["IdInforme"], Fecha_Informe=form1.cleaned_data["Fecha_Informe"])
                obj.save()
                obj = InformePOS(IdInforme=InformeCuentas.objects.get(IdInforme = form1.cleaned_data["IdInforme"]), BeneficiosPOS=form2.cleaned_data["BeneficiosPOS"], CodigoPOS=form2.cleaned_data["CodigoPOS"])
                obj.save()
                return HttpResponseRedirect('../')
    return render(request,"computar_beneficiosPOS.html",{'form1':InformeForm(), 'form2':InformePOSForm()})

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