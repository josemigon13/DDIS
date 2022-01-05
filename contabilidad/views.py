from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from login_menu_pral.views import Conexion_BD
from operator import itemgetter

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
        elif 'computar-costeCampaña-btn' in keys_request_POST:
            return HttpResponseRedirect('computar_costeCampaña')
        elif 'listar-informes-btn' in keys_request_POST:
            return HttpResponseRedirect('listar_informes')

    return render(request,"menu_contabilidad.html")

def computar_salario(request):
    if request.method == 'POST' :
        form1 = InformeCuentasForm(request.POST)
        form2 = InformeSalarialEmpleadoForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    try:
                        cursor.execute(f"""SELECT IdInforme FROM InformeSalarialEmpleado WHERE DNI='{form2.cleaned_data["DNI"]}'""")
                        IdInforme = []
                        for t in cursor.fetchall():
                            for x in t:
                                IdInforme.append(x)
                        Fecha = []
                        for id in IdInforme:
                            cursor.execute(f"""SELECT Fecha_Informe FROM InformeCuentas WHERE IdInforme='{id}'""")
                            Fecha.append(cursor.fetchall())
                        Fecha_Informe = []
                        for t in Fecha:
                            for x in t:
                                Fecha_Informe.append(x)
                        Fecha = []
                        for t in Fecha_Informe:
                            for x in t:
                                Fecha.append(x.date())
                        if (form1.cleaned_data["Fecha_Informe"] in Fecha):
                            error_message="ERROR: Ya existe un Informe Salarial para el empleado en la fecha proporcionada en la BD"
                            return render(request,"computar_salario.html", {'form1':InformeCuentasForm(), 'form2':InformeSalarialEmpleadoForm(), 'error_message': error_message})
                        else:
                            raise Exception()
                    except:
                        cursor.execute("SAVEPOINT save_previa_trabajador")
                        cursor.execute(f"""INSERT INTO InformeCuentas (IdInforme, Fecha_Informe)
                                        VALUES ('{form1.cleaned_data["IdInforme"]}',
                                        TO_DATE('{form1.cleaned_data["Fecha_Informe"]}','yyyy-mm-dd'))""")
                        try:
                            cursor.execute(f"""INSERT INTO InformeSalarialEmpleado (IdInforme, DNI)
                                            VALUES ('{form1.cleaned_data["IdInforme"]}',
                                            '{form2.cleaned_data["DNI"]}')""")
                            args=(form1.cleaned_data["IdInforme"],)
                            cursor.callproc('inf_salarial',args)
                            return HttpResponseRedirect('../') 
                        except:
                            cursor.execute(f"""ROLLBACK TO SAVEPOINT save_previa_trabajador""")
                            raise Exception()
            except:
                error_message="""ERROR en la inserción en la Base de Datos de la información del Informe Salarial."""
                return render(request,"computar_salario.html", {'form1':InformeCuentasForm(), 'form2':InformeSalarialEmpleadoForm(), 'error_message': error_message})
        else:
            error_message="""ERROR en alguno de los campos a rellenar del Informe Salarial"""
            return render(request,"computar_salario.html", {'form1':InformeCuentasForm(), 'form2':InformeSalarialEmpleadoForm(), 'error_message': error_message}) 
    return render(request,"computar_salario.html",{'form1':InformeCuentasForm(), 'form2':InformeSalarialEmpleadoForm()})

