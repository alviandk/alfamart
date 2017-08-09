# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0016_remove_detailtransaksi_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtransaksi',
            name='customer',
            field=models.ForeignKey(blank=True, to='alfamart.Customer', null=True),
            preserve_default=True,
        ),
    ]
