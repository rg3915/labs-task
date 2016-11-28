# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161127_0113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('name',), 'verbose_name': 'employee', 'verbose_name_plural': 'employees'},
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='full_name',
            new_name='name',
        ),
    ]
