# Generated by Django 2.2.6 on 2019-11-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('details', models.TextField()),
                ('slug', models.SlugField(default='', unique=True)),
                ('duration', models.IntegerField(default=2, verbose_name='Sprint Duration(week)')),
            ],
        ),
    ]
