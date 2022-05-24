from django.db import models

# Create your models here.
from django.db import models
from model_utils.models import TimeStampedModel
from applications.gestorPolos.models import Polo
from applications.gestorUsuarios.models import ClientProfile


class Sale(TimeStampedModel):
    amount = models.FloatField(null=False)
    count = models.IntegerField(null=False)
    id_client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)


class DetailSale(models.Model):
    count_polo = models.IntegerField(null=False)
    price_sub_total = models.FloatField(null=False)
    id_sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    id_polo = models.ForeignKey(Polo, on_delete=models.CASCADE)
