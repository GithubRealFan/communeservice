# Generated by Django 4.2.2 on 2023-06-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='password',
            field=models.CharField(default='commune1234', max_length=255),
            preserve_default=False,
        ),
    ]
