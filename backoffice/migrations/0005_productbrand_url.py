# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0004_auto_20170514_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='URL',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
