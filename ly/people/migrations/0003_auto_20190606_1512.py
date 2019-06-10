# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20190606_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='shcool_name',
            new_name='school_name',
        ),
    ]
