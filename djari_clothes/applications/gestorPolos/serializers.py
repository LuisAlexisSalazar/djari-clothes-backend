from rest_framework import serializers, pagination

from .models import Polo, PoloFavorites, Marca, DetallePolo
from ..gestorUsuarios.models import MedioEmprendedor, Emprendedor


class DetallePoloSerializerFill(serializers.ModelSerializer):
    id_polo = serializers.IntegerField()

    class Meta:
        model = DetallePolo
        fields = ('talla', 'id_polo')


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class PoloFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoloFavorites
        # fields = '__all__'
        fields = ('name_marca',)


class PoloSerializerHome(serializers.ModelSerializer):
    marca = MarcaSerializer(many=True)
    tallas = serializers.SerializerMethodField()

    class Meta:
        model = Polo
        fields = (
            'id',
            'get_image',
            'name_modelo',
            'price',
            'marca',
            'tallas',
        )

    def get_tallas(self, obj):
        # Queryset
        tallas = DetallePolo.objects.filter(polo=obj).values('talla')
        list_tallas = []
        for t in tallas:
            list_tallas.append(t['talla'])
        return list_tallas


class MedioSerializer(serializers.ModelSerializer):
    nameMedio = serializers.SerializerMethodField()

    class Meta:
        model = MedioEmprendedor
        # fields = '__all__'
        fields = ('valor_medio', 'link_chat', 'nameMedio')

    def get_nameMedio(self, obj):
        # return {'nombre_medio': obj.medioContacto.nombre_medio}
        return obj.medioContacto.nombre_medio


# ?Return customer manytomany serializer
# https://stackoverflow.com/questions/17256724/include-intermediary-through-model-in-responses-in-django-rest-framework
class EmprendedorSerializar(serializers.ModelSerializer):
    # medios = MedioSerializer(source='medio_emprendedor_set', many=True)
    medios = serializers.SerializerMethodField()

    class Meta:
        model = Emprendedor
        fields = ('name_emprendedor', 'medios')

    def get_medios(self, obj):
        qset = MedioEmprendedor.objects.filter(emprendedor=obj)
        return [MedioSerializer(m).data for m in qset]


class PoloSerializer(serializers.ModelSerializer):
    # emprendedor = serializers.SerializerMethodField()
    emprendedor = EmprendedorSerializar()
    marca = serializers.SerializerMethodField()

    class Meta:
        model = Polo
        fields = '__all__'

    # def get_emprendedor(self, obj):
    #     return obj.emprendedor.name_emprendedor

    def get_marca(self, obj):
        # *Marca en este caso es la relación muchos a muchos
        queryset = obj.marca.all()
        return queryset[0].name_marca


class PoloSerializerHome2(serializers.ModelSerializer):
    emprendedor = EmprendedorSerializar()
    marca = serializers.SerializerMethodField()
    tallas = serializers.SerializerMethodField()

    class Meta:
        model = Polo
        fields = (
            'id',
            'get_image',  # Function of model defined
            'price',
            'marca',
            'emprendedor',
            'color',
            'tallas'
        )

    def get_marca(self, obj):
        # *Marca en este caso es la relación muchos a muchos
        queryset = obj.marca.all()
        return queryset[0].name_marca

    def get_tallas(self, obj):
        # Queryset
        tallas = DetallePolo.objects.filter(polo=obj).values('talla')
        list_tallas = []
        for t in tallas:
            list_tallas.append(t['talla'])
        return list_tallas

    # class MedioEmprendedorSerializaer(serializers.ModelSerializer):


#     emprendedor =
#     medioContacto =
#     class Meta:
#         models = MedioEmprendedor
#         fields = ("emprendedor",
#                   "medioContacto",
#                   "valor_medio",
#                   "link_medio")

# +Pagination


class PaginationCatalogoSerializer(pagination.PageNumberPagination):
    page_size = 6
    max_page_size = 20


class RegisterPoloSerializer(serializers.Serializer):
    id_polo = serializers.IntegerField()
    id_user = serializers.IntegerField()

    def validate(self, data):
        if data['id_polo'] < 0:
            raise serializers.ValidationError('Id del polo Incorrecto')
        return data


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class ArrayCharSerializer(serializers.ListField):
    child = serializers.CharField()


class FieldsToFilter(serializers.Serializer):
    list_colors = ArrayIntegerSerializer()
    range_price = ArrayIntegerSerializer()
    list_tallas = ArrayCharSerializer()
    list_marcas = ArrayIntegerSerializer()


class AffiliationContactSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=4, max_length=35)
    email = serializers.EmailField(allow_blank=False)
    message = serializers.CharField(min_length=15, max_length=70)
