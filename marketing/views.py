from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from login_menu_pral.views import Conexion_BD
from operator import itemgetter
import cx_Oracle
import re

##### VARIABLES GLOBALES


IdCampaña_actual = -1 # IdCampaña guardado globalmente de la actual campaña que se está procesando y a la que añadir Ofertas
eleccion_menu_actual = "" # Global para ir indicando, cambiando y consultando qué html de menú se va a mostrar por pantalla
consultar_tablas_marketing_tras_opcion3 = False # Para mostrar tablas de Marketing tras finalizar un pedido (opción 3) 

# Función para obtener el mensaje que en los triggers se introduce en la salida del DBMS
# al haber sentencias "DBMS_OUTPUT.PUT_LINE" en los triggers
def get_message_from_dbms_output_trigger(cursor):
	# le haré enable antes de las sentencias que ejecutan trigger para asegurar
	#cursor.callproc("dbms_output.enable") # para permitir obtener la salida de datos del trigger cuando se hace PUT_LINE
	statusVar = cursor.var(cx_Oracle.NUMBER)
	lineVar = cursor.var(cx_Oracle.STRING)
	message_from_trigger = ""
	while True:
		cursor.callproc("dbms_output.get_line", (lineVar, statusVar))
		if statusVar.getvalue() != 0:
			break
		message_from_trigger += lineVar.getvalue()
	
	return message_from_trigger

# Create your views here.
def menu_marketing(request):
	global eleccion_menu_actual
	eleccion_menu_actual = "menu_maketing_consultar_tablas.html" # Se guarda la página de menú actual

	if request.method == 'POST':
		keys_request_POST = request.POST.keys()
		if 'alta-oferta-prod-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/alta_ofer_prod")
		elif 'baja-oferta-prod-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/baja_ofer_prod")
		elif 'consultar-oferta-prod-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/consultar_ofer_prod")
		elif 'alta-camp-pub-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/alta_camp_pub")
		elif 'baja-camp-pub-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/baja_camp_pub")
		elif 'consultar-camp-pub-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/consultar_camp_pub")
		elif 'consultar-tablas-marketing-btn' in keys_request_POST:
			return consultar_tablas_marketing(request)

	global consultar_tablas_marketing_tras_opcion3
	if consultar_tablas_marketing_tras_opcion3:
		consultar_tablas_marketing_tras_opcion3 = False 
		# la vuelvo a poner a Falso para que no sea el comportamiento normal
		# (solo cuando se activa la opcion 3)
		return consultar_tablas_marketing(request)
	else:
		return render(request,"menu_maketing_consultar_tablas.html")



