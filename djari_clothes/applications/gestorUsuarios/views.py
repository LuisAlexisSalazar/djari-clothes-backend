from django.shortcuts import render

from .models import AdminProfile, User
from .serializers import AdminSerializer, UserSerializer
from rest_framework.generics import GenericAPIView
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from djari_clothes.settings import *
from djari_clothes.Fill_data.utils import *


# +View to Fill Data


class FillAdminView(APIView):
    serializer_class = AdminSerializer

    def get(self, request):
        name_file = "admins.json"
        data = read_json(name_file)

        for d in data:
            serializer = self.serializer_class(data=d)

            if serializer.is_valid(raise_exception=True):
                print("*" * 5)
                user = User.objects.get(pk=serializer.validated_data['id_admin'])
                print("*" * 5)
                print("Obtuvo al usuario")
                print(user)
                print(user.id)
                print("*" * 5)
                profile_admin = AdminProfile.objects.create(
                    user=user,
                    numberPhone=serializer.validated_data['numberPhone']
                )
                print("Guardo perfil de admin")
                profile_admin.save()

        return Response({
            'status': "completado registro de los nuevos perfiles de admins"
        })


class FillUserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        name_file = "clients.json"
        data = read_json(name_file)
        for d in data:
            serializer = self.serializer_class(data=d)
            if serializer.is_valid(raise_exception=True):
                client_item = User.objects.create(
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password'],
                    username=serializer.validated_data['username'], )
                client_item.save()
        return Response({
            'status': "completado registro de clients"
        })
