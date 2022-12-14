# Generated by Django 3.1.5 on 2021-03-07 11:54

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("libraryfrontend", "0015_bookratingmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookratingmodel",
            name="rating",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
        migrations.AlterUniqueTogether(
            name="bookratingmodel",
            unique_together={("book", "user")},
        ),
    ]
