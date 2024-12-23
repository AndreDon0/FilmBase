# Generated by Django 5.1.3 on 2024-12-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_alter_profile_catalog_view_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='enable_crazy_settings',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='theme',
            field=models.CharField(choices=[('As system', 'Как в системе'), ('light', 'Светлая'), ('dark', 'Тёмная')], default='light', max_length=10),
        ),
    ]
