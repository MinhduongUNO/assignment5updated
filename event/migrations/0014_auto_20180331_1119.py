# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20180331_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_record',
            name='Event_Description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='event.Event'),
        ),
    ]