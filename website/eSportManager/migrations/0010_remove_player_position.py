# Generated by Django 3.2 on 2023-01-19 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eSportManager', '0009_alter_player_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
    ]