def computar_pagoProveedor(request):
    if request.method == 'POST' :
        form1 = InformeCuentasForm(request.POST)
        form2 = InformeProveedorForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    try:
                        cursor.execute(f"""SELECT IdInforme FROM InformeProveedor WHERE NumProveedor='{form2.cleaned_data["NumProveedor"]}'""")
                        IdInforme = []
                        for t in cursor.fetchall():
                            for x in t:
                                IdInforme.append(x)
                        Fecha = []
                        for id in IdInforme:
                            cursor.execute(f"""SELECT Fecha_Informe FROM InformeCuentas WHERE IdInforme='{id}'""")
                            Fecha.append(cursor.fetchall())
                        Fecha_Informe = []
                        for t in Fecha:
                            for x in t:
                                Fecha_Informe.append(x)
                        Fecha = []
                        for t in Fecha_Informe:
                            for x in t:
                                Fecha.append(x.date())
                        if (form1.cleaned_data["Fecha_Informe"] in Fecha):
                            error_message="ERROR: Ya existe un Informe de Proveedor para el proveedor en la fecha proporcionada en la BD"
                            return render(request,"computar_pagoProveedor.html", {'form1':InformeCuentasForm(), 'form2':InformeProveedorForm(), 'error_message': error_message})
                        else:
                            raise Exception()
                    except:
                        cursor.execute("SAVEPOINT save_previa_pagoProveedor")
                        cursor.execute(f"""INSERT INTO InformeCuentas (IdInforme, Fecha_Informe)
                                        VALUES ('{form1.cleaned_data["IdInforme"]}',
                                        TO_DATE('{form1.cleaned_data["Fecha_Informe"]}','yyyy-mm-dd'))""")
                        try:
                            cursor.execute(f"""INSERT INTO InformeProveedor (IdInforme, NumProveedor)
                                            VALUES ('{form1.cleaned_data["IdInforme"]}',
                                            '{form2.cleaned_data["NumProveedor"]}')""")
                            args=(form1.cleaned_data["IdInforme"],)
                            cursor.callproc('inf_proveedor',args)
                            return HttpResponseRedirect('../')
                        except:
                            cursor.execute(f"""ROLLBACK TO SAVEPOINT save_previa_pagoProveedor""")
                            raise Exception()    
            except:
                error_message="""ERROR en la inserción en la Base de Datos de la información del Informe de Proveedor."""
                return render(request,"computar_pagoProveedor.html", {'form1':InformeCuentasForm(), 'form2':InformeProveedorForm(), 'error_message': error_message})
        else:
            error_message="""ERROR en alguno de los campos a rellenar del Informe de Proveedor"""
            return render(request,"computar_pagoProveedor.html", {'form1':InformeCuentasForm(), 'form2':InformeProveedorForm(), 'error_message': error_message})
    return render(request,"computar_pagoProveedor.html",{'form1':InformeCuentasForm(), 'form2':InformeProveedorForm()})

def computar_costeCampaña(request):
    if request.method == 'POST' :
        form1 = InformeCuentasForm(request.POST)
        form2 = InformeCampañaForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    try:
                        cursor.execute(f"""SELECT IdCampaña FROM InformeCampaña""")
                        IdCampaña = cursor.fetchall()
                        if ((form2.cleaned_data["IdCampaña"],) in IdCampaña):
                            error_message="ERROR: Ya existe un Informe de Campaña para la campaña publicitaria proporcionada en la BD"
                            return render(request,"computar_costeCampaña.html", {'form1':InformeCuentasForm(), 'form2':InformeCampañaForm(), 'error_message': error_message})
                        else:
                            raise Exception()
                    except:
                        cursor.execute(f"""SAVEPOINT save_previa_costeCampaña""")
                        cursor.execute(f"""INSERT INTO InformeCuentas (IdInforme, Fecha_Informe)
                                        VALUES ('{form1.cleaned_data["IdInforme"]}',
                                        TO_DATE('{form1.cleaned_data["Fecha_Informe"]}','yyyy-mm-dd'))""")
                        try:
                            cursor.execute(f"""INSERT INTO InformeCampaña (IdInforme, IdCampaña)
                                            VALUES ('{form1.cleaned_data["IdInforme"]}',
                                            '{form2.cleaned_data["IdCampaña"]}')""")
                            args=(form1.cleaned_data["IdInforme"],)
                            cursor.callproc('inf_campaña',args)
                            return HttpResponseRedirect('../')
                        except:
                            cursor.execute(f"""ROLLBACK TO SAVEPOINT save_previa_costeCampaña""")
                            raise Exception()        
            except:
                error_message="""ERROR en la inserción en la Base de Datos de la información del Informe de Campaña Publicitaria."""
                return render(request,"computar_costeCampaña.html", {'form1':InformeCuentasForm(), 'form2':InformeCampañaForm(), 'error_message': error_message})
        else:
            error_message="ERROR en alguno de los campos a rellenar del Informe de Campaña Publicitaria"
            return render(request,"computar_costeCampaña.html", {'form1':InformeCuentasForm(), 'form2':InformeCampañaForm(), 'error_message': error_message}) 
    return render(request,"computar_costeCampaña.html",{'form1':InformeCuentasForm(), 'form2':InformeCampañaForm()})

