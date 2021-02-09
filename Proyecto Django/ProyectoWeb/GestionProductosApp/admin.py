from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","precio","seccion","creado")
    search_fields=("nombre","seccion")
    list_filter=("creado","seccion")
    readonly_fields=('creado','actualizado')
    date_hierarchy="creado"
    


admin.site.register(Producto,ProductoAdmin)