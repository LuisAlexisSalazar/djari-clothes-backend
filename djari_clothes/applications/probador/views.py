from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from applications.gestorPolos.models import Polo
from applications.probador.serializers import ProbadorSerializer, UrlGoogleColaboraty, MetricProbadorSerializer
from .utils import cast_InMemoryUploadFile_numpy_array
import requests
import base64
from djari_clothes.settings import BASE_DIR
import json


def get_url():
    with open('url.txt') as f:
        url = f.readline()
    return url


def write_json(new_data, filename='metrics.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["clients"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


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
        url = get_url()
        # url_polo = Polo.objects.get(pk=id_polo).get_image()
        # print(type(url_polo))
        polo = Polo.objects.get(pk=id_polo)
        image_polo = polo.path_image
        print(BASE_DIR)
        path_temp = BASE_DIR + image_polo.url
        # print(type(image_polo)) #ImageField

        # path_image = "media" + polo.path_image
        # print("Path de imagen:", path_image)

        with open(path_temp, "rb") as image_file:
            img64_polo = base64.b64encode(image_file.read()).decode('utf-8')

        # print(image_polo)
        # print(type(image_polo))

        img_bytes = image_person.file.read()
        # print(type(img_bytes)) #class bytes
        img64_person = base64.b64encode(img_bytes).decode("utf8")

        import json
        payload = json.dumps({"image_person": img64_person, 'image_polo': img64_polo})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        try:
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
        except:
            return Response({"Status": "Arreglando"})


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


class SaveMetric(APIView):
    serializer_class = MetricProbadorSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            gradesVis = serializer.validated_data['gradesVis']
            counterVis = len(gradesVis)

            dict_metric = {
                'gradesVis': gradesVis,
                'counterVis': counterVis,
            }
            write_json(dict_metric)
            return Response({'status': "Registrado"})
        except:
            return Response({'status': "Algo salio mal comuniquese con el desarrollador back-end"})
