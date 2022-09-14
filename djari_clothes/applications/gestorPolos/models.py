from django.db import models
from model_utils.models import TimeStampedModel
from applications.gestorUsuarios.models import User

from .manager import PoloManager, PoloFavoriteManager
from applications.gestorUsuarios.models import Client
from djari_clothes.settings import BASE_DIR
from applications.gestorUsuarios.models import Emprendedor

# Create your models here.

PATH_IMAGE_DEFAULT = "\\polos\default.jpg"


class Marca(models.Model):
    name_marca = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name_marca


class Polo(TimeStampedModel):
    objects = PoloManager()
    COLORS = (
        ('Rojo', 'Rojo'),
        ('Verde', 'Verde'),
        ('Azul', 'Azul'),
        ('Amarillo', 'Amarillo'),
        ('Morado', 'Morado'),
        ('Naranja', 'Naranja'),
        ('Blanco', 'Blanco'),
        ('Negro', 'Negro'),
        ('Celeste', 'Celeste'),
    )

    # *Filtro
    color = models.CharField(choices=COLORS, max_length=8)
    path_image = models.ImageField(upload_to='polos', default=PATH_IMAGE_DEFAULT)
    name_modelo = models.CharField(max_length=15)
    description = models.CharField(max_length=200, blank=True)
    # *Filtro
    # ? Front-end dara Rango de precios
    price = models.FloatField()
    emprendedor = models.ForeignKey(Emprendedor, on_delete=models.CASCADE)
    # *Filtro
    marca = models.ManyToManyField(Marca)

    def get_image(self):
        if self.path_image:
            return "http://127.0.0.1:8000" + self.path_image.url
        return PATH_IMAGE_DEFAULT


# Se envia S M... y en la base de datos llena con Pequeño S, Mediano M..
TALLAS = (
    ("S", 'Pequeño (S)'),
    ("M", 'Mediano (M)'),
    ("L", 'Grande (L)'),
    ("XL", 'Extra Grande (XL)'),
)


class DetallePolo(models.Model):
    # *Filtro
    polo = models.ForeignKey(Polo, on_delete=models.DO_NOTHING)
    talla = models.CharField(max_length=2, choices=TALLAS)


class PoloFavorites(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    polo = models.ForeignKey(Polo, on_delete=models.DO_NOTHING)
    objects = PoloFavoriteManager()
