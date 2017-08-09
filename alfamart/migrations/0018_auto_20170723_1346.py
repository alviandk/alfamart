# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0017_detailtransaksi_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barang',
            name='harga_beli',
            field=models.IntegerField(max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barang',
            name='harga_jual',
            field=models.IntegerField(max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barang',
            name='kode_barang',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barang',
            name='nama_barang',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='alamat',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='email',
            field=models.EmailField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='kode_perusahaan',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='kode_pos',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='kota',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perusahaan',
            name='nama_perusahaan',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stok',
            name='jumlah',
            field=models.IntegerField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stok',
            name='kategori',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stok',
            name='satuan',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
    ]
