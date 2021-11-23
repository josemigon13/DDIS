from django.urls import path
from . import views

urlpatterns = [
    path("logistica/", views.menu_logistica, name="menu_logistica")
]
