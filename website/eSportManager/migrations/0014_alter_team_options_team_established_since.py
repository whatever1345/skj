# Generated by Django 4.1 on 2023-01-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSportManager', '0013_alter_player_options_alter_team_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-established_since']},
        ),
        migrations.AddField(
            model_name='team',
            name='established_since',
            field=models.DateField(null=True),
        ),
    ]
