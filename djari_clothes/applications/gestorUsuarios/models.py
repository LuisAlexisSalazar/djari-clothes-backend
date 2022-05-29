from django.db import models
from django.contrib.auth.models import User


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    numberPhone = models.CharField(null=True, max_length=9, unique=True)


class StoreAffiliate(models.Model):
    ruc = models.CharField(unique=True, max_length=9)
    address = models.CharField(max_length=50)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
