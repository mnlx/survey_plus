# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-07 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_auto_20171207_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfieldanswers',
            name='extends',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.TextField'),
        ),
    ]
