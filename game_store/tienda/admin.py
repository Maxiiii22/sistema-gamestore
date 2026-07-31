from django.contrib import admin
from .models import Empresa,Genero,Plataforma,Consolas,Modelo,Juegos,RelojInteligentes,Celulares,AccesoriosPC,ProductoConImagen,ImagenSecundaria,Marca,Conexion

# Register your models here.

class ConsolasyJuegosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre', 'edicion')}   

class ProductoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}  

admin.site.register(Empresa)
admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Consolas,ConsolasyJuegosAdmin)
admin.site.register(Modelo)
admin.site.register(Marca)
admin.site.register(Juegos,ConsolasyJuegosAdmin)
admin.site.register(RelojInteligentes,ProductoAdmin)
admin.site.register(Celulares,ProductoAdmin)
admin.site.register(AccesoriosPC,ProductoAdmin)
admin.site.register(Conexion)
admin.site.register(ProductoConImagen)
admin.site.register(ImagenSecundaria)

