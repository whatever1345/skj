# Generated by Django 3.2 on 2023-01-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSportManager', '0006_alter_team_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='region',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]