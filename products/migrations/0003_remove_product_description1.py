# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-28 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200528_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description1',
        ),
    ]
