from django.urls import path
from . import views

app_name = "logistica"

urlpatterns = [
    path("logistica/", views.menu_logistica, name="menu_logistica")
]
