# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-01 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0017_auto_20180331_1350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emp_Record',
            new_name='EmpRecord',
        ),
    ]
