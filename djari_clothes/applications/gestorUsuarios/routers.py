from rest_framework.routers import DefaultRouter
# *los router solo trabajan con los viewset
from . import viewset

router = DefaultRouter()
# *La url permite hacer el CRUD , colors -> list colors/1/ GET dentro del GET estan las opciones DELETE,PUT,PATCH..

# router.register(r'user', viewset.UserViewSet, basename="user")

urlpatterns = router.urls
