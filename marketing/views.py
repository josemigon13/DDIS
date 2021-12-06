from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from login_menu_pral.views import Conexion_BD
from operator import itemgetter

##### VARIABLES GLOBALES
IdCampaña_actual = -1 # IdCampaña que se guarda como global de la actual campaña que se va a insertar en la tabla CampañaPublicitaria
eleccion_menu_actual = "" # Global para ir indicando, cambiando y consultando qué html de menú se va a mostrar por pantalla
consultar_tablas_marketing_tras_opciones123 = False

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

	global consultar_tablas_marketing_tras_opciones123
	if consultar_tablas_marketing_tras_opciones123:
		consultar_tablas_marketing_tras_opciones123 = False # la vuelvo a poner a Falso para que no sea el comportamiento normal (solo cuando se activa la opcion 3)
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
					cursor.execute(f"""INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub,
																		Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
									VALUES ('{str(IdCampaña)}', '{str(Nombre_CampPub)}', '{str(Descripcion_CampPub)}', '{str(Precio_CampPub)}', '{str(ListaMediosEmision)}',
											TO_DATE('{FechaIni_CampPub}','yyyy-mm-dd'), TO_DATE('{FechaFin_CampPub}','yyyy-mm-dd'))""")
					# Si se ha insertado correctamente la campaña publicitaria, y habiéndose hecho bien previamente un punto de guardado
					# (savepoint al que volveremos si se cancela el pedido y así no se modifica la tabla CampañaPublicitaria ni Promociona en la BD),
					# lo redireccionamos al menú de elección de 4 opciones de alta de de campaña publicitaria
					# Pero antes de pasar al menú, almacenaremos el valor de la variable "IdCampaña" en una variable global, y así
					# poder recuperar este valor posteriormente cuando añadamos la promoción de la oferta en la campaña.
					# Es así porque en la opción 1 se escoge el (o los) IdOfertaProd que se asociará a la campaña con IdCampaña que estamos dando
					# de alta (IdCampaña introducido por el usuario en el primer formulario para dar de alta campaña y se debe recuperar tal dato.
					global IdCampaña_actual
					IdCampaña_actual = str(IdCampaña)
					print("IdCampaña_actual:", IdCampaña_actual)
					cursor.execute("SAVEPOINT save_previa_opcion") 
					# Se establece este savepoint después de insertar la campaña publicitaria
					# pero previamente a insertar ofertas de productos a promocionar en dicha campaña
					# (para poder volver a él y eliminar todas las ofertas, en su caso)

				return HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones")
			except:
				error_message="ERROR en la inserción a la Base de Datos de la información de la campaña publicitaira"
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
   
   global consultar_tablas_marketing_tras_opciones123
   if consultar_tablas_marketing_tras_opciones123:
      consultar_tablas_marketing_tras_opciones123 = False # la vuelvo a poner a Falso para que no sea el comportamiento normal (solo cuando se activa la opcion 1 o 2)
      return consultar_tablas_marketing(request)
   else:
      return render(request,"menu_opciones_consultar_tablas.html")


def opcion_1_aniadir_oferta_prod_promociona(request):
	if request.method == 'POST':
		form = pkOfertaProductosNoPromocionadosForm(IdCampaña_actual, request.POST)
		if form.is_valid():
			IdOfertaProd = "OP-"+ str(form.cleaned_data["ListaOfertaProductos"]) # reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa

			#try:
			with Conexion_BD().get_conexion_BD().cursor() as cursor:
				print("A", "idOfer:", IdOfertaProd, "idCampAct:", IdCampaña_actual)
				cursor.execute(f"SELECT * FROM CampañaPublicitaria")
				a = cursor.fetchall()
				print("fechall =", a)
				cursor.execute(f"""INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('{IdCampaña_actual}', '{IdOfertaProd}')""")
				print("B")
				# A continuación se redirige al menú con las 4 opciones, ejecutándose en la vista
				# nuevamente la función "opciones_alta_camp_pub" y terminar mostrando el contenido de la BD 
				# (por el valor True de la variable global)
			global consultar_tablas_marketing_tras_opciones123
			consultar_tablas_marketing_tras_opciones123 = True
			return HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones")
			# except:
			# 	error_message="ERROR en las sentencias contra la BD al añadir oferta de producto en la promoción"
			# 	return render(request,"opcion1.html", {"form": form, "error_message": error_message})

	# si no se ha hecho un post, estará el formulario vacío para rellenarlo
	return render(request,"opcion1.html", {"form":pkOfertaProductosForm()})

