from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Brand(models.Model):
    BRAND_TYPES = [
        ('PASS', 'Легковой'),
        ('TRUCK', 'Грузовой'),
        ('BUS', 'Автобус')
    ]
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        unique=True
    )
    type = models.CharField(
        max_length=10,
        choices=BRAND_TYPES,
        verbose_name='Тип авто'
    )
    body_type = models.CharField(
        max_length=70,
        help_text='Тип кузова',
        verbose_name='Тип кузова',
        null=True
    )
    fuel_tank = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Объем бака',
        help_text='Объем топливного бака',
        default=30,
        null=True
    )
    seats_number = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(70)],
        verbose_name='Вместимость',
        help_text='Количество пассажиров',
        null=True
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Vehicle(models.Model):
    number = models.CharField(
        max_length=20,
        verbose_name='Гос. номер',
        unique=True
    )
    price = models.IntegerField(
        verbose_name='Стоимость'
    )
    release_year = models.IntegerField(
        verbose_name='Год выпуска'
    )
    mileage = models.IntegerField(
        verbose_name='Пробег'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='vehicles',
        verbose_name='Бренд',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['price']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.number}'
