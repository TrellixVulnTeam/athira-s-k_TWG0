# Generated by Django 3.0 on 2020-01-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_facultys'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentattendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=20)),
                ('stdid', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('hr1status', models.CharField(max_length=10)),
                ('hr2status', models.CharField(max_length=10)),
                ('hr3status', models.CharField(max_length=10)),
                ('hr4status', models.CharField(max_length=10)),
            ],
        ),
    ]