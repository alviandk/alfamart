# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0012_auto_20150429_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtransaksi',
            name='tanggal_transaksi',
            field=models.DateField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
