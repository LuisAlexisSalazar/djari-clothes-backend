from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()

router.register(r'polos', viewsets.PoloViewSet, basename="polos")

urlpatterns = router.urls
