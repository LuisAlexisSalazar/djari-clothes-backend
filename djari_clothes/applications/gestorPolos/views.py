from django.contrib.auth.models import User
from rest_framework import viewsets
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
        list_id = PoloFavorites.objects.get_list_most_popular()
        queryset = Polo.objects.get_polos_from_list(list_id)
        return queryset


class RegisterFavoritePoloView(CreateAPIView):
    serializer_class = RegisterPoloSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_polo = serializer.validated_data['id_polo']

        polo = Polo.objects.get(pk=id_polo)
        user = self.request.user

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


# class CatalogoView(APIView):

class FilterPolosCatalogoView(APIView):
    serializer_class = FieldsToFilter
    pagination_class = PaginationCatalogoSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data, "*" * 10)
        serializer.is_valid()
        print(serializer.errors)
        if serializer.is_valid():
            polos = Polo.objects.get_polos_to_filter(serializer.validated_data)

            # !Importante poner many=TRUE
            serializer = PoloSerializerHome(polos, many=True)
            return Response(serializer.data)
        return Response({'msj': 'Error en filtrar'})


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
