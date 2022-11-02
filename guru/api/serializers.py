from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import City, Shop, Street


class CitySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City


class StreetSerializer(ModelSerializer):
    city = SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        fields = '__all__'
        model = Street


class ShopSerializer(ModelSerializer):
    city = SlugRelatedField(
        queryset=City.objects.all(),
        slug_field='name',
    )
    street = SlugRelatedField(
        queryset=Street.objects.all(),
        slug_field='name',
    )

    class Meta:
        fields = '__all__'
        model = Shop
