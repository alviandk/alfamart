# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0011_remove_barangtransaksi_diskon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtransaksi',
            name='jam_transaksi',
            field=models.TimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='tanggal_transaksi',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