def computar_impuestos(request):
    if request.method == 'POST' :
        form1 = InformeCuentasForm(request.POST)
        form2 = InformeTributarioForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    try:
                        cursor.execute(f"""SELECT IdInforme FROM InformeTributario""")
                        IdInforme = []
                        for t in cursor.fetchall():
                            for x in t:
                                IdInforme.append(x)
                        Fecha = []
                        for id in IdInforme:
                            cursor.execute(f"""SELECT Fecha_Informe FROM InformeCuentas WHERE IdInforme='{id}'""")
                            Fecha.append(cursor.fetchall())
                        Fecha_Informe = []
                        for t in Fecha:
                            for x in t:
                                Fecha_Informe.append(x)
                        Fecha = []
                        for t in Fecha_Informe:
                            for x in t:
                                Fecha.append(x.date())
                        if (form1.cleaned_data["Fecha_Informe"] in Fecha):
                            error_message="ERROR: Ya existe un Informe Tributario para la fecha proporcionada en la BD"
                            return render(request,"computar_impuestos.html", {'form1':InformeCuentasForm(), 'form2':InformeTributarioForm(), 'error_message': error_message})
                        else:
                            raise Exception()
                    except:
                        cursor.execute(f"""SAVEPOINT save_previa_impuestos""")
                        cursor.execute(f"""INSERT INTO InformeCuentas (IdInforme, Fecha_Informe)
                                        VALUES ('{form1.cleaned_data["IdInforme"]}',
                                        TO_DATE('{form1.cleaned_data["Fecha_Informe"]}','yyyy-mm-dd'))""")
                        try:
                            cursor.execute(f"""INSERT INTO InformeTributario (IdInforme, ImporteTributario)
                                            VALUES ('{form1.cleaned_data["IdInforme"]}',
                                            '{form2.cleaned_data["ImporteTributario"]}')""")
                            args=(form1.cleaned_data["IdInforme"],)
                            cursor.callproc('inf_TRIB',args)
                            return HttpResponseRedirect('../')
                        except:
                            cursor.execute(f"""ROLLBACK TO SAVEPOINT save_previa_impuestos""")
                            raise Exception()
            except:
                error_message="""ERROR en la inserción en la Base de Datos de la información del Informe Tributario"""
                return render(request,"computar_impuestos.html", {'form1':InformeCuentasForm(), 'form2':InformeTributarioForm(), 'error_message': error_message})
        else:
            error_message="ERROR en alguno de los campos a rellenar del Informe Tributario"
            return render(request,"computar_impuestos.html", {'form1':InformeCuentasForm(), 'form2':InformeTributarioForm(), 'error_message': error_message}) 
    return render(request,"computar_impuestos.html",{'form1':InformeCuentasForm(), 'form2':InformeTributarioForm()})

