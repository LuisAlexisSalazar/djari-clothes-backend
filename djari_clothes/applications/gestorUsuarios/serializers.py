from rest_framework import serializers, pagination
from .models import User, Emprendedor, MedioContacto, MedioEmprendedor, Client


# class AdminSerializer(serializers.ModelSerializer):
#     id_admin = serializers.IntegerField()
#
#     class Meta:
#         model = AdminProfile
#         fields = ('numberPhone', 'id_admin')


class EmprendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprendedor
        fields = '__all__'


class MedioContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioContacto
        fields = '__all__'


class MedioContactoSerializer(serializers.ModelSerializer):
    id_emprendedor = serializers.IntegerField()
    id_medioContacto = serializers.IntegerField()

    class Meta:
        model = MedioEmprendedor
        fields = ('valor_medio', 'link_medio', 'id_emprendedor', 'id_medioContacto')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email',)


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirmation_password = serializers.CharField()


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserDetails(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
