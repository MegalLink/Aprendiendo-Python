from django.urls import path
from ProyectoWebApp import views
urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('productos/', views.productos,name="Productos"),
    path('contacto/', views.contacto,name="Contacto"),
    path('nosotros/', views.nosotros,name="Nosotros"),
]