from django.urls import path
from . import views

urlpatterns = [
    path("marketing/", views.menu_marketing, name="menu_marketing")
]