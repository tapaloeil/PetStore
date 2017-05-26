# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-26 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreferences',
            name='SellPriceRMB',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Prix de vente (RMB)'),
        ),
    ]