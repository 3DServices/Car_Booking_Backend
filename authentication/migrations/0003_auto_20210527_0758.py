# Generated by Django 3.2.3 on 2021-05-27 07:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210520_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.CharField(default=uuid.UUID('176190e9-a3b5-43ed-b21a-2cafeb5e1862'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fleetmanager',
            name='id',
            field=models.CharField(default=uuid.UUID('a3896cf5-1b32-40a5-b78f-4cccdbeca411'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='id',
            field=models.CharField(default=uuid.UUID('7029c5dd-08b5-4cfe-a3b2-680fc26eb3e5'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='systemadmin',
            name='id',
            field=models.CharField(default=uuid.UUID('0df2939b-0b6c-4264-8731-d55529c4a4a0'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='Id',
            field=models.CharField(default=uuid.UUID('a364ff12-a378-4724-bfb8-1e655c147c0d'), max_length=50, primary_key=True, serialize=False),
        ),
    ]
