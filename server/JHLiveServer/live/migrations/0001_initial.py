# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('phone', models.CharField(verbose_name='手机号', max_length=20)),
                ('password', models.CharField(verbose_name='密码', max_length=20)),
                ('nickname', models.CharField(verbose_name='昵称', max_length=100)),
                ('haveLive', models.IntegerField(verbose_name='是否在直播', default=1)),
            ],
        ),
    ]
