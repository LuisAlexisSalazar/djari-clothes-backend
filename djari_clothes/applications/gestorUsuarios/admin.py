from django.contrib import admin

from .models import MedioContacto, Emprendedor, MedioEmprendedor,Client

# Register your models here.
admin.site.register(MedioContacto)
admin.site.register(Emprendedor)
admin.site.register(MedioEmprendedor)
admin.site.register(Client)
