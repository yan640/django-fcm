# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_fcm', '0003_auto_20170320_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='reg_id',
            field=models.CharField(max_length=255, verbose_name='GCM Registration id'),
        ),
    ]