def opcion_2_eliminar_todas_promociones_con_ofer_prods(request):
	#try:
	with Conexion_BD().get_conexion_BD().cursor() as cursor:
		cursor.execute("ROLLBACK TO SAVEPOINT save_previa_opcion") # volvemos al savepoint para aplicar el borrado

		# A continuación se redirige al menú con las 4 opciones, ejecutándose en la vista
		# nuevamente la función "opciones_alta_camp_pub" y terminar mostrando el contenido de la BD
		# (por el valor True de la variable global)
	global consultar_tablas_marketing_tras_opciones123
	consultar_tablas_marketing_tras_opciones123 = True
	return  HttpResponseRedirect("/menu/marketing/alta_camp_pub/opciones")
	# except:
	# 	error_message="ERROR al eliminar todas las ofertas de producto asociadas por promoción a la campaña"
	# 	return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})


def opcion_3_cancelar_camp_pub(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			cursor.execute("ROLLBACK TO SAVEPOINT save_previa_alta_camp_pub") # volvemos al savepoint para aplicar al cancelación

		# A continuación se redirige al menú principal de la aplicación, ejecutándose en la vista
		# ahora la función "menu" y terminar mostrando el contenido de la BD (por el valor True de la variable global)
		global consultar_tablas_marketing_tras_opciones123
		consultar_tablas_marketing_tras_opciones123 = True 
		return HttpResponseRedirect("/menu/marketing/") # lo redireccionamos de vuelta al menú de marketing
	except:
		error_message="ERROR al cancelar el alta dela campaña publicitaria"
		return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})

