# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160220_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
