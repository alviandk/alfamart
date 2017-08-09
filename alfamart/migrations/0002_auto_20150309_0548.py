# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kasir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='transaksi',
            name='nama_kasir',
            field=models.ForeignKey(related_name='nama_kasir', default='', to='alfamart.Kasir'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaksi',
            name='tanggal_transaksi',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
