from django.shortcuts import render,HttpResponse
from GestionProductosApp.models import Producto
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def productos(request):
    productos=Producto.objects.all()
    ctx={'productos':productos}
    return render(request,"productos.html",ctx)

def contacto(request):
    
    if request.method=="POST":
        subject=request.POST["nombre"]
        message=request.POST["mensaje"]+ " "+ request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["alexresidentevil@gmail.com"]

        send_mail(subject,message,email_from,recipient_list)
        enviado=True
        return render(request,"enviado.html")
    return render(request,"contacto.html")

def nosotros(request):
    return render(request,"nosotros.html")

