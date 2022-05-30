from django.shortcuts import render

from .models import Sale, DetailSale, Polo, User
from .serializers import SaleSerializer, DetailSaleSerializer, DetailSail_to_ShopingCarSerializer
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from djari_clothes.Fill_data.utils import *


# +View to System
class SaleView(CreateAPIView):
    serializer_class = DetailSail_to_ShopingCarSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            client = request.user
            list_id_polos = serializer.validated_data['list_id_polos']
            list_count = serializer.validated_data['list_count']
            sale = Sale.objects.create(amount=0, count=0, client=client)
            sale.save()

            amountSale = 0
            countSale = 0
            polos = Polo.objects.filter(pk__in=list_id_polos)

            for polo, count in zip(polos, list_count):
                detail_sale = DetailSale.objects.create(
                    count_polo=count,
                    price=polo.price,
                    sale=sale,
                    polo=polo)
                polo.stock = polo.stock - count
                amountSale = amountSale + (polo.price * count)
                countSale = countSale + count

            sale.amount = amountSale
            sale.count = countSale
            sale.save()

            return Response({'msj': 'venta exitosa'})
        return Response(serializer.errors)


# +View to Fill Data
class WholeSaleView(APIView):
    serializer_class = DetailSaleSerializer

    def get(self, request):
        name_file = "detailSale2.json"
        data = read_json(name_file)

        id_client_temp = 9
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
