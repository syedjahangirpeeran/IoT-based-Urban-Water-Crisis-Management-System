# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-08 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uwc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensors',
            name='sensor5',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sensors',
            name='sensor6',
            field=models.FloatField(default=0),
        ),
    ]