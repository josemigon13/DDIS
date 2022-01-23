from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from login_menu_pral.views import Conexion_BD
from operator import itemgetter
import cx_Oracle
import re

# Método que recupera los mensajes del DBMS

def getDBMS(cursor):
    statusVar = cursor.var(cx_Oracle.NUMBER)
    lineVar = cursor.var(cx_Oracle.STRING)
    while True:
        cursor.callproc("dbms_output.get_line", (lineVar, statusVar))
        if statusVar.getvalue() != 0:
            break
        message = lineVar.getvalue()
    return message

# Create your views here.
def menu_logistica(request):
	if request.method == 'POST':
		keys_request_POST = request.POST.keys()
		if 'alta-pedido-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/logistica/alta_pedido")
		elif 'baja-pedido-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/logistica/baja_pedido")
		elif 'consultar-pedido-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/logistica/consultar_pedido")
		elif 'alta-proveedor-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/logistica/alta_proveedor")
		elif 'baja-proveedor-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/logistica/baja_proveedor")
		elif 'consultar-proveedor-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/logistica/consultar_proveedor")
		elif 'consultar-tablas-logistica-btn' in keys_request_POST:
			return consultar_tablas_logistica(request)
	return render(request,"menu_logistica_consultar_tablas.html")

def alta_proveedor(request):
	if request.method == 'POST':
		form = ProveedorForm(request.POST)
		
		if form.is_valid():
			NumProveedor = form.cleaned_data["NumProveedor"]
			Nombre_Prov = form.cleaned_data["Nombre_Prov"]
			DireccionWeb_Prov = form.cleaned_data["DireccionWeb_Prov"]
			Tlf_Prov = form.cleaned_data["Tlf_Prov"]

			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					cursor.execute(	f"""INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
										VALUES ('{str(NumProveedor)}', '{str(Nombre_Prov)}',
										'{str(DireccionWeb_Prov)}', '{str(Tlf_Prov)}')""")
					cursor.execute("COMMIT") # Para hacer efectiva la inserción

				return HttpResponseRedirect("/menu/logistica/")
			except cx_Oracle.DatabaseError as e:
				# mensaje de error genérico por si no es ninguno de por restricción de CP o control por check de fechas
				error_message="ERROR en la inserción a la Base de Datos de la información del proveedor. "

				error, = e.args # obtengo el primer argumento del error
				if error.code == 1: # ORA-00001: restricción única violada # Claves Candidatas
					error_message += "Identificador de proveedor ya existentes."

				return render(request,"alta_proveedor.html", {"form": form, "error_message": error_message})
		else:
			error_message="ERROR en los campos a rellenar de la proveedor"
			return render(request,"alta_proveedor.html", {"form": form, "error_message": error_message})

	# si no se ha hecho un post, estará el formulario vacío para rellenarlo
	return render(request,"alta_proveedor.html", {"form":ProveedorForm()})


