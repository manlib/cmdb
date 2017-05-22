# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_employee_leave_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeasset',
            name='product_no',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='officeasset',
            name='manufactory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ManuFactory', verbose_name='\u54c1\u724c'),
        ),
    ]
