from django.db.models import (CASCADE, CharField, ForeignKey, Model,
                              PositiveSmallIntegerField, TimeField)


class City(Model):
    name = CharField(
        unique=True,
        max_length=200,
        verbose_name='Название города',
        help_text='Введите название города',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Street(Model):
    name = CharField(
        unique=True,
        max_length=200,
        verbose_name='Название улицы',
        help_text='Введите название улицы',
    )
    city = ForeignKey(
        City,
        on_delete=CASCADE,
        verbose_name='Город улицы',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    def __str__(self):
        return self.name


class Shop(Model):
    name = CharField(
        unique=True,
        max_length=200,
        verbose_name='Название магазина',
        help_text='Введите название магазина',
    )
    city = ForeignKey(
        City,
        on_delete=CASCADE,
        verbose_name='Город магазина',
    )
    street = ForeignKey(
        Street,
        on_delete=CASCADE,
        verbose_name='Улица магазина',
    )
    house = PositiveSmallIntegerField(
        verbose_name='Номер дома',
        help_text='Введите номер дома',
    )
    open_time = TimeField(
        verbose_name='Время открытия',
        help_text='Введите время открытия',
    )
    close_time = TimeField(
        verbose_name='Время закрытия',
        help_text='Введите время закрытия',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name
