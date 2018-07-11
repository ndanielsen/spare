# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-29 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_pickuptime_neighborhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationfulfillment',
            name='pickup_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donations.PickupTime'),
            preserve_default=False,
        ),
    ]
