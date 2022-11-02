from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .filters import ShopFilter
from .models import City, Shop
from .serializers import CitySerializer, ShopSerializer, StreetSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(ModelViewSet):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        city = get_object_or_404(City, id=city_id)
        return city.streets.all()

    def perform_create(self, serializer):
        city_id = self.kwargs.get('city_id')
        city = get_object_or_404(City, id=city_id)
        serializer.save(city=city)


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShopFilter
