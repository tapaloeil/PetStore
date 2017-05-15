# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 20:15
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0020_auto_20170514_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlink',
            name='LinkBuyPrice',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='EUR', max_digits=10, verbose_name="Prix d'achat"),
        ),
        migrations.AddField(
            model_name='productlink',
            name='LinkBuyPrice_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'Euro'), ('HKD', 'Hong Kong Dollar'), ('GBP', 'Pound Sterling'), ('USD', 'US Dollar'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi')], default='EUR', editable=False, max_length=3),
        ),
    ]
