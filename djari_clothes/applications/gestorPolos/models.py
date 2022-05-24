from django.db import models
from model_utils.models import TimeStampedModel
from applications.gestorUsuarios.models import AdminProfile, ClientProfile


# Create your models here.


class Polo(TimeStampedModel):
    COLORS = (
        (1, 'Rojo'),
        (2, 'Verde'),
        (3, 'Azul'),
    )

    color = models.CharField(max_length=1, choices=COLORS)
    path_image = models.ImageField(null=False, upload_to='polos')
    name_modelo = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    TALAS = (
        ("S", 'Peuqeño'),
        ("M", 'Mediano'),
        ("L", 'Grande'),
        ("XL", 'X-Grande'),
    )
    talla = models.CharField(max_length=2, choices=TALAS)
    date_input = models.DateField(null=False)

    marca = models.CharField(max_length=10)
    id_admin = models.ForeignKey(AdminProfile, on_delete=models.CASCADE)


class PoloFavorites(TimeStampedModel):
    id_client = models.ForeignKey(ClientProfile, on_delete=models.DO_NOTHING)
    id_polo = models.ForeignKey(Polo, on_delete=models.DO_NOTHING)
