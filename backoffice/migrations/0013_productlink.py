# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0012_auto_20170514_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField(blank=True, max_length=3000, null=True, verbose_name='Lien vers la fiche produit')),
                ('Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backoffice.Product')),
            ],
        ),
    ]
