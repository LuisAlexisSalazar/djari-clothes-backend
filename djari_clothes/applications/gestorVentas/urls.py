from django.urls import path
from . import views

app_name = "sale_app"
urlpatterns = [

    # --View to fill data
    path('fillWholeSale/', views.WholeSaleView.as_view()),
]
