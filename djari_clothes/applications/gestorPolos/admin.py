from django.contrib import admin
from .models import Polo, PoloFavorites, Marca, DetallePolo

# Register your models here.
admin.site.register(Polo)
admin.site.register(PoloFavorites)
admin.site.register(Marca)
admin.site.register(DetallePolo)
