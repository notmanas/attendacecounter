# Generated by Django 3.0.5 on 2020-04-30 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('att_app', '0007_auto_20200429_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('day', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=40)),
                ('lec1', models.CharField(max_length=30)),
                ('lec2', models.CharField(max_length=30)),
                ('lec3', models.CharField(max_length=30)),
                ('lec4', models.CharField(max_length=30)),
                ('lec5', models.CharField(max_length=30)),
                ('lec6', models.CharField(max_length=30)),
                ('lec7', models.CharField(max_length=30)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='att_app.student')),
            ],
            options={
                'verbose_name': 'Attendence Table',
                'verbose_name_plural': 'Attendence Tables',
            },
        ),
    ]
