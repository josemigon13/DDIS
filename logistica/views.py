from django.shortcuts import render

# Create your views here.

def menu_logistica(request):
    return render(request,"menu_logistica.html")