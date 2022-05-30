from django.urls import path
from . import views

app_name = "sale_app"
urlpatterns = [

    path('api/carritoCompras/sale/', views.SaleView.as_view(), name="sale"),
    # --View to fill data
    path('fillWholeSale/', views.WholeSaleView.as_view()),
]
