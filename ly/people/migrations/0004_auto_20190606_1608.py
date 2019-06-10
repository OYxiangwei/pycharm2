# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20190606_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('student_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('teacher_name', models.CharField(max_length=30)),
                ('my_school', models.ForeignKey(to='people.school')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='my_school',
            field=models.ManyToManyField(to='people.teacher'),
        ),
    ]
