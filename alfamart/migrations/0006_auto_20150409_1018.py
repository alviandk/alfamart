# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0005_auto_20150316_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='harga_satuan',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
