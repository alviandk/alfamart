# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0015_barangtransaksi_total_harga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailtransaksi',
            name='customer',
        ),
    ]
