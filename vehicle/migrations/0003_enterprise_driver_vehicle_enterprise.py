# Generated by Django 4.2.3 on 2023-07-23 22:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_brand_vehicle_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название предприятия', max_length=255, unique=True, verbose_name='Название предприятия')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Предприятие',
                'verbose_name_plural': 'Предприятия',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=80, verbose_name='Фамилия')),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(80)], verbose_name='Возраст')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
                ('enterprise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drivers', to='vehicle.enterprise', verbose_name='Предприятие')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drivers', to='vehicle.vehicle', verbose_name='Авто')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='enterprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='vehicle.enterprise', verbose_name='Предприятие'),
        ),
    ]
