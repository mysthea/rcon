# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concrete',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=20, verbose_name='klasa')),
            ],
        ),
        migrations.CreateModel(
            name='Diametersw',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('value', models.IntegerField(verbose_name='wartość')),
            ],
        ),
        migrations.CreateModel(
            name='Dsit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=20, verbose_name='typ')),
            ],
        ),
        migrations.CreateModel(
            name='Punching',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('b', models.DecimalField(max_digits=3, decimal_places=1)),
                ('h', models.DecimalField(max_digits=3, decimal_places=1)),
                ('dx', models.DecimalField(max_digits=3, decimal_places=1)),
                ('dy', models.DecimalField(max_digits=3, decimal_places=1)),
                ('lx', models.DecimalField(max_digits=2, decimal_places=1)),
                ('ly', models.DecimalField(max_digits=2, decimal_places=1)),
                ('ad', models.DecimalField(max_digits=2, decimal_places=1)),
                ('lambda_u', models.IntegerField()),
                ('asx', models.DecimalField(max_digits=3, decimal_places=1)),
                ('asy', models.DecimalField(max_digits=3, decimal_places=1)),
                ('ved', models.DecimalField(max_digits=4, decimal_places=1)),
                ('beta', models.DecimalField(max_digits=3, decimal_places=2)),
                ('vrdc', models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=3)),
                ('vrdmax', models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=3)),
                ('c_class', models.ForeignKey(to='app.Concrete')),
                ('dsit', models.ForeignKey(to='app.Dsit')),
                ('dsw', models.ForeignKey(to='app.Diametersw')),
            ],
        ),
        migrations.CreateModel(
            name='Sect',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=20, verbose_name='typ')),
            ],
        ),
        migrations.CreateModel(
            name='Steel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=20, verbose_name='klasa')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=30, verbose_name='typ')),
            ],
        ),
        migrations.AddField(
            model_name='punching',
            name='s_class',
            field=models.ForeignKey(to='app.Steel'),
        ),
        migrations.AddField(
            model_name='punching',
            name='sect',
            field=models.ForeignKey(to='app.Sect'),
        ),
        migrations.AddField(
            model_name='punching',
            name='support',
            field=models.ForeignKey(to='app.Support'),
        ),
    ]
