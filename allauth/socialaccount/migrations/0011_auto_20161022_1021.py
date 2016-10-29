# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-22 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0010_auto_20161022_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('linkedin', 'LinkedIn'), ('google', 'Google'), ('linkedin_oauth2', 'LinkedIn')], max_length=30, verbose_name='provider'),
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('linkedin', 'LinkedIn'), ('google', 'Google'), ('linkedin_oauth2', 'LinkedIn')], max_length=30, verbose_name='provider'),
        ),
    ]