def consultar_tablas_logistica(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			proveedores, pedidos = [], [] # inicializar a listas vacías, por si están vacías las tablas en la BD

			# Obtención en lista de todos los atributos de la tabla Proveedor, para representarla como tabla en html
			cursor.execute("SELECT * FROM Proveedor")  # podría ponerse SELECT * FROM Proveedor ORDER BY NumProveedor y ahorrarse lo siguiente
			proveedores = [ ( int(fila[0]), 
							  {'NumProveedor':fila[0], 'Nombre_Prov':fila[1],
							  'DireccionWeb_Prov':fila[2], 'Tlf_Prov':fila[3]} ) 
							for fila in  cursor.fetchall() ]
			# se ordena según el primer item del par (el codigo numerico entero NumProveedor)
			proveedores_sort = sorted(proveedores, key=itemgetter(0))
			# El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
			# 2º item de cada par de la lista anterior (se añadio el 1er del par para la ordenacion)
			proveedores = [ proveedores_sort[i][1] for i in range(0,len(proveedores_sort))]
			
			# Obtención en lista de todos los atributos de la tabla Pedido, para su representación como tabla en html
			cursor.execute("SELECT * FROM Pedido")  # análogo a lo anterior
			pedidos = [ ( int(fila[0]), 
						  {'NumPedido':fila[0], 'NumProveedor':fila[1], 'IdAlmacen':fila[2], 'Articulos':fila[3],
						  'Fecha_Ped':fila[4], 'Precio_Ped':fila[5]} )
						for fila in  cursor.fetchall() ]
			# se ordena según el primer item del par (el codigo numerico entero NumPedido)
			pedidos_sort = sorted(pedidos, key=itemgetter(0))
			# El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
			# 2º item de cada par de la lista anterior (se añadio el 1er del par para la ordenacion)
			pedidos = [ pedidos_sort[i][1] for i in range(0,len(pedidos_sort))]
					
		tablas_vacias = (len(proveedores) == 0 and len(pedidos) == 0)

		return render( request, "menu_logistica_consultar_tablas.html", 
						{	'incluir_mostrar_tablas':True, 'proveedores':proveedores, 'pedidos':pedidos, 
							'tablas_vacias':tablas_vacias    })
	except:
		error_message_mostrar_tabs="ERROR: Las tablas no se han podido mostrar."
		return render( request, "menu_logistica_consultar_tablas.html", {"error_message_mostrar_tabs": error_message_mostrar_tabs})



def baja_proveedor(request):
	if request.method == 'POST':
		form = pkProveedorForm(request.POST)
		if form.is_valid():
			NumProveedor = str(form.cleaned_data["NumProveedor"])
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# para asegurar que se hacen todas las eliminaciones o ninguna
					cursor.execute("SAVEPOINT save_previa_baja_proveedor") 
					
					cursor.execute(f"""SELECT * FROM Proveedor WHERE NumProveedor = '{NumProveedor}'""")
					existe_proveedor = cursor.fetchone()
                    # Se comprueba si el proveedor escogido a borrar está en la base de datos
					if not existe_proveedor:
						raise Exception() # directos al flujo de excepcion para mandar mensaje de no haber podido eliminar

					# Elimino el Informe asociado que tiene referencia al proveedor si lo hay, 
					# y luego al padre (en InformeCuentas)
					cursor.execute(f"SELECT * FROM InformeProveedor WHERE NumProveedor = '{NumProveedor}'")
					tupla_InformeProveedor = cursor.fetchone()

					# si sí había tupla en InformeProveedor asociado (esto es, si no es "None")
					if tupla_InformeProveedor: 
						IdInforme = tupla_InformeProveedor[0]
						cursor.execute(f"DELETE FROM InformeProveedor WHERE IdInforme = '{IdInforme}'")
						cursor.execute(f"DELETE FROM InformeCuentas WHERE IdInforme = '{IdInforme}'")
						
					# Elimino primero las tuplas de la tabla Pedido donde aparece NumProveedor (clave externa),
					# antes de borrarla de la tabla de Proveedor
					cursor.execute(f"DELETE FROM Pedido WHERE NumProveedor = '{NumProveedor}'")
					cursor.execute(f"DELETE FROM Proveedor WHERE NumProveedor = '{NumProveedor}'")

					cursor.execute("COMMIT") # para hacer efectivas las eliminaciones en tablas
				success_message=f"""Eliminado con éxito el proveedor con identificador {NumProveedor} 
									y sus relaciones con pedidos asociados"""
				return render(request,"baja_proveedor.html", {'form': pkProveedorForm(),"success_message": success_message	})
			except:
				# Deshacemos las posibles eliminaciones ("cancelamos la operación de forma lógica") 
				# en las tablas con rollback si se produce cualquier excepción en las sentencias delete SQL
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					cursor.execute("ROLLBACK TO SAVEPOINT save_previa_baja_proveedor")
				error_message=f"ERROR al tratar de eliminar el Proveedor con identificador {NumProveedor}"
				return render(request,"baja_proveedor.html", {'form':form, "error_message": error_message})

	return render(request,"baja_proveedor.html",{'form': pkProveedorForm()})


def consultar_proveedor(request):
	if request.method == 'POST':
		form = pkProveedorForm(request.POST)
		if form.is_valid():
		
			NumProveedor = form.cleaned_data["NumProveedor"]
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Obtención de todos los atributos de la tupla de la tabla Proveedor con identificador NumProveedor
					cursor.execute(f"SELECT * FROM Proveedor WHERE NumProveedor = '{str(NumProveedor)}'")
					tupla_proveedor =  cursor.fetchone() 
					proveedor_seleccionado = {	'NumProveedor':tupla_proveedor[0],
												'Nombre_Prov':tupla_proveedor[1],
												'DireccionWeb_Prov':tupla_proveedor[2],
												'Tlf_Prov':tupla_proveedor[3] }

				return render( request, "consultar_proveedor.html", 
							{'form': form, 'incluir_mostrar_tablas':True,'proveedor_seleccionado':proveedor_seleccionado})
			except:
				error_message=f"ERROR al consultar el Proveedor con identificador {str(NumProveedor)}"
				return render(request,"consultar_proveedor.html", {'form':form, "error_message": error_message})

	return render(request,"consultar_proveedor.html",{'form': pkProveedorForm()})

def alta_pedido(request):
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			NumPedido = form.cleaned_data["NumPedido"]
			NumProveedor = form.cleaned_data["NumProveedor"]
			IdAlmacen = form.cleaned_data["IdAlmacen"]
			Articulos = form.cleaned_data["Articulos"]
			Fecha_Ped = form.cleaned_data["Fecha_Ped"]
			Precio_Ped = form.cleaned_data["Precio_Ped"]
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					cursor.execute(	f"""INSERT INTO Pedido (NumPedido, NumProveedor, IdAlmacen,
															Articulos, Fecha_Ped, Precio_Ped)
										VALUES ('{str(NumPedido)}', '{str(NumProveedor)}', '{str(IdAlmacen)}',
												'{str(Articulos)}', TO_DATE('{str(Fecha_Ped)}','yyyy-mm-dd'),
												'{str(Precio_Ped)}')""")
					cursor.execute("COMMIT") # Para hacer efectiva la inserción

				return HttpResponseRedirect("/menu/logistica/") # lo redireccionamos de vuelta al menú
																# de logistica tras el alta de pedido
			except cx_Oracle.DatabaseError as e:
				# mensaje de error genérico por si no es ninguno de por restricción de CP o control por check de Precio_Ped
				error_message="ERROR en la inserción a la Base de Datos de la información del pedido. "

				error, = e.args # obtengo el primer argumento del error
				if error.code == 1: # ORA-00001: restricción única violada # Clave Primaria
					error_message += "Identificador de pedido ya existente."
				elif error.code == 2290:  # Si el error en sí es por el precio erróneo por ORA-02290
										# restricción de control por el CHECK del create table
					error_message = """ERROR - Precio de pedido Incorrecto: debe ser postivo."""


				return render(request,"alta_pedido.html", {"form": form, "error_message": error_message})
		else:
			error_message="ERROR en los campos a rellenar del pedido"
			return render(request,"alta_pedido.html", {"form": form, "error_message": error_message})

	# si no se ha hecho un post, estará el formulario vacío para rellenarlo
	return render(request,"alta_pedido.html", {"form":PedidoForm()})


def baja_pedido(request):
	if request.method == 'POST':
		form = pkPedidoForm(request.POST)
		if form.is_valid():
			NumPedido = form.cleaned_data["NumPedido"]	
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					cursor.execute(f"""SELECT * FROM Pedido WHERE NumPedido='{str(NumPedido)}'""")
					existe_pedido = cursor.fetchone()
					# Se comprueba si el almacén escogido a borrar está en la base de datos
					if not existe_pedido:
							raise Exception() # directos al flujo de excepcion para mandar mensaje de no haber podido eliminar

					cursor.callproc("dbms_output.enable")
					cursor.execute(f"""BEGIN pedido_borrado('{int(NumPedido)}'); END;""")
					success_message = getDBMS(cursor)
					cursor.execute(f"DELETE FROM Pedido WHERE NumPedido = '{str(NumPedido)}'")
					cursor.execute("COMMIT")

				return render(request,"baja_pedido.html",{'form': pkPedidoForm(),'success_message':success_message})
			except:
				error_message="ERROR en el borrado del pedido"
				return render(request,"baja_pedido.html",{'form':form, 'error_message':error_message})
		else:
			error_message="ERROR en el identificador del pedido"
			return render(request,"baja_pedido.html",{'form':form, 'error_message':error_message})

	return render(request,"baja_pedido.html",{'form': pkPedidoForm()})



def consultar_pedido(request):
	if request.method == 'POST':
		form = pkPedidoForm(request.POST)
		if form.is_valid():
			NumPedido = form.cleaned_data["NumPedido"]
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Obtención de todos los atributos de la tupla de la tabla Pedido con identificador NumPedido
					cursor.execute(f"SELECT * FROM Pedido WHERE NumPedido = '{str(NumPedido)}'")
					tupla_pedido =  cursor.fetchone() 
					pedido_seleccionado={ 	'NumPedido':tupla_pedido[0], 'NumProveedor':tupla_pedido[1], 
											'IdAlmacen':tupla_pedido[2], 'Articulos':tupla_pedido[3], 
											'Fecha_Ped':tupla_pedido[4], 'Precio_Ped':tupla_pedido[5] }
											

				return render( request, "consultar_pedido.html", {'form':form, 'incluir_mostrar_tablas':True,
																	'pedido_seleccionado':pedido_seleccionado})
			except:
				error_message=f"ERROR al consultar el Pedido con identificador {str(NumPedido)}"
				return render(request,"consultar_pedido.html", {'form':form, "error_message": error_message})

	return render(request,"consultar_pedido.html",{'form': pkPedidoForm()})
