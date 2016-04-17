# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_child'),
    ]

    operations = [
        migrations.CreateModel(
            name='newChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('nonvariableParent', models.CharField(max_length=20)),
                ('hpG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('strG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('magG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('skillG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spdG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lckG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('defG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('resG', models.DecimalField(decimal_places=2, max_digits=10)),
                ('strB', models.IntegerField()),
                ('magB', models.IntegerField()),
                ('skillB', models.IntegerField()),
                ('spdB', models.IntegerField()),
                ('lckB', models.IntegerField()),
                ('defB', models.IntegerField()),
                ('resB', models.IntegerField()),
                ('classP', models.CharField(max_length=30)),
                ('class2', models.CharField(max_length=30)),
            ],
        ),
    ]
