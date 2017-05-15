# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 20:13
from __future__ import unicode_literals

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0016_auto_20170514_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlink',
            name='BuyPrice',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=None, default_currency='EUR', max_digits=10, null=True, verbose_name="Prix d'achat"),
        ),
        migrations.AddField(
            model_name='productlink',
            name='BuyPrice_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euro'), ('HKD', 'Hong Kong Dollar'), ('GBP', 'Pound Sterling'), ('USD', 'US Dollar'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi')], default='EUR', editable=False, max_length=3),
        ),
    ]