def alta_camp_pub(request):
	if request.method == 'POST':
		form = CampañaPublicitariaForm(request.POST)
		if form.is_valid():
			IdCampaña = form.cleaned_data["IdCampaña"]
			Nombre_CampPub = form.cleaned_data["Nombre_CampPub"]
			Descripcion_CampPub = form.cleaned_data["Descripcion_CampPub"]
			Precio_CampPub = form.cleaned_data["Precio_CampPub"]
			ListaMediosEmision = form.cleaned_data["ListaMediosEmision"]
			FechaIni_CampPub = form.cleaned_data["FechaIni_CampPub"]
			FechaFin_CampPub = form.cleaned_data["FechaFin_CampPub"]

			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					cursor.execute("SAVEPOINT save_previa_alta_camp_pub")
					cursor.execute(	f"""INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub,
										Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
										VALUES ('{str(IdCampaña)}', '{str(Nombre_CampPub)}', '{str(Descripcion_CampPub)}', 
										'{str(Precio_CampPub)}', '{str(ListaMediosEmision)}', 
							TO_DATE('{FechaIni_CampPub}','yyyy-mm-dd'), TO_DATE('{FechaFin_CampPub}','yyyy-mm-dd'))""")
					# Si se ha insertado correctamente la campaña publicitaria, y habiéndose hecho bien previamente 
					# un punto de guardado (savepoint al que volveremos si se cancela el alta de campaña y así no se 
					# modifica la tabla CampañaPublicitaria ni Promociona en la BD), lo redireccionamos al menú de elección
					# de 4 opciones de alta de de campaña publicitaria. Pero antes de pasar al menú, almacenaremos el valor
					# de la variable "IdCampaña" en una variable global, y así poder recuperar este valor posteriormente
					# cuando añadamos la promoción de ofertas en la campaña.
					# Es así porque en la opción 1 se escoge el (o los) IdOfertaProd que se asociará a la campaña con 
					# IdCampaña que estamos dando de alta (IdCampaña introducido por el usuario en el primer formulario
					# para dar de alta campaña) y se debe recuperar tal dato.
					global IdCampaña_actual
					IdCampaña_actual = str(IdCampaña)
					cursor.execute("SAVEPOINT save_previa_opcion") 
					# Se establece este savepoint después de insertar la campaña publicitaria
					# pero previamente a insertar ofertas de productos a promocionar en dicha campaña
					# (para poder volver a él y eliminar todas las ofertas, en su caso)

				return HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones")
			except cx_Oracle.DatabaseError as e:
				# mensaje de error genérico por si no es ninguno de por restricción de CP o control por check de fechas
				error_message="ERROR en la inserción a la Base de Datos de la información de la campaña publicitaria. "

				error, = e.args # obtengo el primer argumento del error
				if error.code == 1: # ORA-00001: restricción única violada # Clave Primaria
					error_message += "Identificador de campaña ya existente."
				elif error.code == 2290:  	# Si el error en sí es por las fechas erróneas por ORA-02290
											# restricción de control por el CHECK del create table
					error_message = """ERROR - Fechas Incorrectas: la fecha de fin es anterior en el tiempo a la
                                fecha de inicio de la campaña a dar de alta."""

				return render(request,"alta_camp_pub.html", {"form": form, "error_message": error_message})
		else:
			error_message="ERROR en los campos a rellenar de la campaña publicitaira"
			return render(request,"alta_camp_pub.html", {"form": form, "error_message": error_message})

	# si no se ha hecho un post, estará el formulario vacío para rellenarlo
	return render(request,"alta_camp_pub.html", {"form":CampañaPublicitariaForm()})



def opciones_alta_camp_pub(request):
	global eleccion_menu_actual
	eleccion_menu_actual = "menu_opciones_consultar_tablas.html"  # Se guarda la página de menú actual
	if request.method == 'POST':
		keys_request_POST = request.POST.keys()
		if 'opcion1-btn' in keys_request_POST:
			return HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones/uno")
		elif 'opcion2-btn' in keys_request_POST:
			return opcion_2_eliminar_todas_promociones_con_ofer_prods(request)
		elif 'opcion3-btn' in keys_request_POST:
			return opcion_3_cancelar_camp_pub(request)
		elif 'opcion4-btn' in keys_request_POST:
			return opcion_4_finalizar_camp_pub(request)
   
   	# para que se muestre el menú de menu_opciones_consultar_tablas.html 
	# con las tablas siempre visibles para verificar lo que van haciendo
	# las opciones antes de hacer el commit definitivo del alta de campaña en la BD
	return consultar_tablas_marketing(request) 



