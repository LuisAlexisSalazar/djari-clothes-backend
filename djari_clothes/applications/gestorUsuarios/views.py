from django.shortcuts import render

from .models import AdminProfile, ClientProfile
from .serializers import AdminSerializer, ClientSerializer
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
        print("Entra Get")
        file = BASE_DIR + "\djari_clothes\Fill_data\\admins.json"
        print("*" * 5, file)
        f = open(file)
        data = json.load(f)
        print("Leyo Json")
        for d in data:
            # print(d)
            serializer = AdminSerializer(data=d)
            if serializer.is_valid():
                AdminItem = AdminProfile.objects.create(
                    name=serializer.validated_data['name'],
                    password=serializer.validated_data['password'],
                    email=serializer.validated_data['email'],
                    numberPhone=serializer.validated_data['numberPhone'],
                    is_afiliado=serializer.validated_data['is_afiliado'],
                )
                AdminItem.save()

        return Response({
            'status': "completado registro de admins"
        })


class FillClientView(APIView):
    serializer_class = ClientSerializer

    def get(self, request):
        name_file = "clients.json"
        data = read_json(name_file)

        for d in data:
            serializer = self.serializer_class(data=d)
            if serializer.is_valid():
                client_item = ClientProfile.objects.create(
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password'],
                    name=serializer.validated_data['name'],
                    last_name=serializer.validated_data['last_name'],
                )
                client_item.save()

        return Response({
            'status': "completado registro de clients"
        })
