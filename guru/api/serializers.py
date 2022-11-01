from rest_framework.serializers import ModelSerializer
from shops.models import City


class CitySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City
