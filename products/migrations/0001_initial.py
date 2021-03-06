# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-24 09:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('docfile', models.FileField(default='img/default_profile.png', upload_to='Product/%Y/%m/%d')),
                ('description', models.CharField(default=False, max_length=160)),
                ('contact_method', models.CharField(choices=[('Email', 'Email'), ('Call', 'Call'), ('Text', 'Text')], default='Email', max_length=3)),
                ('contact_info', models.CharField(blank=True, max_length=160)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2016, 11, 23, 9, 27, 2, 832246))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'title',
                'verbose_name_plural': 'title',
                'ordering': ('docfile',),
            },
        ),
    ]
