from rest_framework import serializers, pagination
from .models import AdminProfile, User


class AdminSerializer(serializers.ModelSerializer):
    id_admin = serializers.IntegerField()

    class Meta:
        model = AdminProfile
        fields = ('numberPhone', 'id_admin')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')


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
