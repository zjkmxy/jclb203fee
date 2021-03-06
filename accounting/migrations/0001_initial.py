# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-06 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating', models.DateField(verbose_name='Dating')),
                ('desc', models.CharField(max_length=200, verbose_name='Desc')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('cr_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Credit', to='accounting.Category')),
                ('dr_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Debit', to='accounting.Category')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Label')),
            ],
        ),
    ]
