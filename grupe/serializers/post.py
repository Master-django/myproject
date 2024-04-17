from rest_framework import serializers 
from ..models import Grupe

class GrupeSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Grupe
        fields =['Name', 'Suroga', 'Raqami_telefon', 'soli_tavalud', 'Millat']