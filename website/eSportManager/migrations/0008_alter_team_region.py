# Generated by Django 3.2 on 2023-01-19 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eSportManager', '0007_alter_team_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='eSportManager.region'),
        ),
    ]
