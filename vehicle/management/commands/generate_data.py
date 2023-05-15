import string
import random

from django.core.management import BaseCommand
from faker import Faker

from vehicle.models import Enterprise, Brand, Driver, Manager, Vehicle


class Command(BaseCommand):
    def create_vehicle_number(self):
        fake = Faker('ru_RU')
        number = ''.join(fake.random_letters(length=1)).upper()
        number += ''.join([random.choice(string.digits) for _ in range(3)])
        number += ''.join(fake.random_letters(length=2)).upper()
        number += ''.join([random.choice(string.digits) for _ in range(2)])
        return number

    def add_arguments(self, parser):
        parser.add_argument('num_vehicles', type=int, help='Number of Cars per Enterprise')
        parser.add_argument('num_drivers', type=int, help='Number of Drivers per Enterprise')

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        brands = [Brand.objects.create(title=fake.name()) for _ in range(5)]
        num_vehicles = options['num_vehicles']
        num_drivers = options['num_drivers']

        enterprises = [
            Enterprise.objects.create(name=f'Test enterprise {i}') for i in range(1, 4)
        ]
        for j in range(1, num_vehicles + 1):
            vehicle = Vehicle.objects.create(
                price=fake.random_int(min=100000, max=5000000, step=10000),
                release_year=fake.random_int(min=1990, max=2022),
                mileage=fake.random_int(min=1000, max=200000, step=1000),
                number=self.create_vehicle_number(),
                brand=random.choice(brands),
                enterprise=random.choice(enterprises)
            )
            driver = Driver(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(18, 80),
                salary=random.randint(24000, 80000),
                vehicle=vehicle,
                enterprise=random.choice(enterprises),
                is_active=False
            )
            if j % 10 == 0:
                driver.is_active = True
            driver.save()
        self.stdout.write(self.style.SUCCESS("Data created successfully"))
