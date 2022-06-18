from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.gestorPolos.models import Polo
from applications.probador.serializers import ProbadorSerializer, UrlGoogleColaboraty
from .utils import cast_InMemoryUploadFile_numpy_array
import requests
import base64
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt


def get_url():
    with open('url.txt') as f:
        url = f.readline()
    return url


class ProbadorView(APIView):
    serializer_class = ProbadorSerializer

    def post(self, request):
        # try:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        image_person = serializer.validated_data['file_person']
        id_polo = serializer.validated_data['id_polo']
        # print(type(image_person))
        # print("Type:", type(image_person.file))
        # print("File:", image_person.file)

        # url = get_url()
        url = "http://127.0.0.1:8987/test"
        url_polo = Polo.objects.get(pk=id_polo).get_image()
        img_bytes = image_person.file.read()
        # print(type(img_bytes)) #class bytes
        im_b64 = base64.b64encode(img_bytes).decode("utf8")

        import json
        payload = json.dumps({"image_person": im_b64, 'url_polo': url_polo})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # text = img: base64...
        response = requests.post(url, data=payload, headers=headers)
        # print(response.json())
        # print(response.json()['img'])
        im_b64_person = response.json()['img']

        # Mostrar la imagen Final
        # img_person_bytes = base64.b64decode(im_b64_person.encode('utf-8'))
        # img_final = Image.open(io.BytesIO(img_person_bytes))
        # np_final = np.asarray(img_final)
        # imgplot = plt.imshow(np.real(np_final))
        # plt.show()

        final_code = 'data:image/jpeg;base64,' + im_b64_person
        data = {"img": final_code}

        # https://stackoverflow.com/questions/67375006/how-to-send-bytesio-using-requests-post
        # image_person_np, image_shirt_np = cast_InMemoryUploadFile_numpy_array(image_person,plot=False)

        return Response(data)
    # except:
    #     return Response({"Imagenes": False, "msg": "Un error inesperado comunicarse con el encargado del backend"})


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
            url = get_url()
            print(url)
            data = {"url": url, "Status": True}
            return Response(data)
        except:
            return Response({"Status": False})