def opcion_1_aniadir_oferta_prod_promociona(request):
	if request.method == 'POST':
		form = pkOfertaProductosNoPromocionadosForm(IdCampaña_actual, request.POST)
		if form.is_valid():
			# reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			IdOfertaProd = "OP-"+ str(form.cleaned_data["ListaOfertaProductos"])

			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# para permitir obtener la salida de datos del trigger cuando se hace PUT_LINE es necesario activar
					# lo antes de la ejecución de cualquier trigger, para que los put_line de los triggers se recojan
					cursor.callproc("dbms_output.enable")
					cursor.execute(	f"""INSERT INTO Promociona (IdCampaña, IdOfertaProd)
										VALUES ('{IdCampaña_actual}', '{IdOfertaProd}')""")

				# A continuación se redirige al menú con las 4 opciones, ejecutándose en la vista
				# nuevamente la función "opciones_alta_camp_pub" y mostrándose el contenido
				# actual de la BD de Marketing aún sin hacer commmit definitivo
				return HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones")
			except cx_Oracle.DatabaseError as e:
				error_message=f"""ERROR al tratar de añadir la promoción de la Oferta de Productos con identificador
								{str(IdOfertaProd)} a la campaña actual en la Base de Datos.""" # error genérico
				error, = e.args # obtengo el primer argumento del error
				# Si ha saltado el trigger por excepción de fechas erróneas entre intervalos de fechas de ofertas y campañas
				if error.code == 20001: 
					# Recolectamos el valor de salida por el trigger para identificar el mensaje de cómo ha ido la operacion
					# y este es el error particular que cambiamos por el genérico
					with Conexion_BD().get_conexion_BD().cursor() as cursor:
						error_message = get_message_from_dbms_output_trigger(cursor)
						# Por si se acumulan los 2 mensajes diferentes del trigger em el OUTPUT del DBMS
						error_message = error_message.split("XCEPCIÓN")[1] # importante para siempre separar en 2 y coger [1]
						error_message = "EXCEPCIÓN" + error_message # vuelvo a poner el trozo de string que se separó (split)

				return render(request,"opcion1.html", {"form": form, "error_message": error_message})

	# si no se ha hecho un post, estará el formulario vacío para rellenarlo
	return render(request,"opcion1.html", {"form":pkOfertaProductosNoPromocionadosForm(IdCampaña_actual)})

def opcion_2_eliminar_todas_promociones_con_ofer_prods(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			cursor.execute("ROLLBACK TO SAVEPOINT save_previa_opcion") # volvemos al savepoint para aplicar el borrado

		# A continuación se redirige al menú con las 4 opciones, ejecutándose en la vista
		# nuevamente la función "opciones_alta_camp_pub" y mostrándose el contenido
		# actual de la BD de Marketing aún sin hacer commmit definitivo
		return  HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones")
	except:
		error_message="ERROR al eliminar todas las ofertas de producto asociadas por promoción a la campaña"
		return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})


def opcion_3_cancelar_camp_pub(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			# volvemos al savepoint para aplicar la cancelación
			cursor.execute("ROLLBACK TO SAVEPOINT save_previa_alta_camp_pub")

		# A continuación se redirige al menú principal de la aplicación, ejecutándose en la vista
		# ahora la función "menu" y terminar mostrando el contenido de la BD (por el valor True 
		# de la variable global) habiéndose descartado los cambios en el menú de opciones (rollback)
		global consultar_tablas_marketing_tras_opcion3
		consultar_tablas_marketing_tras_opcion3 = True 
		return HttpResponseRedirect("/menu/marketing/") # lo redireccionamos de vuelta al menú de marketing
	except:
		error_message="ERROR al cancelar el alta dela campaña publicitaria"
		return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})

def opcion_4_finalizar_camp_pub(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			cursor.execute(f"SELECT * FROM Promociona WHERE IdCampaña = '{IdCampaña_actual}'")
			promociones_asociadas_IdCampaña_actual= [  fila[0] for fila in  cursor.fetchall()]

			if(len(promociones_asociadas_IdCampaña_actual) == 0):
				# forzamos excepción por intentar violar restricción semántica RS4.3 al intentar dar de alta una 
				# campaña sin ofertas en promoción. Solo podemos asegurar esta restricción por programación así,
				# pues por la lógica de la transacción, al poder añadir y borrar ofertas asociadas al antojo,
				# no podría programarse un trigger de forma eficaz
				raise Exception( """Debe seleccionar como mínimo una oferta de productos que se
									vaya a promocionar en la actual campaña publicitaria a dar de alta.""")

			cursor.execute("COMMIT") # Finalizamos el alta de campaña dejando constancia de forma efectiva 
									 # en la base de datos las inserciones en las tablas Promociona y CampañaPublicitaria 

		return HttpResponseRedirect("/menu/marketing/") # lo redireccionamos de vuelta al menú de marketing
	except Exception as e_warning_RS4_3:
		error_message=f"ERROR al finalizar el alta de la campaña publicitaria. {e_warning_RS4_3.args[0]}"
		return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})
	except cx_Oracle.DatabaseError as e:
		# mensaje de error genérico de la BD por si no es por la restricción semántica RS4.3
		error_message=f"ERROR al finalizar el alta de la campaña publicitaria. {e.args[0]}"
		return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})


