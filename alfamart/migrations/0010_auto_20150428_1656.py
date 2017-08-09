# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0009_auto_20150428_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barangtransaksi',
            name='barang',
            field=models.ForeignKey(related_name='barang_yang_diulang', blank=True, to='alfamart.Barang', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barangtransaksi',
            name='detail',
            field=models.ForeignKey(related_name='detail-transaksi', blank=True, to='alfamart.DetailTransaksi', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barangtransaksi',
            name='diskon',
            field=models.ForeignKey(related_name='diskon_barang', blank=True, to='alfamart.Diskon', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barangtransaksi',
            name='jumlah_barang',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diskon',
            name='diskon',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diskon',
            name='nama_barang',
            field=models.ForeignKey(related_name='barang_diskon', blank=True, to='alfamart.Barang', null=True),
            preserve_default=True,
        ),
    ]
