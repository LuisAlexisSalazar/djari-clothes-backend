from django.urls import path
from . import views

app_name = "users_app"
urlpatterns = [
    # *Nuevo Modelo de Negocio
    path('api/registrarse/createUser/', views.CreateUserView.as_view()),
    path('api/user/AffiliationContact/', views.AffiliationContactSerializerView.as_view()),

    # --View
    path('api/login/login/', views.LoginUserView.as_view()),
    # toDo: cambiar la URL del password con un uuid
    path('api/ForgotPassword/sendEmail', views.SendEmailResetPassword.as_view()),
    path('api/ForgotPassword/newPassword/<pk>', views.ResetPasswordView.as_view()),
    path('api/user/details/<pk>', views.DetailsUser.as_view()),

    # --View to fill data
    # path('fillAdmins/', views.FillAdminView.as_view()),
    path('fillEmprendedores/', views.FillEmprendedoresView.as_view()),
    path('fillMedioContacto/', views.MedioContactoView.as_view()),
    path('fillMedioEmpresarios/', views.MedioEmpresariosView.as_view()),
]
