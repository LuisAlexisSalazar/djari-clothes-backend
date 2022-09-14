from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PoloSerializer
from .serializers import (
    Polo)


class PoloViewSet(viewsets.ModelViewSet):
    serializer_class = PoloSerializer
    queryset = Polo.objects.all()
