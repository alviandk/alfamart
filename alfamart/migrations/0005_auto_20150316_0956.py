# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0004_auto_20150316_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='diskon',
            name='tanggal_mulai_promo',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='diskon',
            name='tanggal_selesai_diskon',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='kode_pos',
            field=models.CharField(max_length=7, null=True, blank=True),
            preserve_default=True,
        ),
    ]
