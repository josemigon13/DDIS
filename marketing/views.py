from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def menu_marketing(request):
	if request.method == 'POST':
		keys_request_POST = request.POST.keys()
		if 'alta-oferta-prod-btn' in keys_request_POST:
			return HttpResponseRedirect("/marketing/alta_ofer_prod")
		elif 'baja-oferta-prod-btn' in keys_request_POST:
			return HttpResponseRedirect("/marketing/baja_ofer_prod")
		elif 'consultar-oferta-prod-btn' in keys_request_POST:
			return HttpResponseRedirect("/marketing/consultar_ofer_prod")
		elif 'alta-camp-pub-btn' in keys_request_POST:
			return HttpResponseRedirect("/marketing/alta_camp_pub")
		elif 'baja-camp-pub-btn' in keys_request_POST:
			return HttpResponseRedirect("/marketing/baja_camp_pub")
		elif 'consultar-camp-pub-btn' in keys_request_POST:
			return HttpResponseRedirect("/marketing/consultar_camp_pub")

	return render(request,"menu_marketing.html")

def alta_camp_pub(request):
	form = CampaniaPublicitariaForm()
	if request.method == 'POST':
		form_campania = CampaniaPublicitariaForm( request.POST )
		form_select_ofer_prod = OpcionesOferProdForm( request.POST )
		if form_campania.is_valid() and form_select_ofer_prod.is_valid():
			form.save()
			return HttpResponseRedirect('menu_almacen')
	return render(request,"alta_lote.html",{'form':form})

def baja_camp_pub(request):
	form = pkCampaniaPublicitariaForm()
	if request.method == 'POST':
		form = pkCampaniaPublicitariaForm( request.POST )	
		if form.is_valid():
			pk = form.cleaned_data
			lote = CampaniaPublicitaria.objects.get( IdCampania=pk )
			lote.delete()
			return HttpResponseRedirect('menu_almacen')
		else:
			error_message = "ERROR en el identificador del lote"
			return render(request,"baja_lote.html", {"form": form, "error_message": error_message})
	return render(request,"baja_lote.html",{'form':form})

def consultar_camp_pub(request):
    camp_pubs = CampaniaPublicitaria.objects.all()
    return render(request,"consultar_camp_pub.html",{'camp_pubs': camp_pubs})

def alta_ofer_prod(request):
    form = OfertaProductosForm()
    if request.method == 'POST' :
        form = OfertaProductosForm( request.POST )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('menu_almacen')
    return render(request,"alta_ofer_prod.html",{'form':form})

def baja_ofer_prod(request):
    form = pkOfertaProductosForm()
    if request.method == 'POST' :
        form = pkOfertaProductosForm( request.POST )
        if form.is_valid():
            pk = form.cleaned_data
            almacen = OfertaProductos.objects.get( IdOfertaProd=pk )
            almacen.delete()
            return HttpResponseRedirect('menu_almacen')
        else:
            error_message = "ERROR en el identificador del almacen"
            return render(request,"baja_almacen.html", {"form": form, "error_message": error_message})
    return render(request,"baja_ofer_prod.html",{'form':form})

def consultar_ofer_prod(request):
    ofer_prods = OfertaProductos.objects.all()
    return render(request,"consultar_camp_pub.html",{'ofer_prods':ofer_prods})
