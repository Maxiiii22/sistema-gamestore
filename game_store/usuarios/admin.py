from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email',"cod_area","fecha_nacimiento","first_name", 'last_name',"telefono", 'is_active', 'is_staff')

    search_fields = ('username', 'email',"first_name")  

    list_filter = ('is_staff', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ("cod_area",'fecha_nacimiento',"telefono")}),  
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ( "cod_area",'fecha_nacimiento',"telefono")}),  
    )



admin.site.register(CustomUser, CustomUserAdmin)
