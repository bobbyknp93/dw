# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-26 08:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contact_method',
            field=models.CharField(choices=[('Email', 'Email'), ('Call', 'Call'), ('Text', 'Text')], default='Email', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 25, 8, 49, 21, 426339)),
        ),
    ]
