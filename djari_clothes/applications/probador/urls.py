from django.urls import path
from . import views

app_name = "probador_app"
urlpatterns = [

    path('api/probador/', views.ProbadorView.as_view()),
    path('api/update/url_Google', views.UpdateGoogleColaboraty.as_view()),
    path('api/recovery/url_Google', views.GetURLGoogleColaboraty.as_view()),
    path('api/save_metric', views.SaveMetric.as_view())

]
# https://colab.research.google.com/drive/1fzE9wogJs1sY-c29Vg8DcTpRhFwQZPlj#scrollTo=ERtlKi12zcDt