# Generated by Django 3.0.5 on 2020-05-03 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0018_auto_20200503_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labs',
            name='code',
        ),
        migrations.RemoveField(
            model_name='labs',
            name='total_lectures',
        ),
        migrations.RemoveField(
            model_name='theorysubjects',
            name='total_lectures',
        ),
    ]
