# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0007_remove_transaksi_harga_satuan'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarangTransaksi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jumlah_barang', models.IntegerField()),
                ('barang', models.ForeignKey(related_name='barang_yang_diulang', to='alfamart.Barang')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetailTransaksi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_faktur', models.IntegerField(max_length=10)),
                ('tanggal_transaksi', models.DateField(null=True, blank=True)),
                ('jam_transaksi', models.TimeField(null=True, blank=True)),
                ('nama_kasir', models.ForeignKey(related_name='nama_kasir', to='alfamart.Kasir')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='nama_kasir',
        ),
        migrations.DeleteModel(
            name='Transaksi',
        ),
        migrations.AddField(
            model_name='barangtransaksi',
            name='detail',
            field=models.ForeignKey(related_name='detail-transaksi', to='alfamart.DetailTransaksi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barangtransaksi',
            name='diskon',
            field=models.ForeignKey(related_name='diskon_barang', to='alfamart.Diskon'),
            preserve_default=True,
        ),
    ]
