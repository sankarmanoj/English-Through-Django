# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 03:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_page_welloffset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='imageWidth',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='page',
            name='wellOffset',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(12)]),
        ),
    ]
