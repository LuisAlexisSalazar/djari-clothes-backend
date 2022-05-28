from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Polo, PoloFavorites
from .serializers import PoloSerializerHome, PoloSerializer, PoloFavoritesSerializer, \
    RegisterPoloSerializer
from djari_clothes.Fill_data.utils import read_json


# +View to application
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
        # print(serializer, "*" * 5)
        # print(serializer.data, "*" * 5)
        id_polo = serializer.validated_data['id_polo']

        polo = Polo.objects.get(pk=id_polo)
        user = self.request.user
        print("*" * 10, user)
        print("*" * 10, type(user))
        try:
            polo_favorite = PoloFavorites(id_client=user, id_polo=polo)
            polo_favorite.save()
            return Response({'msj': 'Exitosa asignación'})
        except:
            return Response({'msj': 'Hubo un problema para asignar'})


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
                    marca=serializer.validated_data['marca'],
                    id_admin=serializer.validated_data['id_admin'],
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
            print(serializer.is_valid())
            print(serializer.errors)
            if serializer.is_valid():
                favorite_polo_item = PoloFavorites.objects.create(
                    id_client=serializer.validated_data['id_client'],
                    id_polo=serializer.validated_data['id_polo'],
                )
                favorite_polo_item.save()

        return Response({
            'status': "completado registro de polos favoritos"
        })
