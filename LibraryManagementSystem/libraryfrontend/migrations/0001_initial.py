# Generated by Django 3.1.5 on 2021-01-19 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthorModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("about", models.TextField()),
                ("birth_date", models.DateField()),
                ("death_date", models.DateField()),
                ("author_image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="CategoryModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PublisherModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="BookModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("published_date", models.DateField()),
                ("book_cover", models.ImageField(upload_to="")),
                ("description", models.TextField()),
                ("amount", models.IntegerField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="libraryfrontend.authormodel",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="libraryfrontend.categorymodel",
                    ),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="libraryfrontend.publishermodel",
                    ),
                ),
            ],
        ),
    ]
