# Generated by Django 4.2.2 on 2023-06-19 08:29

import django.core.validators
from django.db import migrations, models
import ep_190623.my_music_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_music_app', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), ep_190623.my_music_app.models.validate_string]),
        ),
    ]