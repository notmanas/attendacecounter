# Generated by Django 3.0.5 on 2020-04-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0002_auto_20200427_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classandsub',
            name='class_name',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='classandsub',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
