# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manageman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('manageman_id', models.IntegerField()),
                ('manageman_name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('school_id', models.IntegerField()),
                ('shcool_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='manageman',
            name='my_school',
            field=models.OneToOneField(to='people.school'),
        ),
    ]
