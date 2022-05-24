from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  re_path('', include('applications.gestorPolos.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
