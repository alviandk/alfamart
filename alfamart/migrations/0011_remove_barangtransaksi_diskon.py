# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0010_auto_20150428_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barangtransaksi',
            name='diskon',
        ),
    ]
