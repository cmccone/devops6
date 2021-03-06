# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='\u4f5c\u8005\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u4f5c\u8005\u90ae\u7bb1')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('address', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u4f5c\u8005\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u4f5c\u8005\u4fe1\u606f',
                'verbose_name_plural': '\u4f5c\u8005\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u51fa\u7248\u5546\u540d\u79f0')),
                ('address', models.CharField(max_length=5, verbose_name='\u51fa\u7248\u5546\u5730\u5740')),
                ('city', models.CharField(blank=True, max_length=60, null=True, verbose_name='\u51fa\u7248\u5546\u57ce\u5e02')),
            ],
            options={
                'verbose_name': '\u51fa\u7248\u5546\u4fe1\u606f',
                'verbose_name_plural': '\u51fa\u7248\u5546\u4fe1\u606f',
            },
        ),
    ]
