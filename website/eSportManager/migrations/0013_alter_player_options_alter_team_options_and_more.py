# Generated by Django 4.1 on 2023-01-20 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eSportManager', '0012_alter_coach_current_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.RemoveField(
            model_name='team',
            name='established_since',
        ),
    ]