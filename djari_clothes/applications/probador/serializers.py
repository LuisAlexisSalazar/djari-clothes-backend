from rest_framework import serializers


class ProbadorSerializer(serializers.Serializer):
    file_person = serializers.ImageField()
    id_polo = serializers.IntegerField()


class UrlGoogleColaboraty(serializers.Serializer):
    url = serializers.URLField()


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class MetricProbadorSerializer(serializers.Serializer):
    gradesVis = ArrayIntegerSerializer()
