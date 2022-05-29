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
