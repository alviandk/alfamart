# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alfamart', '0008_auto_20150428_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtransaksi',
            name='jenis_transaksi',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'T', b'Tunai'), (b'K', b'Kartu Kredit')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='jumlah_bayar',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kasir',
            name='alamat',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kasir',
            name='jenis_kelamin',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'L', b'Laki-Laki'), (b'P', b'Perempuan')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kasir',
            name='kode_pos',
            field=models.CharField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kasir',
            name='no_hp',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kasir',
            name='tanggal_lahir',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kasir',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='nama_kasir',
            field=models.ForeignKey(related_name='nama_kasir', blank=True, to='alfamart.Kasir', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='no_faktur',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kasir',
            name='nama',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
