# Generated by Django 2.2.1 on 2019-05-25 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobsConfig',
            new_name='Job',
        ),
    ]
