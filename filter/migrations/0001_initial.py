# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-09 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=100)),
                ('operating_system', models.CharField(blank=True, max_length=100)),
                ('data_transfer', models.CharField(blank=True, max_length=100)),
                ('processor_speed', models.DecimalField(decimal_places=1, max_digits=2)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
