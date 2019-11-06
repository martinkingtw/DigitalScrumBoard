# Generated by Django 2.2.5 on 2019-11-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprintBacklog', '0005_remove_sprint_sprint_number'),
        ('productBacklog', '0010_auto_20191102_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pbi',
            name='sprint',
        ),
        migrations.AddField(
            model_name='pbi',
            name='sprint',
            field=models.ManyToManyField(to='sprintBacklog.Sprint'),
        ),
    ]