# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_loci', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectlocation',
            name='object_id',
            field=models.CharField(db_index=True, max_length=32),
        ),
    ]
