from rest_framework import serializers


class ProbadorSerializer(serializers.Serializer):
    image_person = serializers.ImageField()
    shirt_person = serializers.ImageField()