def consultar_tablas_marketing(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			camp_pubs, ofertas, promociona = [], [], [] # inicializar a listas vacías, por si están vacías las tablas en la BD

			# Obtención en lista de todos los atributos de la tabla CampañaPublicitaria, para representarla como tabla en html
			cursor.execute("SELECT * FROM CampañaPublicitaria")
			camp_pubs = [  ( int(str(fila[0]).split("-")[1]), 
							{'IdCampaña':fila[0], 'Nombre_CampPub':fila[1], 'Descripcion_CampPub':fila[2],
							'Precio_CampPub':fila[3], 'ListaMediosEmision' :fila[4], 
							'FechaIni_CampPub':fila[5], 'FechaFin_CampPub':fila[6] })  for fila in  cursor.fetchall()]
			# se ordena según el primer item del par (el codigo numerico entero de IdCampaña)
			camp_pubs_sort = sorted(camp_pubs, key=itemgetter(0))
			# El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
			# 2º item de cada par de la lista anterior (se añadio el 1er del par para la ordenacion)
			camp_pubs = [ camp_pubs_sort[i][1] for i in range(0,len(camp_pubs_sort))]
			
			# Obtención en lista de todos los atributos de la tabla OfertaProductos, para su representación como tabla en html
			cursor.execute("SELECT * FROM OfertaProductos")
			ofertas = [ ( int(str(fila[0]).split("-")[1]), 
						{ 	'IdOfertaProd':fila[0], 'Nombre_OferProd':fila[1],
							'ListaProductos':fila[2], 'Precio_OferProd':fila[3],
							'FechaIni_OferProd':fila[4], 'FechaFin_OferProd':fila[5] })  for fila in  cursor.fetchall()]
			 # se ordena según el primer item del par (el codigo numerico entero de IdOfertaProd)
			ofertas_sort = sorted(ofertas, key=itemgetter(0))
			# El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
			# 2º item de cada par de la lista anterior (se añadio el 1er del par para la ordenacion)
			ofertas = [ ofertas_sort[i][1] for i in range(0,len(ofertas_sort))]
			
			# Obtención en lista de todos los atributos de la tabla Promociona -- para su representación como tabla en html
			cursor.execute("SELECT * FROM Promociona")
			promociona = [ ( int(str(fila[0]).split("-")[1]),  int(str(fila[1]).split("-")[1]), 
							{	'IdCampaña':fila[0], 'IdOfertaProd':fila[1] } ) for fila in  cursor.fetchall()]
			# se ordena según el primer item y segundo item del par (el codigo numerico entero  de Campaña y Oferta)
			promociona_sort = sorted(promociona, key=itemgetter(0,1)) 
			# El conjunto de diccionarios ("de tuplas de la tabla") ya ordenados se obtiene, quedándonos con el
			# 3º item de cada 3-upla (en este caso es de 3 y no es un par) de la lista anterior
			# (se añadió el 1er y el 2º item del par para la ordenacion)
			promociona = [ promociona_sort[i][2] for i in range(0,len(promociona_sort))]

		tablas_vacias = (len(camp_pubs) == 0 and len(ofertas) == 0 and len(promociona) == 0)

		# El segundo argumento (eleccion_menu_actual) tendrá la página html del menú correspondiente donde nos
		# encontremos y se muestren justo ahí las tablas a continuación de las opciones del respectivo menú:
		return render( request, eleccion_menu_actual, 
						{	'incluir_mostrar_tablas':True, 'camp_pubs':camp_pubs, 'ofertas':ofertas, 
							'promociona':promociona, 'tablas_vacias':tablas_vacias    })
	except:
		error_message_mostrar_tabs="ERROR: Las tablas no se han podido mostrar."
		return render( request, eleccion_menu_actual, {"error_message_mostrar_tabs": error_message_mostrar_tabs})



def baja_camp_pub(request):
	if request.method == 'POST':
		form = pkCampañaPublicitariaForm(request.POST)
		if form.is_valid():
			# reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			IdCampaña = "CP-"+ str(form.cleaned_data["ListaCampañaPublicitarias"])
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# para asegurar que se hacen todas las eliminaciones o ninguna
					cursor.execute("SAVEPOINT save_previa_baja_camp_pub") 
					
					# Elimino el Informe asociado que tiene referencia a la campaña si lo hay, 
					# y luego al padre (en InformeCuentas)
					cursor.execute(f"SELECT * FROM InformeCampaña WHERE IdCampaña = '{IdCampaña}'")
					tupla_InformeCampaña = cursor.fetchone()

					# si sí había tupla en InformeCampaña asociada (esto es, si no es "None")
					if tupla_InformeCampaña: 
						IdInforme = tupla_InformeCampaña[0]
						cursor.execute(f"DELETE FROM InformeCampaña WHERE IdInforme = '{IdInforme}'")
						cursor.execute(f"DELETE FROM InformeCuentas WHERE IdInforme = '{IdInforme}'")
					
					# Elimino primero las tuplas de la tabla Promociona donde aparece IdCampaña (clave externa),
					# antes de borrarla de la tabla de CampañaPublicitaria
					cursor.execute(f"DELETE FROM Promociona WHERE IdCampaña = '{IdCampaña}'")
					cursor.execute(f"DELETE FROM CampañaPublicitaria WHERE IdCampaña = '{IdCampaña}'")
					cursor.execute("COMMIT") # para hacer efectivas las eliminaciones en tablas
				success_message=f"""Eliminada con éxito la Campaña publicitaria con identificador {IdCampaña} 
								y sus relaciones con Ofertas de Productos promocionadas"""
				return render(request,"baja_camp_pub.html", {	'form':pkCampañaPublicitariaForm(), 
																"success_message": success_message	})
			except:
				# Deshacemos las posibles eliminaciones ("cancelamos la operación de forma lógica") 
				# en las tablas con rollback si se produce cualquier excepción en las sentencias delete SQL
				cursor.execute("ROLLBACK TO SAVEPOINT save_previa_baja_camp_pub")
				error_message=f"ERROR al tratar de eliminar la Campaña publicitaria con identificador {IdCampaña}"
				return render(request,"baja_camp_pub.html", {'form':form, "error_message": error_message})

	return render(request,"baja_camp_pub.html",{'form': pkCampañaPublicitariaForm()})


def consultar_camp_pub(request):
	if request.method == 'POST':
		form = pkCampañaPublicitariaForm(request.POST)
		if form.is_valid():
			# reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			IdCampaña = "CP-"+ str(form.cleaned_data["ListaCampañaPublicitarias"])
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Obtención de todos los atributos de la tupla de la tabla CampañaPublicitaria con identificador IdCampaña
					cursor.execute(f"SELECT * FROM CampañaPublicitaria WHERE IdCampaña = '{IdCampaña}'")
					tupla_camp_pub =  cursor.fetchone() 
					camp_pub_seleccionada = {	'IdCampaña':tupla_camp_pub[0], 'Nombre_CampPub':tupla_camp_pub[1],
												'Descripcion_CampPub':tupla_camp_pub[2],
												'Precio_CampPub':tupla_camp_pub[3], 'ListaMediosEmision' :tupla_camp_pub[4], 
												'FechaIni_CampPub':tupla_camp_pub[5], 'FechaFin_CampPub':tupla_camp_pub[6] }
					# Obtención de los Identificadores de OfertaProductos que promociona la campaña
					# No está en la propia tabla CampañaPublicitaria, pero es información necesaria
					# mostrar por ser la lista de ofertas asociadas a una campaña publicitaria
					cursor.execute(f"SELECT * FROM Promociona WHERE IdCampaña = '{IdCampaña}'")
					ids_oferprod_promocionadas = [  fila[1]  for fila in  cursor.fetchall()]

					# Junto todos los ids de la lista anterior en un string enumarado por comas que almaceno en el diccionario 
					# que se pasa para mostrarlo en la tabla html junto a los otros atributos de campaña
					camp_pub_seleccionada['IdOfertaProd_promocionadas'] = ', '.join(ids_oferprod_promocionadas)

				return render( request, "consultar_camp_pub.html", 
							{'form': form, 'incluir_mostrar_tablas':True,'camp_pub_seleccionada':camp_pub_seleccionada})
			except:
				error_message=f"ERROR al consultar la Campaña publicitaria con identificador {str(IdCampaña)}"
				return render(request,"consultar_camp_pub.html", {'form':form, "error_message": error_message})

	return render(request,"consultar_camp_pub.html",{'form': pkCampañaPublicitariaForm()})

def alta_ofer_prod(request):
	if request.method == 'POST':
		form = OfertaProductosForm(request.POST)
		if form.is_valid():
			IdOfertaProd = form.cleaned_data["IdOfertaProd"]
			Nombre_OferProd = form.cleaned_data["Nombre_OferProd"]
			ListaProductos = form.cleaned_data["ListaProductos"]
			Precio_OferProd = form.cleaned_data["Precio_OferProd"]
			FechaIni_OferProd = form.cleaned_data["FechaIni_OferProd"]
			FechaFin_OferProd = form.cleaned_data["FechaFin_OferProd"]

			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					cursor.execute(	f"""INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
																	 Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
										VALUES ('{str(IdOfertaProd)}', '{str(Nombre_OferProd)}', '{str(ListaProductos)}',
												'{str(Precio_OferProd)}', TO_DATE('{str(FechaIni_OferProd)}','yyyy-mm-dd'),
												TO_DATE('{str(FechaFin_OferProd)}','yyyy-mm-dd'))""")
					cursor.execute("COMMIT") # Para hacer efectiva la inserción

				return HttpResponseRedirect("/menu/marketing/") # lo redireccionamos de vuelta al menú
																# de marketing tras el alta de oferta
			except cx_Oracle.DatabaseError as e:
				# mensaje de error genérico por si no es ninguno de por restricción de CP o control por check de fechas
				error_message="ERROR en la inserción a la Base de Datos de la información de la oferta de productos. "

				error, = e.args # obtengo el primer argumento del error
				if error.code == 1: # ORA-00001: restricción única violada # Clave Primaria
					error_message += "Identificador de oferta ya existente."
				elif error.code == 2290:  # Si el error en sí es por las fechas erróneas por ORA-02290
										# restricción de control por el CHECK del create table
					error_message = """ERROR - Fechas Incorrectas: la fecha de fin es anterior en el tiempo a la
                                fecha de inicio de la oferta a dar de alta."""

				return render(request,"alta_ofer_prod.html", {"form": form, "error_message": error_message})
		else:
			error_message="ERROR en los campos a rellenar de la oferta de productos"
			return render(request,"alta_ofer_prod.html", {"form": form, "error_message": error_message})

	# si no se ha hecho un post, estará el formulario vacío para rellenarlo
	return render(request,"alta_ofer_prod.html", {"form":OfertaProductosForm()})


def baja_ofer_prod(request):
	if request.method == 'POST':
		form = pkOfertaProductosForm(request.POST)
		if form.is_valid():
			# reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			IdOfertaProd = "OP-"+ str(form.cleaned_data["ListaOfertaProductos"]) 
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					message_from_trigger = "" # string vacío por si falla algo antes de asignar la variable
					# Elimino primero las tuplas de la tabla Promociona donde aparece IdOfertaProd 
					# (clave externa), antes de borrarla de la tabla de IdOfertaProd
					# 	Savepoint para asegurar que se hacen todas las eliminaciones o ninguna
					cursor.execute("SAVEPOINT save_previa_baja_ofer_prod") 
					cursor.execute(f"DELETE FROM Promociona WHERE IdOfertaProd = '{str(IdOfertaProd)}'")
					# para permitir obtener la salida de datos del trigger cuando se hace PUT_LINE es necesario activar
					# lo antes de la ejecución de cualquier trigger, para que los put_line de los triggers se recojan
					cursor.callproc("dbms_output.enable") 
					cursor.execute(f"DELETE FROM OfertaProductos WHERE IdOfertaProd = '{str(IdOfertaProd)}'")
					
					# Recolectamos el valor de salida por el trigger para identificar el mensaje de cómo ha ido la operacion
					message_from_trigger = get_message_from_dbms_output_trigger(cursor)
					
					# Para barajar la posibilidad de que salte excepción en el trigger por ejecución de sentencias SQL
					#  -- aunque es muy remoto que ocurra
					if "EXCEPCIÓN" in message_from_trigger:
						# Forzamos la excepción en el código, para constatarla en el mensaje de error
						# en la interfaz web debido en consonancia con la excepción del trigger
						raise Exception("Excepción Trigger campañaMinimoUnaOferta")

					# Si todo va bien, se hacen efectivas las eliminaciones en tablas
					cursor.execute("COMMIT")

				# Modificamos el mensaje de aviso si se recibe más de una Campaña afectada, para agrupar y pasarlo a plural
				patron = re.compile("(CP-[1-9][0-9]*)") # busca el patron que esr Entre parentesis y lo guarda
				list_campañas_match = patron.findall(message_from_trigger)
				campañas_match = ', '.join(list_campañas_match)
				if (len(list_campañas_match) != 0):
					if (len(list_campañas_match) == 1): # singular
						message_plural_singular =f"""la campaña identificada por {campañas_match} promociona, se elimina
										  			tal campaña, para evitar tener una campaña"""
					else:							# plural
						message_plural_singular =f"""las campañas identificadas por {campañas_match} promocionan, se eliminan
										  				tales campañas, para evitar tener campañas"""
					message_from_trigger = 	f"""Como se elimina la única oferta de productos que
											{message_plural_singular} sin relación con ninguna oferta."""
				
				success_message=f"""Eliminada con éxito la Oferta de Productos con identificador {str(IdOfertaProd)}
									y sus posibles asociaciones con Campañas Publicitarias que la promocionaran. 
									{message_from_trigger}"""
				return render(request,"baja_ofer_prod.html", {	'form':pkOfertaProductosForm(),
																"success_message": success_message})
			except:
				# Deshacemos las posibles eliminaciones ("cancelamos la operación de forma lógica") 
				# en las tablas con rollback si se produce cualquier excepción en el trigger o
				# o antes pues tablas como Promociona podrían afectarse
				cursor.execute("ROLLBACK TO SAVEPOINT save_previa_baja_ofer_prod")
				error_message=f"""ERROR al tratar de eliminar la Oferta de Productos con identificador
									{str(IdOfertaProd)}. {message_from_trigger}"""
				return render(request,"baja_ofer_prod.html", {'form':form, "error_message": error_message})

	return render(request,"baja_ofer_prod.html",{'form': pkOfertaProductosForm()})


def consultar_ofer_prod(request):
	if request.method == 'POST':
		form = pkOfertaProductosForm(request.POST)
		if form.is_valid():
			# reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			IdOfertaProd =  "OP-"+ str(form.cleaned_data["ListaOfertaProductos"]) 
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Obtención de todos los atributos de la tupla de la tabla CampañaPublicitaria con identificador IdCampaña
					cursor.execute(f"SELECT * FROM OfertaProductos WHERE IdOfertaProd = '{str(IdOfertaProd)}'")
					tupla_ofer_prod =  cursor.fetchone() 
					ofer_prod_seleccionada={'IdOfertaProd':tupla_ofer_prod[0], 'Nombre_OferProd':tupla_ofer_prod[1],
											'ListaProductos':tupla_ofer_prod[2], 'Precio_OferProd' :tupla_ofer_prod[3], 
											'FechaIni_OferProd':tupla_ofer_prod[4], 'FechaFin_OferProd':tupla_ofer_prod[5] }

				return render( request, "consultar_ofer_prod.html", {'form':form, 'incluir_mostrar_tablas':True,
																	'ofer_prod_seleccionada':ofer_prod_seleccionada})
			except:
				error_message=f"ERROR al consultar la Campaña publicitaria con identificador {str(IdOfertaProd)}"
				return render(request,"consultar_ofer_prod.html", {'form':form, "error_message": error_message})

	return render(request,"consultar_ofer_prod.html",{'form': pkOfertaProductosForm()})
