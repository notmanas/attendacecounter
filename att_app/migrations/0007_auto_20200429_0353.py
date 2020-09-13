# Generated by Django 3.0.5 on 2020-04-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0006_classandsub_total_lectures'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AddField(
            model_name='class',
            name='Lab1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='Lab2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='Lab3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='Lab4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='Lab5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='Lab6',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject1_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='class',
            name='subject2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject2_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='class',
            name='subject3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject3_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='class',
            name='subject4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject4_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='class',
            name='subject5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject5_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='class',
            name='subject6',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='class',
            name='subject6_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]