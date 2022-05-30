from django.urls import path
from . import views

app_name = "users_app"
urlpatterns = [
    # --View
    path('api/registrarse/createUser/', views.CreateUserView.as_view()),
    path('api/login/login/', views.LoginUserView.as_view()),
    # toDo: cambiar la URL del password con un uuid
    path('api/ForgotPassword/sendEmail', views.SendEmailResetPassword.as_view()),
    path('api/ForgotPassword/newPassword/<pk>', views.ResetPasswordView.as_view()),

    # --View to fill data
    path('fillAdmins/', views.FillAdminView.as_view()),
    path('fillUsers/', views.FillUserView.as_view()),
]
