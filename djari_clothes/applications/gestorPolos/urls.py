from django.urls import include, re_path, path

from . import views

app_name = "producto_app"

urlpatterns = [
    path('api/home/recentPolos/', views.RecentPolosView.as_view(), name='recent'),
    path('api/home/popularPolos/', views.PopularPolosView.as_view(), name='popular'),
    path('api/registerPoloFavorite/', views.RegisterFavoritePoloView.as_view(), name='registerPopularFavorite'),
    path('api/paginaItem/detailsPolo/<pk>', views.DetailsPoloView.as_view(), name='polo_details'),
    path('api/catalogo/polos/', views.PolosCatalogoView.as_view(), name='polos_catalogos'),
    path('api/catalogo/filter_polos/', views.FilterPolosCatalogoView.as_view(), name='filter_polos'),
    path('api/catalogo/filters/', views.FiltersCatalogo.as_view(), name='filters_catalogo'),

    # --View to fill data
    path('fillPolos/', views.FillPolosView.as_view()),
    path('fillFavoritiesPolos/', views.FillFavoritiesPolosView.as_view()),
]
