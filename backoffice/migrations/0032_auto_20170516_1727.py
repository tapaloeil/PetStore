# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0031_auto_20170516_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Slug',
            new_name='slug',
        ),
    ]