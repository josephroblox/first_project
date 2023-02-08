from django.contrib import admin
from .forms import RegModelForm
from boletin.models import Registrado

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["id", "email", "nombre"] #aqui se escribe las columnas que quiero q tenga la tabla
    form = RegModelForm
    list_filter = ["timestamp", "nombre"]#aqui se escriben los filtros que quiero seleccionar
    search_fields =["nombre", "email"]#aqui se escriben los campos de busqueda escrita
    #list_editable =["nombre", "email"]#me sirvio para modificar esas propiedas en la tabla
   #class Meta:
    #model = Registrado 
    

# Register your models here.
admin.site.register(Registrado, AdminRegistrado)