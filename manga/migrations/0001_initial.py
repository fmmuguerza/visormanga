# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter_title', models.CharField(max_length=200)),
                ('chapter', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name=b'date published')),
                ('updated_at', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name=b'date published')),
                ('updated_at', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('page_number', models.IntegerField(default=0)),
                ('chapter', models.ForeignKey(related_name='images', to='manga.Chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(related_name='chapters', to='manga.Manga'),
        ),
    ]
