from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Polo, PoloFavorites
from .serializers import PoloSerializerHome, PoloSerializer, PoloFavoritesSerializer, \
    RegisterPoloSerializer, PaginationCatalogoSerializer, FieldsToFilter
from djari_clothes.Fill_data.utils import read_json

# +View to application
from ..gestorUsuarios.models import AdminProfile


class RecentPolosView(ListAPIView):
    serializer_class = PoloSerializerHome

    def get_queryset(self):
        queryset = Polo.objects.get_recent_polo()
        return queryset


class PopularPolosView(ListAPIView):
    serializer_class = PoloSerializerHome

    def get_queryset(self):
        list_id_polos = PoloFavorites.objects.get_list_most_popular()
        # id_user = self.kwargs.get('pk', None)
        # user = User.objects.get(pk=id_user)
        # list_id_polos = PoloFavorites.objects(client=user)[:10].values_list('polo', flat=True)
        queryset = Polo.objects.get_polos_from_list(list_id_polos)
        return queryset


class RegisterFavoritePoloView(CreateAPIView):
    serializer_class = RegisterPoloSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_polo = serializer.validated_data['id_polo']
        id_user = serializer.validated_data['id_user']

        polo = Polo.objects.get(pk=id_polo)
        user = User.objects.get(pk=id_user)

        polo_favorite = PoloFavorites.objects.filter(client=user, polo=polo)
        if polo_favorite.exists():
            polo_favorite.delete()
            return Response({'msj': 'Asignación Removida'})
        else:
            polo_favorite = PoloFavorites(client=user, polo=polo)
            polo_favorite.save()
            return Response({'msj': 'Exitosa asignación'})


class DetailsPoloView(RetrieveAPIView):
    queryset = Polo.objects.all()
    serializer_class = PoloSerializer


class PolosCatalogoView(ListAPIView):
    serializer_class = PoloSerializerHome
    queryset = Polo.objects.all()
    pagination_class = PaginationCatalogoSerializer


class FiltersCatalogo(APIView):
    def get(self, request):
        tallas = [x[0] for x in Polo.TALLAS]
        marcas = [x[1] for x in Polo.MARCAS]
        colores = [x[1] for x in Polo.COLORS]

        filters = {
            "tallas": tallas,
            "marcas": marcas,
            "colores": colores,
            "rango_precio": [0, 350],
        }
        return Response(filters)


# class CatalogoView(APIView):

class FilterPolosCatalogoView(ListAPIView):
    # serializer_class = FieldsToFilter
    # serializer_class = FieldsToFilter
    serializer_class = PoloSerializerHome
    pagination_class = PaginationCatalogoSerializer

    def get_queryset(self):
        list_colors = self.request.GET.get('list_colors', [])
        range_price = self.request.GET.get('range_price', [])
        list_tallas = self.request.GET.get('list_tallas', [])
        list_marcas = self.request.GET.get('list_marcas', [])

        if len(list_colors) != 0:
            list_colors = list_colors.split(",")
            list_colors = list(map(int, list_colors))

        if len(range_price) != 0:
            range_price = range_price.split(",")
            range_price = list(map(int, range_price))
        if len(list_tallas) != 0:
            list_tallas = list_tallas.split(",")
        if len(list_marcas) != 0:
            list_marcas = list_marcas.split(",")
            list_marcas = list(map(int, list_marcas))

        data = {'list_colors': list_colors,
                'range_price': range_price,
                'list_tallas': list_tallas,
                'list_marcas': list_marcas}
        print(data)
        polos = Polo.objects.get_polos_to_filter(data)
        # !Importante poner many=TRUE
        # serializer = PoloSerializerHome(polos, many=True)
        # return Response(serializer.data)

        # --Try solve pagintation
        # paginator = LimitOffsetPagination()
        # result_page = self.pagination_class.paginate_queryset(polos, request)
        # serializer = PoloSerializerHome(result_page, many=True, context={'request': request})
        # response = Response(serializer.data, status=status.HTTP_200_OK)
        # return response
        # return Polo.objects.all()
        return polos
        # return Response({'msj': 'Error en filtrar'})


# class PolosFavoriteUser(ListAPIView):
#     serializer_class = PoloSerializerHome
#
#     def get_queryset(self):
#         # id_user = self.kwargs.get('pk', None)
#         # id_user = pk
#         # print(id_user)
#         user = User.objects.get(pk=id_user)
#         list_id_polos = PoloFavorites.objects(client=user)[:10].values_list('polo', flat=True)
#         queryset = Polo.objects.get_polos_from_list(list_id_polos)
#         return queryset


# +View to Fill Data
class FillPolosView(APIView):
    serializer_class = PoloSerializer

    def get(self, request):
        name_file = "polos.json"
        data = read_json(name_file)

        for d in data:
            # print(d)
            serializer = self.serializer_class(data=d)
            print(serializer.is_valid())
            print(serializer.errors)
            if serializer.is_valid():
                PoloItem = Polo.objects.create(
                    color=serializer.validated_data['color'],
                    name_modelo=serializer.validated_data['name_modelo'],
                    description=serializer.validated_data['description'],
                    price=serializer.validated_data['price'],
                    stock=serializer.validated_data['stock'],
                    talla=serializer.validated_data['talla'],
                    marcas=serializer.validated_data['marcas'],
                )
                PoloItem.save()

        return Response({
            'status': "completado registro de polos"
        })


class FillFavoritiesPolosView(APIView):
    serializer_class = PoloFavoritesSerializer

    def get(self, request):
        name_file = "favoritePolos.json"
        data = read_json(name_file)

        for d in data:
            # print(d)
            serializer = self.serializer_class(data=d)

            if serializer.is_valid(raise_exception=True):
                # client = User.objects.get(pk=serializer.validated_data['client'])
                client = serializer.validated_data['client']

                if not (AdminProfile.objects.filter(user=client)):
                    favorite_polo_item = PoloFavorites.objects.create(
                        client=client,
                        polo=serializer.validated_data['polo'])
                    favorite_polo_item.save()

        return Response({
            'status': "completado registro de polos favoritos"
        })
