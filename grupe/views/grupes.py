from rest_framework import generics
from grupe.models import Grupe
from grupe.serializers import GrupeSerializer
from rest_framework import viewsets


class GrupeViewSet(viewsets.ModelViewSet):
    queryset = Grupe.objects.all()
    serializer_class = GrupeSerializer