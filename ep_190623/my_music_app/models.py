from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_string(value):
    # can contain letters, numbers and underscore
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError(
                'Ensure this value contains only letters, '
                'numbers, and underscore.'
            )


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_string,
        ),
    )

    email = models.EmailField(
    )

    age = models.PositiveIntegerField(
        blank=True, null=True,
    )


class Album(models.Model):
    class Meta:
        ordering = ('pk', )

    album_name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=(
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ('R&B Music', 'R&B Music'),
            ('Rock Music', 'Rock Music'),
            ('Country Music', 'Country Music'),
            ('Dance Music', 'Dance Music'),
            ('Hip Hop Music', 'Hip Hop Music'),
            ('Other', 'Other'),
        ),
    )

    description = models.TextField(
        blank=True, null=True,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        ),
    )
