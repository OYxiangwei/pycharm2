# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('roomid', models.IntegerField()),
                ('loc', models.CharField(max_length=10)),
                ('roomname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('room', models.OneToOneField(to='spm.classroom')),
            ],
        ),
    ]
