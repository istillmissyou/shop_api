from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, ShopViewSet, StreetViewSet

router = DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'shop', ShopViewSet)
router.register(
    r'city/(?P<city_id>\d+)/street',
    StreetViewSet,
    basename='street'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
