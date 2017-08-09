# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kode_barang', models.CharField(max_length=10)),
                ('nama_barang', models.CharField(max_length=250)),
                ('harga_beli', models.IntegerField()),
                ('harga_jual', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diskon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diskon', models.IntegerField()),
                ('nama_barang', models.ForeignKey(related_name='barang_diskon', to='alfamart.Barang')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perusahaan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kode_perusahaan', models.CharField(max_length=15)),
                ('nama_perusahaan', models.CharField(max_length=250)),
                ('alamat', models.CharField(max_length=250)),
                ('kota', models.CharField(max_length=50)),
                ('kode_pos', models.CharField(max_length=7)),
                ('no_telepon', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stok',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kategori', models.CharField(max_length=50)),
                ('satuan', models.CharField(max_length=50)),
                ('jumlah', models.IntegerField()),
                ('nama_barang', models.ForeignKey(related_name='barang_stok', to='alfamart.Barang')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jumlah_barang', models.IntegerField()),
                ('harga_satuan', models.ForeignKey(to='alfamart.Stok')),
                ('nama_barang', models.ForeignKey(related_name='barang_transaksi', to='alfamart.Barang')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='barang',
            name='perusahaan',
            field=models.ForeignKey(related_name='asal', to='alfamart.Perusahaan'),
            preserve_default=True,
        ),
    ]
