# Generated by Django 4.2.2 on 2023-06-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_startmining_server_onoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='onoff',
            field=models.BooleanField(verbose_name=0),
        ),
    ]
