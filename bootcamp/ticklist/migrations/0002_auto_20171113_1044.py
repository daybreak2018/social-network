# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 10:44
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticklist',
            name='end_date',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(models.IntegerField(validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(datetime.datetime(2017, 11, 13, 10, 44, 6, 303918))]))]),
        ),
        migrations.AlterField(
            model_name='ticklist',
            name='start_date',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(datetime.datetime(2017, 11, 13, 10, 44, 6, 303918))]),
        ),
    ]