def computar_beneficiosPOS(request):
    if request.method == 'POST' :
        form1 = InformeCuentasForm(request.POST)
        form2 = InformePOSForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            try:
                with Conexion_BD().get_conexion_BD().cursor() as cursor:
                    try:
                        cursor.execute(f"""SELECT IdInforme FROM InformePOS WHERE CodigoPOS = '{form2.cleaned_data["CodigoPOS"]}'""")
                        IdInforme = []
                        for t in cursor.fetchall():
                            for x in t:
                                IdInforme.append(x)
                        Fecha = []
                        for id in IdInforme:
                            cursor.execute(f"""SELECT Fecha_Informe FROM InformeCuentas WHERE IdInforme='{id}'""")
                            Fecha.append(cursor.fetchall())
                        Fecha_Informe = []
                        for t in Fecha:
                            for x in t:
                                Fecha_Informe.append(x)
                        Fecha = []
                        for t in Fecha_Informe:
                            for x in t:
                                Fecha.append(x.date())
                        if (form1.cleaned_data["Fecha_Informe"] in Fecha):
                            error_message="ERROR: Ya existe un Informe de Punto de Venta para la fecha proporcionada en la BD"
                            return render(request,"computar_beneficiosPOS.html", {'form1':InformeCuentasForm(), 'form2':InformePOSForm(), 'error_message': error_message})
                        else:
                            raise Exception()
                    except:
                        cursor.execute(f"""SAVEPOINT save_previa_pos""")
                        cursor.execute(f"""INSERT INTO InformeCuentas (IdInforme, Fecha_Informe)
                                        VALUES ('{form1.cleaned_data["IdInforme"]}',
                                        TO_DATE('{form1.cleaned_data["Fecha_Informe"]}','yyyy-mm-dd'))""")
                        try:
                            cursor.execute(f"""INSERT INTO InformePOS (IdInforme, BeneficiosPOS, CodigoPOS)
                                            VALUES ('{form1.cleaned_data["IdInforme"]}',
                                            '{form2.cleaned_data["BeneficiosPOS"]}',
                                            '{form2.cleaned_data["CodigoPOS"]}')""")
                            args=(form1.cleaned_data["IdInforme"],)
                            cursor.callproc('inf_pos',args)
                            return HttpResponseRedirect('../')
                        except:
                            cursor.execute(f"""ROLLBACK TO SAVEPOINT save_previa_pos""")
                            raise Exception()    
            except:
                error_message="""ERROR en la inserción en la Base de Datos de la información del Informe de Punto de Venta"""
                return render(request,"computar_beneficiosPOS.html", {'form1':InformeCuentasForm(), 'form2':InformePOSForm(), 'error_message': error_message})
        else:
            error_message="ERROR en alguno de los campos a rellenar del Informe de Punto de Venta"
            return render(request,"computar_salario.html", {'form1':InformeCuentasForm(), 'form2':InformePOSForm(), 'error_message': error_message}) 
    return render(request,"computar_beneficiosPOS.html",{'form1':InformeCuentasForm(), 'form2':InformePOSForm()})

