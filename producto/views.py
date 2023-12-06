from django.shortcuts import render
from cliente import models

def home(request):
    return render(request, "producto/index.html")

def view_autos(request):
    auto = models.Auto.objects.all()
    context = {"Autor" : auto}
    return render(request, "Producto/ver_autos.html", context)