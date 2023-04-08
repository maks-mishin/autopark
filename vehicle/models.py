from django.db import models


class Brand(models.Model):
    BRAND_TYPES = [
        ('PASS', 'Легковой'),
        ('TRUCK', 'Грузовой'),
        ('BUS', 'Автобус')
    ]
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    type = models.CharField(
        max_length=10,
        choices=BRAND_TYPES,
    )
    gas_tank_volume = models.IntegerField(
        verbose_name='Объем бака',
        default=30
    )
    seats_number = models.IntegerField(
        verbose_name='Количество мест',
        default=4
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Vehicle(models.Model):
    price = models.IntegerField(verbose_name='Стоимость')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег')
    number = models.CharField(
        max_length=20,
        verbose_name='Номер'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='vehicles',
        verbose_name='Бренд'
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
