# Generated by Django 3.0.5 on 2020-06-06 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouterApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.CharField(max_length=18, unique=True, validators=[django.core.validators.MinLengthValidator(18)])),
                ('hostname', models.CharField(max_length=14, unique=True)),
                ('loopback', models.GenericIPAddressField(unique=True)),
                ('macaddress', models.CharField(max_length=17, unique=True, validators=[django.core.validators.MinLengthValidator(17)])),
            ],
        ),
    ]
