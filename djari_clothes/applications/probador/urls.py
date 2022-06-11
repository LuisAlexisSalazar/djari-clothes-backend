from django.urls import path
from . import views

app_name = "probador_app"
urlpatterns = [

    path('api/probador/', views.ProbadorView.as_view())

]
