from django.urls import path
from . import views

urlpatterns = [
    path("contabilidad/", views.menu_contabilidad, name="menu_contabilidad")
]
