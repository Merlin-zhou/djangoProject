# Generated by Django 3.1.1 on 2020-10-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20201020_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=100),
        ),
    ]
