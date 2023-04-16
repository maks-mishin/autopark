from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Enterprise(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Название предприятия',
                            help_text='Название предприятия', unique=True)
    city = models.CharField(max_length=255, verbose_name='Город')
    country = models.CharField(max_length=255, verbose_name='Страна')

    class Meta:
        ordering = ['name']
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'

    def __str__(self):
        return f'{self.name} ({self.city})'


class Brand(models.Model):
    BRAND_TYPES = [
        ('PASS', 'Легковой'),
        ('TRUCK', 'Грузовой'),
        ('BUS', 'Автобус')
    ]
    title = models.CharField(max_length=255, verbose_name='Название',
                             unique=True)
    type = models.CharField(max_length=10, choices=BRAND_TYPES,
                            verbose_name='Тип авто')
    body_type = models.CharField(max_length=70, help_text='Тип кузова',
                                 verbose_name='Тип кузова', null=True)
    fuel_tank = models.DecimalField(max_digits=5, decimal_places=2,
                                    verbose_name='Объем бака',
                                    help_text='Объем топливного бака',
                                    default=30, null=True)
    seats_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)],
                                       verbose_name='Вместимость',
                                       help_text='Количество пассажиров',
                                       null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Vehicle(models.Model):
    price = models.IntegerField(verbose_name='Стоимость')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег')
    number = models.CharField(max_length=20, verbose_name='Гос. номер', unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,
                              related_name='vehicles', verbose_name='Бренд',
                              blank=True, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE,
                                   related_name='vehicles', verbose_name='Предприятие',
                                   blank=True, null=True)

    class Meta:
        ordering = ['price']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.number}'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__enterprise = self.enterprise

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude)
        if (self.enterprise != self.__enterprise) and (self.enterprise is not None):
            if self.has_active_driver():
                raise ValidationError('У автомобиля есть активный водитель')

    def has_active_driver(self):
        return self.drivers.filter(is_active=True).exists()


class Driver(models.Model):
    first_name = models.CharField(max_length=80, verbose_name='Имя')
    last_name = models.CharField(max_length=80, verbose_name='Фамилия')
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)], verbose_name='Возраст')
    salary = models.IntegerField(verbose_name='Зарплата')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='drivers', verbose_name='Авто')
    enterprise = models.ForeignKey(Enterprise, on_delete=models.SET_NULL,
                                   related_name='drivers', verbose_name='Предприятие',
                                   null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def check_active_car(self):
        if not self.vehicle:
            raise ValidationError('У водителя нет привязки к машине')
        if self.vehicle.has_active_driver():
            raise ValidationError('Есть активный водитель')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__is_active = self.is_active
        self.__vehicle = self.vehicle

    def clean_fields(self, exclude=None) -> None:
        super().clean_fields(exclude)
        if self.is_active != self.__is_active and self.is_active:
            self.check_active_car()
        if self.is_active and self.vehicle != self.__vehicle:
            raise ValidationError('Активный водитель не может сменить машину')