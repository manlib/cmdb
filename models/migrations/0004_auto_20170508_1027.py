# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20170505_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.Employee', verbose_name='\u90e8\u95e8\u9886\u5bfc'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[(b'on', '\u5728\u804c'), (b'dimission', '\u79bb\u804c'), (b'vacation', '\u4f11\u5047')], default=b'on', max_length=64, verbose_name='\u5728\u804c\u72b6\u6001'),
        ),
    ]
