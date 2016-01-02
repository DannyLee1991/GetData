# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProvCity',
            fields=[
                ('_id', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='TimeHousingPriceOfOneHand',
            fields=[
                ('_id', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['time'],
            },
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='TimeHousingPriceOfSecondHand',
            fields=[
                ('_id', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['time'],
            },
            bases=None,
            managers=None,
        ),
    ]
