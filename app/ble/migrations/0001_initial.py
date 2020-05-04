# Generated by Django 2.2.6 on 2019-10-08 06:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_address', models.TextField(db_column='device_address')),
                ('device_name', models.TextField(db_column='device_name')),
                ('device_description', models.TextField(db_column='device_description')),
                ('registration_time', models.DateTimeField(db_column='registration_time', default=datetime.datetime(2019, 10, 8, 13, 43, 16, 357539))),
            ],
            options={
                'db_table': 'devices',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('rssi', models.IntegerField(db_column='rssi')),
                ('timestamp', models.DateTimeField(db_column='timestamp', default=datetime.datetime(2019, 10, 8, 13, 43, 16, 357539))),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ble.Devices')),
            ],
            options={
                'db_table': 'data',
                'ordering': ['-timestamp'],
                'managed': True,
            },
        ),
    ]
