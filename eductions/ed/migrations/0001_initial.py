# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('school_name', models.CharField(max_length=23)),
                ('school_ali', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('teacher_id', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=33)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='myschool',
            field=models.OneToOneField(to='ed.teacher'),
        ),
    ]
