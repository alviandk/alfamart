# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alfamart', '0002_auto_20150309_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='perusahaan',
            name='logo',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
