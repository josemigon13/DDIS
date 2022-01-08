from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
import cx_Oracle
# # from django.db import connection # para inicializar la variable de conexion_BD para que sea válida antes del login con
# #                                  # la que hay en settigns y que se establece al hacer runserver, donde se cambiará a la 
# #                                  # que interactuará realmente después del login

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Conexion_BD(metaclass=Singleton):
    def get_conexion_BD(self):
        return self.conexion_BD

    def establecer_conexion_BD(self, username, passwd):
        # se define aquí el atributo que almacena la conexión con la BD de Oracle
        self.conexion_BD = cx_Oracle.connect( user=username, password=passwd,
                                        dsn="oracle0.ugr.es:1521/practbd.oracle0.ugr.es",
                                        encoding="UTF-8")

    def cerrar_conexion_BD(self):
        self.conexion_BD.close()


def login_bd(request):
    if request.method == 'POST':
        form = LoginBDForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                Conexion_BD().establecer_conexion_BD(username, password)
                # si se ha conectado bien a la BD, lo redireccionamos  a la url del menú principal de la aplicación
                return HttpResponseRedirect("menu")
            except:
                error_message="""ERROR: Credenciales de usuario y contraseña incorrectas
                                 para la conexión a la base de datos de Oracle"""
                return render(request,"login_bd.html", {"form": form, "error_message": error_message})

    # si no se ha hecho un post o hay errores en los campos del form,
    # se presenta de nuevo el formulario vacío para rellenarlo
    return render(request,"login_bd.html", {"form": LoginBDForm()})

def cerrar_sesion_bd_app():
    Conexion_BD().cerrar_conexion_BD()  # Se cierra la conexión que se estableció con el login del principio
    return HttpResponseRedirect("/")    # Redirige a la raíz de la aplicación, a la página 
                                        # de login, para simular la salida de la aplicación
    

def menu(request):
    if request.method == 'POST':
        keys_request_POST = request.POST.keys()
            # Obtengo las claves del diccionario request.POST, que por ejemplo tiene el valor:
            # <QueryDict: {'csrfmiddlewaretoken': ['CHNZtCiLbU'], 'alamcen-btn': ['']}> 
            # Me quedo con las claves para coger "almacen-btn", que es la que me interesa 
            # coger (según el boton que pulse y se escoja hacer una acción u otra)
        if 'almacen-btn' in keys_request_POST:
            return HttpResponseRedirect("almacen")
        elif 'contabilidad-btn' in keys_request_POST:
            return HttpResponseRedirect("contabilidad")
        elif 'logistica-btn' in keys_request_POST:
            pass
            # return HttpResponseRedirect("logistica")
        elif 'marketing-btn' in keys_request_POST:
            return HttpResponseRedirect("marketing")
        elif 'rrhh-btn' in keys_request_POST:
            pass
            return HttpResponseRedirect("rrhh")
        elif 'cerrar-sesion-bd-app-btn' in keys_request_POST:
            return cerrar_sesion_bd_app()
    
    return render(request,"menu_pral.html")
