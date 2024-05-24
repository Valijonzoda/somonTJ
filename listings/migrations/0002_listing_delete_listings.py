# Generated by Django 5.0.6 on 2024-05-24 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_delete_images_categories_image"),
        ("listings", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "listings_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="listings_id"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="images/listings/")),
                ("price", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.categories",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.locations"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Listings",
            },
        ),
        migrations.DeleteModel(
            name="Listings",
        ),
    ]