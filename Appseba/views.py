from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def muestra_fam(request):
    familiar_1=Familiar(nombre="Gisel",edad=33,nacim="2000-12-1")
    familiar_2=Familiar(nombre="Benito",edad=6,nacim="2000-12-1")
    familiar_3=Familiar(nombre="Sebastian",edad=30,nacim="2000-12-1")
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    list_famila=[familiar_1,familiar_2,familiar_3]
    dic_familia={"diccionario1":list_famila}
    plantilla=loader.get_template("template.html")
    documento=plantilla.render(dic_familia)
    return HttpResponse(documento)