# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0003_perusahaan_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perusahaan',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
