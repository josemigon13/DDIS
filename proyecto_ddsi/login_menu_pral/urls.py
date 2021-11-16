from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_bd, name="login_bd"),
    path("menu/", views.menu, name="menu")
]