from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # --Views APIS para front-end
                  re_path('', include('applications.gestorPolos.urls')),
                  re_path('', include('applications.gestorUsuarios.urls')),
                  re_path('', include('applications.gestorVentas.urls')),
                  re_path('', include('applications.probador.urls')),
                  # --ViewSets: CRUDS
                  re_path('', include('applications.gestorPolos.routers')),
                  re_path('', include('applications.gestorUsuarios.routers')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
