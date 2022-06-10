from django.shortcuts import render

from .models import AdminProfile, User
from .serializers import AdminSerializer, UserSerializer, UserRegisterSerializer, UserLoginSerializer, \
    ResetPasswordSerializer, EmailSerializer
from rest_framework.generics import GenericAPIView
import json
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from djari_clothes.settings import *
from djari_clothes.Fill_data.utils import *
from django.db.models import Q
from .utils import send_mail
from django.contrib.auth import authenticate


class CreateUserView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                username = serializer.validated_data['username']
                password = serializer.validated_data['password']
                email = serializer.validated_data['email']
                first_name = serializer.validated_data['first_name']

                user = User.objects.filter(Q(username=username) | Q(email=email))
                if user.exists():
                    return Response({'Creation': False})
                else:
                    user = User.objects.create(username=username,
                                               email=email,
                                               password=password,
                                               is_staff=True,
                                               first_name=first_name)
                    id = user.id
                    return Response({'Creation': True,
                                     'id': id})
        except:
            return Response({'Creation': False})


class LoginUserView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            # print(email,password)
            # user = User.objects.filter(email=email, password=password)
            user = User.objects.filter(email=email)
            if user.exists() and authenticate(request, username=user[0].username, password=password):
                return Response({"Credenciales": True})
            else:
                return Response({"Credenciales": False})
        return Response({"msj": "Error en el formato de datos"})


class SendEmailResetPassword(APIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            if user:
                send_mail(str(user.id), to_emails=[user.email])
                return Response({"StatusCorreo": True})
            else:
                return Response({"StatusCorreo": False})
        return Response({"msj": "Error en el formato de datos"})


class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer

    def put(self, request, pk):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            password = serializer.validated_data['password']
            confirmation_password = serializer.validated_data['confirmation_password']
            print("Vives")
            try:
                client = User.objects.get(pk=pk)
                if password != confirmation_password:
                    return Response({"msj": "Error las contraseña deben ser iguales"})
                else:
                    client.set_password(password)
                    client.save()
                    return Response({"ResetPassword": True})
            except:
                return Response({"msj": "Error desconocido"})


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
