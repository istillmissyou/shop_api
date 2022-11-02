from datetime import datetime

import django_filters as filters
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q

from .models import Shop


class ShopFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city__name')
    street = filters.CharFilter(field_name='street__name')
    open = filters.NumberFilter(
        method='is_open_filter',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
    )

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def is_open_filter(self, queryset, name):
        now = datetime.now().time()
        if self.request.query_params.get('open', None) == 0:
            return queryset.filter(
                Q(open_time__gte=now) | Q(close_time__lte=now)
            )
        return queryset.filter(open_time__lte=now, close_time__gte=now)
