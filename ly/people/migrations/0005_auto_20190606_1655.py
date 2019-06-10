# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20190606_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='my_school',
            new_name='my_teacher',
        ),
    ]