def opcion_4_finalizar_camp_pub(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			cursor.execute("COMMIT") # Finalizamos el pedido dejando constancia de forma efectiva en la base de datos
                               # las inserciones en las tablas de Pedido y Detalle-Pedido

		return HttpResponseRedirect("/menu/marketing/") # lo redireccionamos de vuelta al menú de marketing
	except:
		error_message="ERROR al finalizar el alta de la campaña publicitaria"
		return render(request,"menu_opciones_consultar_tablas.html", {"error_message": error_message})


def consultar_tablas_marketing(request):
	try:
		with Conexion_BD().get_conexion_BD().cursor() as cursor:
			camp_pubs, ofertas, promociona = [], [], [] # inicializar como listas vacías, por si están vacías las tablas en la BD

			# Obtención en lista de todos los atributos de la tabla CampañaPublicitaria -- para su representación como tabla en html
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
			
			# Obtención en lista de todos los atributos de la tabla OfertaProductos -- para su representación como tabla en html
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

		tablas_vacias = (len(camp_pubs) == 0 and len(ofertas) == 0 and len(ofertas) == 0)

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
			IdCampaña = "CP-"+ str(form.cleaned_data["ListaCampañaPublicitarias"]) # reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Elimino primero las tuplas de la tabla Promociona donde aparece IdCampaña (clave externa), antes de borrarla de la tabla de CampañaPublicitaria
					cursor.execute(f"DELETE FROM Promociona WHERE IdCampaña = '{IdCampaña}'")
					cursor.execute(f"DELETE FROM CampañaPublicitaria WHERE IdCampaña = '{IdCampaña}'")
					cursor.execute("COMMIT") # para hacer efectivas las eliminaciones en tablas
				success_message=f"Eliminada con éxito la Campaña publicitaria con identificador {IdCampaña} y sus relaciones con Ofertas de Productos promocionadas"
				return render(request,"baja_camp_pub.html", {'form':pkCampañaPublicitariaForm(), "success_message": success_message})
			except:
				error_message=f"ERROR al tratar de eliminar la Campaña publicitaria con identificador {IdCampaña}"
				return render(request,"baja_camp_pub.html", {'form':form, "error_message": error_message})

	return render(request,"baja_camp_pub.html",{'form': pkCampañaPublicitariaForm()})


def consultar_camp_pub(request):
	if request.method == 'POST':
		form = pkCampañaPublicitariaForm(request.POST)
		if form.is_valid():
			IdCampaña = "CP-"+ str(form.cleaned_data["ListaCampañaPublicitarias"]) # reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Obtención de todos los atributos de la tupla de la tabla CampañaPublicitaria con identificador IdCampaña
					cursor.execute(f"SELECT * FROM CampañaPublicitaria WHERE IdCampaña = '{IdCampaña}'")
					tupla_camp_pub =  cursor.fetchone() 
					camp_pub_seleccionada =   {  'IdCampaña':tupla_camp_pub[0], 'Nombre_CampPub':tupla_camp_pub[1], 'Descripcion_CampPub':tupla_camp_pub[2],
									'Precio_CampPub':tupla_camp_pub[3], 'ListaMediosEmision' :tupla_camp_pub[4], 
									'FechaIni_CampPub':tupla_camp_pub[5], 'FechaFin_CampPub':tupla_camp_pub[6] }

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
					cursor.execute("COMMIT") # Para hacer efectivas las inserciones

				return HttpResponseRedirect("/menu/marketing/") # lo redireccionamos de vuelta al menú de marketing tras el alta de oferta # DEPURAR ruta!!
			except:
				error_message="ERROR en la inserción a la Base de Datos de la información de la oferta de productos"
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
			IdOfertaProd = "OP-"+ str(form.cleaned_data["ListaOfertaProductos"]) # reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Elimino primero las tuplas de la tabla Promociona donde aparece IdOfertaProd (clave externa), antes de borrarla de la tabla de IdOfertaProd
					cursor.execute(f"DELETE FROM Promociona WHERE IdOfertaProd = '{str(IdOfertaProd)}'")
					cursor.execute(f"DELETE FROM OfertaProductos WHERE IdOfertaProd = '{str(IdOfertaProd)}'")
					cursor.execute("COMMIT") # para hacer efectivas las eliminaciones en tablas
					# aqui deberia poner un disparador o algo para evitar eliminar la unica ofer prod asociada a una campaña solo, 
					# para que no queden huerfanas las camp pubs y verifiquen la relacion de obligatoiredad con al menos una  !!!!!!!! REVISAR
				
				success_message=f"Eliminada con éxito la Oferta de Productos con identificador {str(IdOfertaProd)} y sus relaciones con Ofertas de Productos promocionadas"
				return render(request,"baja_ofer_prod.html", {'form':pkOfertaProductosForm(), "success_message": success_message})
			except:
				error_message=f"ERROR al tratar de eliminar la Oferta de Productos con identificador {str(IdOfertaProd)}"
				return render(request,"baja_ofer_prod.html", {'form':form, "error_message": error_message})

	return render(request,"baja_ofer_prod.html",{'form': pkOfertaProductosForm()})


def consultar_ofer_prod(request):
	if request.method == 'POST':
		form = pkOfertaProductosForm(request.POST)
		if form.is_valid():
			IdOfertaProd =  "OP-"+ str(form.cleaned_data["ListaOfertaProductos"]) # reconstruyo el id, solo se obtiene número del id, no el prefijo, por la ordenación previa
			
			try:
				with Conexion_BD().get_conexion_BD().cursor() as cursor:
					# Obtención de todos los atributos de la tupla de la tabla CampañaPublicitaria con identificador IdCampaña
					cursor.execute(f"SELECT * FROM OfertaProductos WHERE IdOfertaProd = '{str(IdOfertaProd)}'")
					tupla_ofer_prod =  cursor.fetchone() 
					ofer_prod_seleccionada = {	'IdOfertaProd':tupla_ofer_prod[0], 'Nombre_OferProd':tupla_ofer_prod[1],
												'ListaProductos':tupla_ofer_prod[2], 'Precio_OferProd' :tupla_ofer_prod[3], 
												'FechaIni_OferProd':tupla_ofer_prod[4], 'FechaFin_OferProd':tupla_ofer_prod[5] }

				return render( request, "consultar_ofer_prod.html", {'form':form, 'incluir_mostrar_tablas':True,
																	'ofer_prod_seleccionada':ofer_prod_seleccionada})
			except:
				error_message=f"ERROR al consultar la Campaña publicitaria con identificador {str(IdOfertaProd)}"
				return render(request,"consultar_ofer_prod.html", {'form':form, "error_message": error_message})

	return render(request,"consultar_ofer_prod.html",{'form': pkOfertaProductosForm()})
