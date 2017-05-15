# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(blank=True, max_length=200, null=True)),
                ('Description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Catégorie de produits')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ProductSubType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backoffice.ProductType'),
        ),
    ]
