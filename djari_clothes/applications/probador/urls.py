from django.urls import path
from . import views

app_name = "probador_app"
urlpatterns = [

    path('api/probador/', views.ProbadorView.as_view()),
    path('api/update/url_Google', views.UpdateGoogleColaboraty.as_view()),
    path('api/recovery/url_Google', views.GetURLGoogleColaboraty.as_view())

]
