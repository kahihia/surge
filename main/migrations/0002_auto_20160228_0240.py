# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='price',
            field=models.IntegerField(default=1050),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='bidding_end_time',
            field=models.DateTimeField(default=main.models.bid_time),
        ),
    ]