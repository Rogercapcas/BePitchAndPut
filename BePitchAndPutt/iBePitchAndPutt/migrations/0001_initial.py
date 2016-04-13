# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('holes', models.IntegerField()),
                ('par', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hole_number', models.IntegerField()),
                ('meters', models.IntegerField()),
                ('handicap_hole', models.IntegerField()),
                ('field', models.ForeignKey(to='iBePitchAndPutt.Field')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hole_result', models.IntegerField()),
                ('total_result', models.IntegerField()),
                ('hole', models.ForeignKey(to='iBePitchAndPutt.Hole')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('handicap', models.FloatField()),
            ],
        ),
    ]
