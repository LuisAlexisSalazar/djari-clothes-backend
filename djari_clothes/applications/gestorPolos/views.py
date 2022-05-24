from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Polo
from .custom_renderers import PNGRenderer, JPEGRenderer
from wsgiref.util import FileWrapper
from .serializers import PoloSerializerHome


class HomeView(ListAPIView):
    serializer_class = PoloSerializerHome

    def get_queryset(self):
        print("*" * 10)
        queryset = Polo.objects.get_recent_polo()
        print(queryset)
        return queryset
