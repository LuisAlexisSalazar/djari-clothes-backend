from django.db import models
from django.contrib.auth.models import AbstractUser


class ClientProfile(models.Model):
    email = models.EmailField(null=True, max_length=75)
    password = models.CharField(max_length=13)
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


# toDo: Usar django utils para obtener la fecha de creación y modificación del modelo
# !falta crear el campo de ultima fecha creado
class AdminProfile(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=13)
    # last_sign_in =
    email = models.EmailField(null=True, max_length=75)
    numberPhone = models.CharField(null=True, max_length=9, unique=True)
    is_afiliado = models.BooleanField(default=False)


class StoreAffiliate(models.Model):
    ruc = models.CharField(unique=True, max_length=9)
    address = models.CharField(max_length=50)
    id_admin = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)
