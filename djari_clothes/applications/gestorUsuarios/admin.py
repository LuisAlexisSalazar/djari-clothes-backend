from django.contrib import admin
from .models import AdminProfile, ClientProfile, StoreAffiliate

# Register your models here.
admin.site.register(AdminProfile)
admin.site.register(ClientProfile)
admin.site.register(StoreAffiliate)
