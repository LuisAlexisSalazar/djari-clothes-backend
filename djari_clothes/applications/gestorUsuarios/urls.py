from django.urls import path
from . import views

app_name = "users_app"
urlpatterns = [
    # --View to fill data
    path('fillAdmins/', views.FillAdminView.as_view()),
    path('fillUsers/', views.FillUserView.as_view()),
]
