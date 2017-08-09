# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0014_auto_20150505_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangtransaksi',
            name='total_harga',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
