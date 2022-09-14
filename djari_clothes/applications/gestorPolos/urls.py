from django.urls import include, re_path, path

from . import views

app_name = "producto_app"

urlpatterns = [
    # *Apis del Nuevo Modelo de Negocio
    path('api/catalogo/polos/', views.PolosCatalogoView.as_view(), name='polos_catalogos'),
    path('api/home/popularPolos/', views.PopularPolosView.as_view(), name='popular'),
    path('api/home/recentPolos/', views.RecentPolosView.as_view(), name='recent'),
    path('api/registerPoloFavorite/', views.RegisterFavoritePoloView.as_view(), name='registerPopularFavorite'),
    path('api/paginaItem/detailsPolo/<pk>', views.DetailsPoloView.as_view(), name='polo_details'),

    # ------------------Antiguos---------------
    # toDo:Hacer compatible con el nuevo modelo de negocio
    path('api/catalogo/filter_polos/', views.FilterPolosCatalogoView.as_view(), name='filter_polos'),
    path('api/catalogo/filters/', views.FiltersCatalogo.as_view(), name='filters_catalogo'),
    # !Pensarlo
    # path('api/details/emprendedor/<pk>', views.FiltersCatalogo.as_view(), name='filters_catalogo'),
    path('api/Test/', views.Test.as_view()),
    # todo: Hacer para un usuario
    path('api/user/poloFavorite/<pk>', views.PolosFavoriteUser.as_view(), name='filters_catalogo'),

    # -----------------------View to fill data--------------
    path('fillPolos/', views.FillPolosView.as_view()),
    path('fillMarcas/', views.FillMarcasView.as_view()),
    path('fillFavoritiesPolos/', views.FillFavoritiesPolosView.as_view()),
    path('fillDetailsPolos/', views.FillDetailsPolosView.as_view()),
]
# Parametros por la misma URL
# https://stackoverflow.com/questions/69408184/drf-url-kwargs-get-list-in-object
# https://djangokatya.com/2020/09/17/django-rest-a-simple-filtering-view-with-arguments/
# Parametros que no pertenecen a la URL pero los pones en ella con GET
# https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
