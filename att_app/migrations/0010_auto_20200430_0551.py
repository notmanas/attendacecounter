# Generated by Django 3.0.5 on 2020-04-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0009_auto_20200430_0547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec5',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec6',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='lec7',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
