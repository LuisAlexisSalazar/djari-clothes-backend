from django.urls import include, re_path, path

from . import views

app_name = "producto_app"

urlpatterns = [
    path('api/home/recentPolos/', views.RecentPolosView.as_view(), name='recent'),
    path('api/home/popularPolos/', views.PopularPolosView.as_view(), name='popular'),
    path('api/registerPoloFavorite/', views.RegisterFavoritePoloView.as_view(), name='registerPopularFavorite'),

    # --View to fill data
    path('fillPolos/', views.FillPolosView.as_view()),
    path('fillFavoritiesPolos/', views.FillFavoritiesPolosView.as_view()),
]
