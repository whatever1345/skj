# Generated by Django 3.2 on 2023-01-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSportManager', '0003_auto_20230118_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='established_since',
            field=models.DateTimeField(),
        ),
    ]
