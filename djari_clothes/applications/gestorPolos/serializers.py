from rest_framework import serializers, pagination
from .models import Polo, PoloFavorites


class PoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polo
        fields = '__all__'


class PoloFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloFavorites
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


class PaginationCatalogoSerializer(pagination.PageNumberPagination):
    page_size = 6
    max_page_size = 20


class RegisterPoloSerializer(serializers.Serializer):
    id_polo = serializers.IntegerField()

    def validate(self, data):
        if data['id_polo'] < 0:
            raise serializers.ValidationError('Id del polo Incorrecto')
        return data
