from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="index"),
    path("busqueda/", views.busqueda),
    path("crear/", views.crear),
    path("autos_stock/", views.autos_stock),
    path("ver_autos/", views.view_autos, name="ver_autos"),
    path("cargar_auto/", views.cargar_autos),
]
