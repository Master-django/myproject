from django.urls import path, include
from rest_framework import routers
from .views import GrupeViewSet

router = routers.DefaultRouter()
router.register(r'grupe', GrupeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


