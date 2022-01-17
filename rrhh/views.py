from django.shortcuts import render
from django.http import HttpResponseRedirect
from login_menu_pral.views import Conexion_BD
from .forms import *
from operator import itemgetter
import cx_Oracle

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
        if 'mostrar-informacion-btn' in keys_request_POST:
            return HttpResponseRedirect("mostrar_informacion")
            
        
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
                    cursor.execute(f"""INSERT INTO Contrato (DNI, IDOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES ('{str(DNI)}', '{str(IDOfertaEmpleo)}', '{str(Nombre_Empleado)}', '{str(Tlf_Empleado)}', '{str(NumSegSocial)}', '{str(Salario)}')""")
                    cursor.callproc("dbms_output.enable")
                    cursor.execute(f"""BEGIN DNI_contrato('{form.cleaned_data["DNI"]}'); END;""")
                    statusVar = cursor.var(cx_Oracle.NUMBER)
                    lineVar = cursor.var(cx_Oracle.STRING)
                    while True:
                        cursor.callproc("dbms_output.get_line", (lineVar, statusVar))
                        if statusVar.getvalue() != 0:
                            break
                        success_message = lineVar.getvalue()
                    cursor.execute("""COMMIT""")
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
            DNI = form.cleaned_data["ListaContrato"]

            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:

                    cursor.execute(f"SELECT IdInforme FROM InformeSalarialEmpleado WHERE DNI = '{str(DNI)}'")
                    listaID=[]
                    for fila in cursor.fetchall():
                        listaID.append(fila[0])
                    for fila1 in listaID:
                        cursor.execute(f"DELETE FROM InformeSalarialEmpleado WHERE IdInforme = '{str(fila1[0])}'")
                        cursor.execute(f"DELETE FROM InformeCuentas WHERE IdInforme = '{str(fila1[0])}'")
                        
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

            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    cursor.execute("SAVEPOINT save_previa_alta_empleo")
                    cursor.execute(f"""INSERT INTO OfertaEmpleo (IDOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp) VALUES ('{str(IDOfertaEmpleo)}', '{str(ListadoEmpleos)}', TO_DATE('{FechaIni_OferEmp}','yyyy-mm-dd'), TO_DATE('{FechaFin_OferEmp}','yyyy-mm-dd'))""")
                    cursor.callproc("dbms_output.enable")
                    cursor.execute(f"""BEGIN IDOfertaEmpleo_OfertaEmpleo('{form.cleaned_data["IDOfertaEmpleo"]}'); END;""")
                    statusVar = cursor.var(cx_Oracle.NUMBER)
                    lineVar = cursor.var(cx_Oracle.STRING)
                    while True:
                        cursor.callproc("dbms_output.get_line", (lineVar, statusVar))
                        if statusVar.getvalue() != 0:
                            break
                        success_message = lineVar.getvalue()
                    cursor.execute("""COMMIT""")
                    return render(request,"alta_oferta_emp.html", {'form':AltaOfertaForm(), "success_message": success_message})

                    #cursor.execute("COMMIT")    
                
                #return HttpResponseRedirect("/menu/rrhh/alta_oferta_emp/")
            
            except:
                error_message="ERROR en la inserción a la Base de Datos de la información de la oferta de empleo"
                return render(request,"alta_oferta_emp.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar sobre la oferta"
            return render(request,"alta_oferta_emp.html", {"form": form, "error_message": error_message})
    return render(request,"alta_oferta_emp.html", {"form":AltaOfertaForm()})

def baja_oferta_emp(request):
        
    if request.method == 'POST' :
        form = BajaOfertaForm(request.POST)
        if form.is_valid():
            IDOfertaEmpleo = form.cleaned_data["ListaOfertas"]

            #try:
            with Conexion_BD().get_conexion_BD().cursor() as cursor:
                cursor.execute(f"SELECT DNI FROM Contrato WHERE IDOfertaEmpleo = '{str(IDOfertaEmpleo)}'")

                listaDNI=[]
                for fila in cursor.fetchall():
                    listaDNI.append(fila[0])

                
                for d in listaDNI:
                    cursor.execute(f"SELECT IdInforme FROM InformeSalarialEmpleado WHERE DNI = '{str(d[0])}'")
                    listaID=[]
                    for fila1 in cursor.fetchall():
                        listaID.append(fila1[0])

                    for fila2 in listaID:
                        cursor.execute(f"DELETE FROM InformeSalarialEmpleado WHERE IdInforme = '{str(fila2[0])}'")
                        cursor.execute(f"DELETE FROM InformeCuentas WHERE IdInforme = '{str(fila2[0])}'")

                        
                cursor.execute(f"DELETE FROM Contrato WHERE IDOfertaEmpleo = '{str(IDOfertaEmpleo)}'")
                cursor.execute(f"DELETE FROM OfertaEmpleo WHERE IDOfertaEmpleo = '{str(IDOfertaEmpleo)}'")
                cursor.execute("COMMIT")

            success_message=f"Eliminado la oferta con ID {str(IDOfertaEmpleo)}"
            return render(request,"baja_oferta_emp.html", {'form':BajaOfertaForm(), "success_message": success_message})
            
            #except:
            #    error_message="ERROR en el borrado de la oferta de empleo"
            #    return render(request,"baja_oferta_emp.html", {"form": form, "error_message": error_message})
                
        else:
            error_message="ERROR en los campos a rellenar de la oferta de empleo"
            return render(request,"baja_oferta_emp.html", {"form": form, "error_message": error_message})
            
    return render(request,"baja_oferta_emp.html", {"form":BajaOfertaForm()})



def mostrar_informacion(request):
    #try:
    with Conexion_BD().get_conexion_BD().cursor() as cursor:
        Contrato, OfertaEmpleo = [], []

        cursor.execute("SELECT * FROM Contrato")
        Contrato = [ ( fila[0], {'DNI':fila[0], 'IDOfertaEmpleo':fila[1], 'Nombre_Empleado':fila[2], 'Tlf_Empleado':fila[3], 'NumSegSocial':fila[4], 'salario':fila[5] }) for fila in cursor.fetchall()]
        Contrato_sorted = sorted(Contrato, key=itemgetter(0))
        Contrato = [ Contrato_sorted[i][1] for i in range(0,len(Contrato))]

        cursor.execute("SELECT * FROM OfertaEmpleo")
        OfertaEmpleo = [( fila[0],  {'IDOfertaEmpleo':fila[0], 'ListadoEmpleos':fila[1], 'FechaIni_OferEmp':fila[2], 'FechaFin_OferEmp':fila[3]}) for fila in cursor.fetchall()]
        OfertaEmpleo_sorted = sorted(OfertaEmpleo, key=itemgetter(0))
        OfertaEmpleo = [ OfertaEmpleo_sorted[i][1] for i in range(0,len(OfertaEmpleo))]

        tablas_vacias = (len(Contrato) == 0)

        return render( request, "mostrar_informacion.html", { 'Contrato':Contrato, 'OfertaEmpleo':OfertaEmpleo, 'tablas_vacias':tablas_vacias })
        
    #except:
    #    error_message="error en la obtención de los datos."
    #    return render( request, "mostrar_informacion.html", {"error_message": error_message})
