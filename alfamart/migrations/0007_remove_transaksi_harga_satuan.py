# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0006_auto_20150409_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksi',
            name='harga_satuan',
        ),
    ]
