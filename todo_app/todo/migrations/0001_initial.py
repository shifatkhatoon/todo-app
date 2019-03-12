# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('task_name', models.CharField(max_length=50)),
                ('schedule_date', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('task_type', models.IntegerField(choices=[(1, 'Meeting'), (2, 'Interview'), (3, 'Other')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'task',
                'ordering': ('created_at',),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
    ]
