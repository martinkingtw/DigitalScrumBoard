# Generated by Django 2.2.7 on 2019-11-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('PO', 'Product Owner'), ('SC', 'Scrum Master'), ('D', 'Developer')], default='D', max_length=2),
        ),
    ]