def listar_informes(request):
    try:
        with Conexion_BD().get_conexion_BD().cursor() as cursor:
            inf_cuentas, inf_salarial, inf_POS, inf_campaña, inf_pro, inf_trib = [], [], [], [], [], [] # inicializar como listas vacías, por si están vacías las tablas en la BD

            # Obtención en lista de todos los atributos de la tabla Informe de Cuentas para su representación como tabla en html
            cursor.execute("SELECT * FROM InformeCuentas")
            inf_cuentas = [  ( fila[0], 
                        {'IdInforme':fila[0], 'Fecha_Informe':fila[1] }) for fila in cursor.fetchall()]
            # se ordena según el primer ítem del par (identificador/número de informe)
            inf_cuentas_sorted = sorted(inf_cuentas, key=itemgetter(0))
            # El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
            # 2º ítem de cada par de la lista anterior (se añadió el 1er ítem del par para la ordenación)
            inf_cuentas = [ inf_cuentas_sorted[i][1] for i in range(0,len(inf_cuentas_sorted))]

            # Obtención en lista de todos los atributos de la tabla Informe Salarial para su representación como tabla en html
            cursor.execute("SELECT * FROM InformeSalarialEmpleado")
            inf_salarial = [  ( fila[0], 
                        {'IdInforme':fila[0], 'DNI':fila[1] }) for fila in cursor.fetchall()]
            # se ordena según el primer ítem del par (identificador/número de informe)
            inf_salarial_sorted = sorted(inf_salarial, key=itemgetter(0))
            # El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
            # 2º ítem de cada par de la lista anterior (se añadió el 1er ítem del par para la ordenación)
            inf_salarial = [ inf_salarial_sorted[i][1] for i in range(0,len(inf_salarial_sorted))]

            # Obtención en lista de todos los atributos de la tabla Informe de Campaña para su representación como tabla en html
            cursor.execute("SELECT * FROM InformeCampaña")
            inf_campaña = [  ( fila[0], 
                        {'IdInforme':fila[0], 'IdCampaña':fila[1] }) for fila in cursor.fetchall()]
            # se ordena según el primer ítem del par (identificador/número de informe)
            inf_campaña_sorted = sorted(inf_campaña, key=itemgetter(0))
            # El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
            # 2º ítem de cada par de la lista anterior (se añadió el 1er ítem del par para la ordenación)
            inf_campaña = [ inf_campaña_sorted[i][1] for i in range(0,len(inf_campaña_sorted))]

            # Obtención en lista de todos los atributos de la tabla Informe de Proveedor para su representación como tabla en html
            cursor.execute("SELECT * FROM InformeProveedor")
            inf_pro = [  ( fila[0], 
                    {'IdInforme':fila[0], 'NumProveedor':fila[1] }) for fila in cursor.fetchall()]
            # se ordena según el primer ítem del par (identificador/número de informe)
            inf_pro_sorted = sorted(inf_pro, key=itemgetter(0))
            # El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
            # 2º ítem de cada par de la lista anterior (se añadió el 1er ítem del par para la ordenación)
            inf_pro = [ inf_pro_sorted[i][1] for i in range(0,len(inf_pro_sorted))]

            # Obtención en lista de todos los atributos de la tabla Informe Tributario para su representación como tabla en html
            cursor.execute("SELECT * FROM InformeTributario")
            inf_trib = [  ( fila[0], 
                    {'IdInforme':fila[0], 'ImporteTributario':fila[1] }) for fila in cursor.fetchall()]
            # se ordena según el primer ítem del par (identificador/número de informe)
            inf_trib_sorted = sorted(inf_trib, key=itemgetter(0))
            # El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
            # 2º ítem de cada par de la lista anterior (se añadió el 1er ítem del par para la ordenación)
            inf_trib = [ inf_trib_sorted[i][1] for i in range(0,len(inf_trib_sorted))]

            # Obtención en lista de todos los atributos de la tabla Informe POS para su representación como tabla en html
            cursor.execute("SELECT * FROM InformePOS")
            inf_POS = [  ( fila[0], 
                    {'IdInforme':fila[0], 'BeneficiosPOS':fila[1], 'CodigoPOS':fila[2] }) for fila in cursor.fetchall()]
            # se ordena según el primer ítem del par (identificador/número de informe)
            inf_POS_sorted = sorted(inf_POS, key=itemgetter(0))
            # El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
            # 2º ítem de cada par de la lista anterior (se añadió el 1er ítem del par para la ordenación)
            inf_POS = [ inf_POS_sorted[i][1] for i in range(0,len(inf_POS_sorted))]
        
        tablas_vacias = (len(inf_cuentas) == 0)

        return render( request, "listar_informes.html", 
                        { 'inf_cuentas':inf_cuentas,
                        'inf_salarial':inf_salarial, 'inf_trib':inf_trib,
                        'inf_POS':inf_POS, 'inf_pro':inf_pro,
                        'inf_campaña': inf_campaña,
                        'tablas_vacias':tablas_vacias })
    except:
        error_message_mostrar_tabs="ERROR: Las tablas no se han podido mostrar."
        return render( request, "listar_informes.html", {"error_message_mostrar_tabs": error_message_mostrar_tabs})