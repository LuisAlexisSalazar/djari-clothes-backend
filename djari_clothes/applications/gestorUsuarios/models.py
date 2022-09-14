from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
)

from applications.gestorUsuarios.managers import UserManager


class MedioContacto(models.Model):
    nombre_medio = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nombre_medio


class Emprendedor(models.Model):
    name_emprendedor = models.CharField(max_length=25, unique=True)
    medios = models.ManyToManyField(MedioContacto, through='MedioEmprendedor')

    def __str__(self):
        return self.name_emprendedor


class MedioEmprendedor(models.Model):
    emprendedor = models.ForeignKey(Emprendedor, on_delete=models.CASCADE)
    medioContacto = models.ForeignKey(MedioContacto, on_delete=models.CASCADE)
    valor_medio = models.CharField(max_length=25)
    link_chat = models.CharField(null=True, max_length=50)


class Client(AbstractUser):
    # username = models.CharField(max_length=150, unique=False, blank=True)
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nameClient = models.CharField(blank=True, max_length=100)

    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)  # a admin user; non super-user
    # admin = models.BooleanField(default=False)  # a superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
