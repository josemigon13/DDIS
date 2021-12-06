from django.urls import path
from . import views

app_name = "login_menu_pral"

urlpatterns = [
    path("", views.login_bd, name="login_bd"),
    path("menu/", views.menu, name="menu")
]