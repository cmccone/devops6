# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-31 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20171231_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.IntegerField(blank=True, choices=[(0, '\u65e0'), (1, '\u603b\u76d1'), (2, '\u7ecf\u7406'), (3, '\u7814\u53d1')], default='0', max_length=32, null=True),
        ),
    ]