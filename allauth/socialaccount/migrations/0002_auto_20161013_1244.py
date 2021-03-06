# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-13 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(choices=[('linkedin_oauth2', 'LinkedIn'), ('google', 'Google'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn')], max_length=30, verbose_name='provider'),
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(choices=[('linkedin_oauth2', 'LinkedIn'), ('google', 'Google'), ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn')], max_length=30, verbose_name='provider'),
        ),
    ]
