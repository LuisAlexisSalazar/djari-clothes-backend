from django.shortcuts import render

from .models import User, Emprendedor, MedioContacto, MedioEmprendedor, Client
from .serializers import UserRegisterSerializer, UserLoginSerializer, \
    ResetPasswordSerializer, EmailSerializer, UserDetails, EmprendedorSerializer, MedioContactoSerializer
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

from ..gestorPolos.serializers import AffiliationContactSerializer


class CreateUserView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):

                email = serializer.validated_data['email']

                # user = Client.objects.filter(Q(username=username) | Q(email=email))
                client = Client.objects.filter(email=email)
                if client.exists():
                    return Response({'Creation': False})
                else:
                    new_client = Client.objects.create(email=email)
                    id = new_client.id
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
                id = user[0].id
                return Response({"Credenciales": True, "id": id})
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
                send_mail(str(user.id), to_emails=[user.email], ResetPassword=True)
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


class DetailsUser(APIView):

    def get(self, request, pk):
        id_user = self.kwargs.get('pk')
        user = User.objects.get(pk=id_user)
        serializer_data = UserDetails(user)
        return Response(serializer_data.data)


class AffiliationContactSerializerView(APIView):
    serializer_class = AffiliationContactSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = "Nombre de contacto: " + name + "\n" + "Medio de contacto: " + email + "\n" + "Mensaje: " + \
                      serializer.validated_data[
                          'message']
            email_hector = "hector.idme@ucsp.edu.pe"
            send_mail(to_emails=[email_hector], mesage=message, ResetPassword=False, subject="Posible Afiliación")
            return Response({
                'status': "EMail completado"
            })
        else:
            return Response({
                'status': "Erro"
            })


# ++++++++++++++++Fill++++++++++++++++++++++
class FillEmprendedoresView(APIView):
    serializer_class = EmprendedorSerializer

    def get(self, request):
        name_file = "emprendedor.json"
        data = read_json(name_file)
        for d in data:
            serializer = self.serializer_class(data=d)
            if serializer.is_valid(raise_exception=True):
                emprendedor = Emprendedor.objects.create(
                    name_emprendedor=serializer.validated_data['name_emprendedor'])
                emprendedor.save()
        return Response({
            'status': "completado registro de emprendedores"
        })


class MedioContactoView(APIView):
    serializer_class = MedioContactoSerializer

    def get(self, request):
        name_file = "mediosContacto.json"
        data = read_json(name_file)
        for d in data:
            serializer = self.serializer_class(data=d)
            if serializer.is_valid(raise_exception=True):
                medio_contacto = MedioContacto.objects.create(
                    nombre_medio=serializer.validated_data['nombre_medio'])
                medio_contacto.save()
        return Response({
            'status': "completado registro de Medio de Contacto"
        })


class MedioEmpresariosView(APIView):
    serializer_class = MedioContactoSerializer

    def get(self, request):
        name_file = "medioEmprendedor.json"
        data = read_json(name_file)
        for d in data:
            serializer = self.serializer_class(data=d)
            if serializer.is_valid(raise_exception=True):
                id_emprendedor = serializer.validated_data['id_emprendedor']
                id_medioContacto = serializer.validated_data['id_medioContacto']

                emprendedor = Emprendedor.objects.get(pk=id_emprendedor)
                medioContacto = MedioContacto.objects.get(pk=id_medioContacto)

                medioEmprendedor = MedioEmprendedor.objects.create(
                    emprendedor=emprendedor,
                    medioContacto=medioContacto,
                    valor_medio=serializer.validated_data['valor_medio'],
                    link_medio=serializer.validated_data['link_medio'],
                )
                medioEmprendedor.save()
        return Response({
            'status': "completado registro de Medios de Emprendedor"
        })
