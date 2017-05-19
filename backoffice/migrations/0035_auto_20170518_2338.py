# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 21:38
from __future__ import unicode_literals

import backoffice.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0034_auto_20170516_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.ProductBrand', verbose_name='Marque'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductName',
            field=models.CharField(max_length=200, verbose_name='Nom du produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductSubType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.ProductSubType', verbose_name='Type de produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.ProductType', verbose_name='Catégorie de produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='Name',
            field=models.CharField(max_length=200, verbose_name='Marque'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(height_field='height', upload_to=backoffice.models.upload_location, width_field='width'),
        ),
        migrations.AlterField(
            model_name='productlink',
            name='Description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='productlink',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Product'),
        ),
        migrations.AlterField(
            model_name='productreferences',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.Product'),
        ),
        migrations.AlterField(
            model_name='productsubtype',
            name='SubType',
            field=models.CharField(max_length=200, verbose_name='Sous-atégorie de produits'),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='Type',
            field=models.CharField(max_length=200, verbose_name='Catégorie de produits'),
        ),
    ]