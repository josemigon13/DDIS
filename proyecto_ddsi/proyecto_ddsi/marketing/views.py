from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def menu_marketing(request):
   if request.method == 'POST':
      keys_request_POST = request.POST.keys()
      if 'alta-oferta-prod-btn' in keys_request_POST:
         pass
         # return HttpResponseRedirect("/marketing/alta_of_prod")
      elif 'baja-oferta-prod-btn' in keys_request_POST:
         pass
         # return HttpResponseRedirect("/marketing/baja_of_prod")
      elif 'consultar-oferta-prod-btn' in keys_request_POST:
         pass
         # return HttpResponseRedirect("/marketing/consular_of_prod")
      elif 'alta-camp-pub-btn' in keys_request_POST:
         pass
         # return HttpResponseRedirect("/marketing/alta_camp_pub")
      elif 'baja-camp-pub-btn' in keys_request_POST:
         pass
         # return HttpResponseRedirect("/marketing/baja_camp_pub")
      elif 'consultar-camp-pub-btn' in keys_request_POST:
         pass
         # return HttpResponseRedirect("/marketing/consultar_camp_pub")

   return render(request,"menu_marketing.html")

