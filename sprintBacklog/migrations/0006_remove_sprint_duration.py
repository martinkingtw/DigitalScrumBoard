# Generated by Django 2.2.5 on 2019-11-09 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprintBacklog', '0005_remove_sprint_sprint_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint',
            name='duration',
        ),
    ]