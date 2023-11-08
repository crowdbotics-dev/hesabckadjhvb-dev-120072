from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NewConnectorbackendhesViewSet

router = DefaultRouter()
router.register(
    "newconnectorbackendhes",
    NewConnectorbackendhesViewSet,
    basename="newconnectorbackendhes",
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
