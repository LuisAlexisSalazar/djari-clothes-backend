from django.db import models
from model_utils.models import TimeStampedModel
from applications.gestorUsuarios.models import AdminProfile, User

from .manager import PoloManager, PoloFavoriteManager

from djari_clothes.settings import BASE_DIR


# Create your models here.


class Polo(TimeStampedModel):
    objects = PoloManager()
    COLORS = (
        (1, 'Rojo'),
        (2, 'Verde'),
        (3, 'Azul'),
    )

    # *Filtro
    color = models.IntegerField(choices=COLORS)
    path_image = models.ImageField(upload_to='polos', default=BASE_DIR + "\\media\\polos\default.jpg")
    name_modelo = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    # *Filtro
    # ? Front-end dara Rango de precios
    price = models.FloatField()
    stock = models.IntegerField()

    TALAS = (
        ("S", 'Peuqeño'),
        ("M", 'Mediano'),
        ("L", 'Grande'),
        ("XL", 'X-Grande'),
    )
    # *Filtro
    talla = models.CharField(max_length=2, choices=TALAS)
    MARCAS = (
        (1, 'djari'),
        (2, 'Gucci'),
        (3, 'Nike'),
        (4, 'Adidas'),
    )
    # *Filtro
    marcas = models.IntegerField(default=1, choices=MARCAS)

    def get_image(self):
        if self.path_image:
            return "http://127.0.0.1:8000" + self.path_image.url
        return ''


class PoloFavorites(TimeStampedModel):
    client = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    polo = models.ForeignKey(Polo, on_delete=models.DO_NOTHING)
    objects = PoloFavoriteManager()
