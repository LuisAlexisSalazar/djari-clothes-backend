from django.urls import include, re_path, path

from . import views

app_name = "producto_app"

urlpatterns = [
    path('api/home/', views.HomeView.as_view(), name='home'),
]
