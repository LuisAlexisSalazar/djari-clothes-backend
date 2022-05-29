from rest_framework import serializers, pagination
from .models import Sale, DetailSale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class DetailSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSale
        fields = ('count_polo', 'polo')
