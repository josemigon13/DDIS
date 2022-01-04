from django.shortcuts import render
from django.http import HttpResponseRedirect
from login_menu_pral.views import Conexion_BD
from .forms import *
from operator import itemgetter

# Create your views here.

def menu_rrhh(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()
        if 'alta-contrato-btn' in keys_request_POST:
            return HttpResponseRedirect('alta_contrato')
        if 'baja-contrato-btn' in keys_request_POST:
            return HttpResponseRedirect("baja_contrato")
        if 'consultar-contrato-btn' in keys_request_POST:
            return HttpResponseRedirect("consultar_contrato")
        if 'alta-oferta-emp-btn' in keys_request_POST:
            return HttpResponseRedirect("alta_oferta_emp")
        if 'baja-oferta-emp-btn' in keys_request_POST:
            return HttpResponseRedirect("baja_oferta_emp")
        
    return render(request,"menu_rrhh.html")

def alta_contrato(request):
    if request.method == 'POST' :
        form = AltaContratoForm(request.POST)
        if form.is_valid():
            DNI = form.cleaned_data["DNI"]
            IDOfertaEmpleo=form.cleaned_data["IDOfertaEmpleo"]
            Nombre_Empleado=form.cleaned_data["Nombre_Empleado"]
            Tlf_Empleado=form.cleaned_data["Tlf_Empleado"]
            NumSegSocial=form.cleaned_data["NumSegSocial"]
            Salario=form.cleaned_data["Salario"]
            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    cursor.execute("SAVEPOINT save_previa_alta_contr")
                    cursor.execute(f"""INSERT INTO Contrato (DNI, IDOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES ('{str(DNI)}', '{str(IDOfertaEmpleo)}', '{str(Nombre_Empleado)}', '{str(Tlf_Empleado)}', '{str(NumSegSocial)}', '{str(Salario)}'""")
                    
                success_message=f"Insertando el contrato con DNI {str(DNI)}"
                return render(request,"alta_contrato.html", {'form':AltaContratoForm(), "success_message": success_message})
            
            except:
                error_message="ERROR en la inserción a la Base de Datos de la información del contrato"
                return render(request,"alta_contrato.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar de contrato"
            return render(request,"alta_contrato.html", {"form": form, "error_message": error_message})
            
    return render(request,"alta_contrato.html", {"form":AltaContratoForm()})



def baja_contrato(request):
        
    if request.method == 'POST' :
        form = BajaContratoForm(request.POST)
        if form.is_valid():
            DNI = form.cleaned_data["DNI"]

            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    cursor.execute(f"DELETE FROM Contrato WHERE DNI = '{str(DNI)}'")
                    cursor.execute("COMMIT")

                success_message=f"Eliminado el contrato con DNI {str(DNI)}"
                return render(request,"baja_contrato.html", {'form':BajaContratoForm(), "success_message": success_message})
            
            except:
                error_message="ERROR en el borrado del contrato"
                return render(request,"baja_contrato.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar de contrato"
            return render(request,"baja_contrato.html", {"form": form, "error_message": error_message})
            
    return render(request,"baja_contrato.html", {"form":BajaContratoForm()})

def consultar_contrato(request):
        
    if request.method == 'POST' :
        form = ConsultarContratoForm(request.POST)
        if form.is_valid():
            DNI = form.cleaned_data["DNI"]

            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    cursor.execute(f"SELECT * FROM Contrato WHERE DNI = '{str(DNI)}'")
                    tupla_contr =  cursor.fetchone() 
                    contr = {	'DNI':tupla_contr[0], 'IDOfertaEmpleado':tupla_contr[1], 'Nombre_Empleado':tupla_contr[2], 'Tlf_Empleado' :tupla_contr[3], 
												'NumSegSocial':tupla_contr[4], 'Salario':tupla_contr[5] }
                    
                    return render( request, "consultar_contrato.html", {'form':form, 'mostrar_tablas':True,
																	'contr':contr})
            
            except:
                error_message="ERROR al consultar el contrato"
                return render(request,"consultar_contrato.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar de contrato"
            return render(request,"consultar_contrato.html", {"form": form, "error_message": error_message})
            
    return render(request,"consultar_contrato.html", {"form":ConsultarContratoForm()})

def alta_oferta_emp(request):
    if request.method == 'POST' :
        form = AltaOfertaForm(request.POST)
        if form.is_valid():
            IDOfertaEmpleo=form.cleaned_data["IDOfertaEmpleo"]
            ListadoEmpleos=form.cleaned_data["ListadoEmpleos"]
            FechaIni_OferEmp=form.cleaned_data["FechaIni_OferEmp"]
            FechaFin_OferEmp=form.cleaned_data["FechaFin_OferEmp"]

            print("IDOfertaEmpleo:", IDOfertaEmpleo)
            print("ListadoEmpleos:", ListadoEmpleos)
            print("FechaIni_OferEmp:", FechaIni_OferEmp)
            print("FechaFin_OferEmp:", FechaFin_OferEmp)

            #try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:
                cursor.execute("SAVEPOINT save_previa_alta_empleo")
                cursor.execute(f"""INSERT INTO OfertaEmpleo (IDOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp) VALUES ('{str(IDOfertaEmpleo)}', '{str(ListadoEmpleos)}', TO_DATE('{FechaIni_OferEmp}','yyyy-mm-dd'), TO_DATE('{FechaFin_OferEmp}','yyyy-mm-dd'))""")
                    
            return HttpResponseRedirect("/menu/rrhh/alta_oferta_emp/")
            
            #except:
                #error_message="ERROR en la inserción a la Base de Datos de la información de la oferta de empleo"
                #return render(request,"alta_oferta_emp.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar sobre la oferta"
            return render(request,"alta_oferta_emp.html", {"form": form, "error_message": error_message})
    return render(request,"alta_oferta_emp.html", {"form":AltaOfertaForm()})

def baja_oferta_emp(request):
        
    if request.method == 'POST' :
        form = BajaOfertaForm(request.POST)
        if form.is_valid():
            IDOfertaEmpleo = form.cleaned_data["IDOfertaEmpleo"]

            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    cursor.execute(f"DELETE FROM OfertaEmpleo WHERE IDOfertaEmpleo = '{str(IDOfertaEmpleo)}'")
                    cursor.execute("COMMIT")

                success_message=f"Eliminado la oferta con ID {str(IDOfertaEmpleo)}"
                return render(request,"baja_oferta_emp.html", {'form':BajaOfertaForm(), "success_message": success_message})
            
            except:
                error_message="ERROR en el borrado de la oferta de empleo"
                return render(request,"baja_oferta_emp.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar de la oferta de empleo"
            return render(request,"baja_oferta_emp.html", {"form": form, "error_message": error_message})
            
    return render(request,"baja_oferta_emp.html", {"form":BajaOfertaForm()})
