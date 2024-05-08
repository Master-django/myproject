from rest_framework import serializers 
from ..models import Grupe

class GrupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupe
        fields =['name', 'address', 'number_phone', 'burth_day', 'nation']

        