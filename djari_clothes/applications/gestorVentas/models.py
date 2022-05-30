from django.db import models

# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel
from applications.gestorPolos.models import Polo
from applications.gestorUsuarios.models import User


class Sale(TimeStampedModel):
    amount = models.FloatField(null=False)
    count = models.IntegerField(null=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE)


class DetailSale(models.Model):
    count_polo = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, on_delete=models.CASCADE)


