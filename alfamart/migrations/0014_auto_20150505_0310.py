# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alfamart', '0013_auto_20150429_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=100, null=True, blank=True)),
                ('jenis_kelamin', models.CharField(blank=True, max_length=1, null=True, choices=[(b'L', b'Laki-Laki'), (b'P', b'Perempuan')])),
                ('tanggal_lahir', models.DateField(null=True, blank=True)),
                ('alamat', models.CharField(max_length=50, null=True, blank=True)),
                ('kota', models.CharField(max_length=25, null=True, blank=True)),
                ('kode_pos', models.CharField(max_length=5, null=True, blank=True)),
                ('no_hp', models.CharField(max_length=12, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='customer',
            field=models.OneToOneField(null=True, blank=True, to='alfamart.Customer'),
            preserve_default=True,
        ),
    ]
