from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from applications.gestorPolos.models import Polo
from applications.probador.serializers import ProbadorSerializer, UrlGoogleColaboraty
from .utils import cast_InMemoryUploadFile_numpy_array


class ProbadorView(APIView):
    serializer_class = ProbadorSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()

            image_person = serializer.validated_data['image_person']
            shirt_person = serializer.validated_data['shirt_person']

            image_person_np, image_shirt_np = cast_InMemoryUploadFile_numpy_array(image_person,
                                                                                  shirt_person,
                                                                                  plot=False)

            return Response({"Imagenes": True})
        except:
            return Response({"Imagenes": False, "msg": "Un error inesperado comunicarse con el encargado del backend"})


class UpdateGoogleColaboraty(APIView):
    serializer_class = UrlGoogleColaboraty

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()

            url_googleCollaboraty = serializer.validated_data['url']
            with open('url.txt', 'w') as f:
                f.write(url_googleCollaboraty)
            return Response({"Update": True})
        except:
            return Response({"Update": False})


class GetURLGoogleColaboraty(APIView):
    def get(self, request):
        try:
            with open('url.txt') as f:
                url = f.readline()

            print(url)
            data = {"url": url, "Status": True}
            return Response(data)
        except Exception as e:
            return Response({"error": e, "Status": False})
