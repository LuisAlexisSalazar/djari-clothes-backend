from rest_framework import serializers, pagination
from .models import Polo


class PoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polo
        fields = '__all__'


class PoloSerializerHome(serializers.ModelSerializer):
    class Meta:
        model = Polo
        fields = (
            'id',
            'get_image',
            'name_modelo',
            'price',
            'marca',
        )

# class PoloSerializer(serializers.Serializer):
#     recent_polos =
