from django.shortcuts import render

from .models import Sale, DetailSale, Polo, User
from .serializers import SaleSerializer, DetailSaleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from djari_clothes.Fill_data.utils import *


# +View to Fill Data
class WholeSaleView(APIView):
    serializer_class = DetailSaleSerializer

    def get(self, request):
        name_file = "detailSale5.json"
        data = read_json(name_file)

        id_client_temp = 7
        client = User.objects.get(pk=id_client_temp)
        sale = Sale.objects.create(amount=0, count=0, client=client)
        sale.save()

        amount = 0
        count = 0

        for d in data:
            serializer = self.serializer_class(data=d)
            print("*" * 10)
            print(serializer.is_valid())

            if serializer.is_valid():
                polo = serializer.validated_data['polo']

                print("*" * 10)
                print("Obtuvo el polo")

                detail_sale_item = DetailSale.objects.create(
                    count_polo=serializer.validated_data['count_polo'],
                    price=polo.price,
                    sale=sale,
                    polo=polo,
                )
                amount = amount + polo.price * serializer.validated_data["count_polo"]
                count = count + serializer.validated_data["count_polo"]

                detail_sale_item.save()
        sale.amount = amount
        sale.count = count
        sale.save()

        return Response({
            'status': "completado registro de clients"
        })
