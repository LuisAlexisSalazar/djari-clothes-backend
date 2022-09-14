from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path, re_path, include
from allauth.account.views import confirm_email

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^rest-auth/', include('rest_auth.urls')),
                  url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
                  url(r'^account/', include('allauth.urls')),
                  url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
                      name='account_confirm_email'),

                  # --Views APIS para front-end
                  re_path('', include('applications.gestorPolos.urls')),
                  re_path('', include('applications.gestorUsuarios.urls')),
                  # re_path('', include('applications.gestorVentas.urls')),
                  re_path('', include('applications.probador.urls')),
                  # --ViewSets: CRUDS
                  re_path('', include('applications.gestorPolos.routers')),
                  re_path('', include('applications.gestorUsuarios.routers')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
